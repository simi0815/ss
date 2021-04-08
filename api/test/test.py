from elasticsearch import Elasticsearch

FIELD_REFL = {
    "uname": "username",
    "cid": "id",
    "gid": "gid",
    "tel": "phone"
}


class ESDatabase():
    def __init__(self):
        self.es = Elasticsearch(
            ['192.168.1.230:9200'],
            http_auth=('elastic', 'twdtwd'),
            use_ssl=True,
            verify_certs=False,
        )

    def _find_all(self, con):
        index_name = 'telegram_*'
        val = con.get("val")
        type = con.get("type")
        if not val or not type:
            return []
        if type not in FIELD_REFL.keys():
            return []
        match = {
            FIELD_REFL[type]: val
        }
        dsl = {
            "query": {
                "match": match
            }
        }
        print("dsl", dsl)
        res = self._find(index_name, dsl)
        return self.deal_res(res)

    def deal_res(self, res):
        try:
            _res = res["hits"]["hits"]
        except Exception:
            return []
        if not _res:
            return
        lis = []
        print(_res)
        for one in _res:
            source = one["_source"]
            uname = source.get(FIELD_REFL["uname"])
            cid = source.get(FIELD_REFL["cid"])
            gid = source.get(FIELD_REFL["gid"])
            tel = source.get(FIELD_REFL["tel"])
            _one = {
                "uname": uname,
                "cid": cid,
                "gid": gid,
                "tel": tel,
            }
            _o = {}
            for k, v in _one.items():
                if  v:
                    _o[k] = v
            lis.append(_o)
        return lis

    def _find(self, index, dsl):
        res = self.es.search(index=index, body=dsl)
        return res


d = ESDatabase()
print(d._find_all({"val": "989178195387", "type": "tel"}))
