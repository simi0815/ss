from api.utils.array import array_dels,deal_merge_list
class MeageData(object):
    def __init__(self, data):
        self.data = data

    def _concat(self, a, b):
        _res = []
        if isinstance(a, list):
            _res.extend(a)
        else:
            _res.append(a)
        if isinstance(b, list):
            _res.extend(b)
        else:
            _res.append(b)
        _res = set(_res)
        _res = list(_res)
        return _res

    def _merge_data(self, dict1, dict2):
        merge_one = {}
        for k1, v1 in dict1.items():
            for k2, v2 in dict2.items():
                if k1 == k2:
                    merge_one[k1] = self._concat(v1, v2)
            if k1 not in dict2:
                merge_one[k1] = v1
        for k2, v2 in dict2.items():
            if k2 not in dict1.keys():
                merge_one[k2] = v2
        if not merge_one.get("merge"):
            merge_one["merge"] = True
        return merge_one

    def _merge_all(self, li, res):
        merge_dict = {}

        for i in li:
            merge_dict = self._merge_data(merge_dict, res[i])

        return merge_dict



    def clean_data(self):
        self._clean_by_cid_and_ctype()
        self._clean_by_prop("email")
        self._clean_by_prop("tel")
        return self.data

    def _clean_by_prop(self, prop):
        res = self.data
        e_list = []
        # 通过相同prop合并
        for index in range(len(res)):
            one = res[index]
            #p是新从源数据拿到的一个数据
            p = one.get(prop)
            # 如果一条数据有这个属性
            if p:
                flag = False
                #将p变成一个列表,
                if not isinstance(p,list):
                    p = [p]
                for i in range(len(e_list)):
                        for o in p:
                            if o in e_list[i]["value"]:
                                e_list[i]["position"].append(index)

                                flag = True
                                break
                if not flag:
                    e_list.append({"position": [index, ], "value": p})
        print(e_list)
        mer_list = []
        need_del = []
        for need_mer in e_list:
            if len(need_mer["position"]) <= 1:
                continue
            mer_dic = self._merge_all(need_mer["position"], res)
            mer_list.append(mer_dic)
            need_del.extend(need_mer["position"])
        res = array_dels(need_del, res)
        res.extend(mer_list)
        self.data = res

    def _clean_by_cid_and_ctype(self):
        res = self.data
        e_list = []
        # 通过相同prop合并
        for index in range(len(res)):
            one = res[index]
            cid = one.get("cid")
            ctype = one.get("ctype")
            if not cid or not ctype:
                continue
            flag = False
            id_and_type = str(cid) + ctype
            for i in range(len(e_list)):

                if id_and_type in e_list[i]["value"]:
                    e_list[i]["position"].append(index)
                    flag = True
                    break
            if not flag:
                e_list.append({"position": [index, ], "value": id_and_type})
        mer_list = []
        need_del = []
        need_mers = []
        for need_mer in e_list:
            if len(need_mer["position"]) <= 1:
                continue
            need_mers.append(need_mer["position"])
        need_mers = deal_merge_list(need_mers)
        for need_mer in need_mers:
            mer_dic = self._merge_all(need_mer, res)
            print("mer_dic",mer_dic)
            mer_list.append(mer_dic)
            need_del.extend(need_mer)

        res = array_dels(need_del, res)
        res.extend(mer_list)
        self.data = res

if __name__ == '__main__':
    data = [
        {"name":"sb1","tel":"1234","email":"xxx@1631.com" ,"ctype":"ly","cid":"123"},
        {"name": "sb1", "tel": ["123","456"], "email": "xxx@163.com"},
        {"name": "sb2", "tel": "123", "email": ["xxx@165.com","gougou@dd.com"]},
        {"name": "sb23", "tel": "4567", "email": "xxx@1651.com","ctype":"ly","cid":"123"}
    ]
    md = MeageData(data)
    print(md.clean_data())