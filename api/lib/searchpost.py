DATABASE = "es"
TYPE_INDEX_REFL = {
    "tw": {
        "index": "tw_page*",
        "id_call": "user_id",
        "items": {
            "date": "date",
            "recom": "retweets_count",
            "content": "tweet"
        }
    },
    "telegram": {
        "index": "telegram_message*",
        "id_call": "id",
        "items": {

        }
    },
}

from elasticsearch import Elasticsearch
from api.conf.api_config import ES_IP_ADDRESSS


class SearchPost():
    def __init__(self, cid, ctype):
        self.cid = cid
        self.ctype = ctype
        self.es = Elasticsearch(
            ES_IP_ADDRESSS,
            request_timeout=30000
        )
    def search(self):
        if self.ctype not in TYPE_INDEX_REFL.keys():
            return []
        index = TYPE_INDEX_REFL[self.ctype]["index"]
        id_name = TYPE_INDEX_REFL[self.ctype]["id_call"]
        res = self._find_post(index, id_name, self.cid)
        if not res:
            return []
        count = res.get("hits", {}).get("total", {}).get("value", 0)
        if not count:
            return []
        res = res["hits"]["hits"]
        back_res = []
        for one in res:
            one = one["_source"]
            _one = {}
            for k, v in TYPE_INDEX_REFL[self.ctype]["items"].items():
                if one.get(v):
                    _one[k] = one[v]
            back_res.append(_one)
        return back_res

    def _find_post(self, index, id_name, cid):
        dsl = {
            "query": {
                "term": {
                    id_name: cid
                }
            }
        }
        try:
            res = self.es.search(index=index, body=dsl, size=100)
        except Exception:
            return {}
        return res


if __name__ == '__main__':
    sp = SearchPost(cid=1105045191407202310, ctype="tw")
    print(sp.search())
