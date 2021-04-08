from elasticsearch import Elasticsearch
from api.conf.api_config import ES_IP_ADDRESSS,ES_ONE_LIMIT
from api.conf.es_conf import ES_DB_REFL
from api.lib.name.parse_name import handle_name


class ESDatabase():
    def __init__(self):
        self.es = Elasticsearch(
            ES_IP_ADDRESSS,
            request_timeout=30000
        )

    def find(self, con):
        return self._find_all(con)

    def find_in_index(self, index, con):
        index_refl = ES_DB_REFL.get(index)
        if not index:
            raise Exception("没有指定的索引")
        res = self._get_index_res(con, index_refl.get("index"), index_refl.get("field_refl"),
                                  index_refl.get("ctype", ""),index_refl.get("resource",""))
        return res

    def _find_all(self, con):
        _res = []
        for index_info in ES_DB_REFL.values():
            index_res = self._get_index_res(con, index_info.get("index"), index_info.get("field_refl"),
                                            index_info.get("ctype",""),index_info.get("resource",""))
            _res.extend(index_res)
        return _res

    def _get_index_res(self, con, index, field_refl, ctype="",resource=""):
        res = self._find_in_index(index, con, field_refl)
        return self._deal_res(res, field_refl, ctype,resource)

    def _find_in_index(self, index_name, con, refl_dic):
        val = con.get("val")
        type = con.get("type")
        if not val or not type or not refl_dic:
            return None
        if type == "name" and "first_name" in refl_dic.keys():
            f_name, l_name = handle_name(val)
            if not f_name:
                return None
            dsl = {
                "query": {
                    "bool": {
                        "should": [
                            {
                                "match": {
                                    refl_dic["first_name"]: {
                                        "query": f_name,
                                        "minimum_should_match": "100%"
                                    }

                                }
                            },
                            {
                                "match": {
                                    refl_dic["last_name"]: {
                                        "query": l_name,
                                        "minimum_should_match": "100%"
                                    }
                                }
                            }
                        ]
                    }
                }
            }
            res = self._find(index_name, dsl)
            return res
        if type not in refl_dic.keys():
            return None

        match = {
            refl_dic[type]: {
                "query": val,
                "minimum_should_match": "100%"
            }
        }
        dsl = {
            "query": {
                "match": match
            }
        }
        res = self._find(index_name, dsl)
        return res

    def _find(self, index, dsl):
        res = self.es.search(index=index, body=dsl, size=ES_ONE_LIMIT)
        return res

    def _deal_res(self, res, refl_dic, c_type,resource):
        if not res or not refl_dic:
            return []
        try:
            _res = res["hits"]["hits"]
        except Exception:
            return []
        if not _res:
            return []
        lis = []
        for one in _res:
            source = one["_source"]
            uname = source.get(refl_dic.get("uname"))
            cid = source.get(refl_dic.get("cid"))
            gid = source.get(refl_dic.get("gid"))
            tel = source.get(refl_dic.get("tel"))
            email = source.get(refl_dic.get("email"))
            name = source.get(refl_dic.get("name", ""))
            first_name = source.get(refl_dic.get("first_name", ""))
            last_name = source.get(refl_dic.get("last_name", ""))
            gender = source.get(refl_dic.get("gender", ""))
            location = source.get(refl_dic.get("location", ""))
            birthday = source.get(refl_dic.get("birthday", ""))
            i_col = one["_type"]
            i_db = one["_index"]
            db_type = "es"
            if first_name and not name:
                if not last_name:
                    last_name = ""
                name = str(first_name) + " " + str(last_name)
            _one = {
                "uname": uname,
                "cid": cid,
                "gid": gid,
                "tel": tel,
                "name": name,
                "email": email,
                "gender": gender,
                "location": location,
                "birthday": birthday,
                "i_col": i_col,
                "i_db": i_db,
                "db_type": db_type,
                "ctype": c_type,
                "resource":resource
            }
            _o = {}
            for k, v in _one.items():
                if v:
                    _o[k] = v
            if not _o.get("cid") and _o.get("ctype"):
                _o.pop("ctype")
            lis.append(_o)
        return lis
if __name__ == '__main__':
    sadb = ESDatabase()
    res = sadb.find({"val": "Kamala Harris", "type": "name"})
    for i in res:
        print(i)
