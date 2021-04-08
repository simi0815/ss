from pymongo import MongoClient

MONGO_ADDRESS = '192.168.1.231'
MONGO_PORT = 27017


class Database(object):
    def __init__(self, address=MONGO_ADDRESS, port=MONGO_PORT):
        self.conn = MongoClient(host=address, port=port, serverSelectionTimeoutMS=3000000)
        self.db = self.conn["lingying-db"]
        res = self.db["pdl-coll"].find({'email':'jack@eckhausfleet.com'})
        print(list(res))
d = Database()
# # l = ['a','b']
# # for index in range(len(l)):
# #    print ('当前水果 :', l[index])
#
# res = [
#     {
#         "_id": "5",
#         "email": "x@.com",
#         "tel": "",
#         "db_type": "mongo",
#         "name": "tom mahoney"
#     },
#     {
#         "_id": "6",
#         "email": "x@.com",
#         "company_name": "james c. gallo",
#         "title": "Manager",
#         "tel":""
#     },
#     {
#         "_id": "1",
#         "email": "hoo.com",
#         "company_name": "Ymca",
#         "fax": 8168108899,
#         "tel": "",
#
#     },
#     {
#         "_id": "2",
#         "email": "hoo.com",
#         "city": "kansas city",
#         "state": "mo",
#         "tel": "",
#     },
#     {
#         "_id": "6",
#         "email": "x@.com",
#         "company_name": "james c. gallo",
#         "title": "Manager",
#         "tel": "fs"
#     },
# ]
#
#
#
#
#
# def concat(a, b):
#     _res = []
#     if isinstance(a, list):
#         _res.extend(a)
#     else:
#         _res.append(a)
#     if isinstance(b, list):
#         _res.extend(b)
#     else:
#         _res.append(b)
#     _res = set(_res)
#     _res = list(_res)
#     return _res
#
#
# def merge_data(dict1, dict2):
#     print("我要合并",dict1,dict2)
#     merge_one = {}
#     for k1, v1 in dict1.items():
#         for k2, v2 in dict2.items():
#             if k1 == k2:
#                 merge_one[k1] = concat(v1, v2)
#         if k1 not in dict2:
#             merge_one[k1] = v1
#     for k2, v2 in dict2.items():
#         if k2 not in dict1.keys():
#             merge_one[k2] = v2
#     print("合并后",merge_one)
#     return merge_one
#
#
# def merge_all(li, res):
#     merge_dict = {}
#     print("li",li)
#     for i in li:
#         print("i",i)
#         merge_dict = merge_data(merge_dict, res[i])
#
#     return merge_dict
# def array_dels(n_d_li,li):
#     a_index = [i for i in range(len(li))]
#     a_index = set(a_index)
#     b_index = set(n_d_li)
#     index = list(a_index - b_index)
#     _res = [li[i] for i in index]
#     return _res
# def clean_data(res):
#
#     e_list = []
#     t_list =  []
#
#     for index in range(len(res)):
#         one = res[index]
#         email = one.get("email")
#         # 如果一条数据有email属性
#         if email:
#             flag = False
#             for i in range(len(e_list)):
#                 # 有就加入所在序号,没有重新添加
#                 if email == e_list[i]["value"]:
#                     e_list[i]["position"].append(index)
#                     flag = True
#             if not flag:
#                 e_list.append({"position": [index, ], "value": email})
#     print(e_list)
#
#     mer_list = []
#     need_del = []
#     for need_mer in e_list:
#         mer_dic = merge_all(need_mer["position"],res)
#         mer_list.append(mer_dic)
#         need_del.extend(need_mer["position"])
#
#     res = array_dels(need_del,res)
#
#     res.extend(mer_list)
#     return res
#
# dic = [
#     {
#
#     },
#     {"a": 1,
#      "b": 2,
#      "c": 5
#      },
#     {"a": 1,
#      "b": 3,
#      "d": 89
#      },
#     {"a": 1,
#      "b": 3,
#      "d": "fsfs"
#      }
# ]
# # print(merge_all([0, 1, 3], dic))
# # print("ds", merge_data(dic[0], dic[1]))
# print(clean_data(res))
