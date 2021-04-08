from pymongo import MongoClient
from elasticsearch import Elasticsearch
import openpyxl

MONGO_ADDRESS = '192.168.1.231'
MONGO_PORT = 27017


class Database(object):
    def __init__(self, address=MONGO_ADDRESS, port=MONGO_PORT):
        self.es = Elasticsearch(
            ['192.168.1.230:9200'],
            request_timeout=30000,
        )
from api.test.tests import refl_dic

db = Database()
ins = list(db.es.indices.get_alias().keys())
ins.sort()
print(len(ins))
import json

print(ins)
fp = open("res7-1.js", "a+")

all = []
for i in ins:
    count = db.es.count(index=i).get("count")
    i_f = db.es.search(index=i, body={
        "query": {
            "match_all": {}
        }
    })
    row = i_f["hits"]["hits"][0]["_source"]

    all.append({
        "index": i,
        "describe":refl_dic.get(i,""),
        "count": count,
        "row": row
    })
all = sorted(all, key=lambda x: x["index"])
for onr in all:
    if onr["index"].startswith("."):
        continue
    fp.write("index = " + "\""+onr["index"] + "\"" + "\n")
    fp.write("describe = " + "\""+str(onr["describe"]) + "\"" + "\n")
    fp.write("count = " + str(onr["count"]) + "\n")
    fp.write("field = " + json.dumps(onr["row"]) + "\n")
    fp.write("///////////////////////////////////////////////")
    fp.write("\n")

