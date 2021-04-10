from pymongo import MongoClient
from api.conf.api_config import MONGO_ADDRESS, MONGO_PORT, MONGO_ONE_LIMIT
from api.conf.mon_conf import MON_DB_REFL
from api.lib.exception import *
from api.middleware import db_hook
from api.lib.name.parse_name import handle_name, merge_name
from api.utils.stringfy import stringfy


class MongoDatabase(object):
    def __init__(self, address=MONGO_ADDRESS, port=MONGO_PORT):
        self.conn = MongoClient(host=address, port=port, serverSelectionTimeoutMS=3000000)

    def get_state(self):
        return self.conn is not None

    def find(self, condition):
        # 查询condition情况
        res = self._find_all(condition)
        return res

    def _deal_con(self, con):
        val = con.get("val")
        type = con.get("type")
        if not val or not type:
            raise ConditionException()
        if type == "name":
            return self._hander_name_con(con)
        return [
            {type: val}
        ]

    # 因为姓名比较特殊，单独处理
    def _hander_name_con(self, con):
        name = con.get("val")
        if con.get("type") != "name" or not name:
            raise ConditionNotName()
        first_n, last_n = handle_name(name)
        if not last_n:
            con = [{"first_name": first_n},
                   {"last_name": first_n},
                   {"name": first_n},
                   ]
            return con
        _condi = {
            "first_name": first_n,
            "last_name": last_n,
        }
        _condi_reve = {
            "first_name": last_n,
            "last_name": first_n,
        }

        full_name = merge_name(first_n, last_n)
        full_name_reve = merge_name(first_n, last_n, reverse=True)
        con = [
            _condi,
            _condi_reve,
            {"name": full_name},
            {"name": full_name_reve},
        ]

        return con

    def _find_all(self, condition):
        # 数据汇总列表
        o_list = []
        # 处理成mongo可查询的condition
        cons = self._deal_con(condition)
        # 循环遍历数据库和集合，依次查询条件condition
        for db_col, info in MON_DB_REFL.items():
            cur_cons = cons.copy()
            # 此处通过"."分离数据库和集合
            db, col = db_col.split(".")
            # 查询前从"db_hook.py"中查询有没有钩子函数
            be_attr = "before_{db}_{col}_{type}".format(db=db, col=col, type=condition.get("type"))
            be_attr = be_attr.replace("-", "_")
            if hasattr(db_hook, be_attr):
                hook = getattr(db_hook, be_attr)
                cur_cons = hook(condition)
            # 对照映射关系表，将查询条/件变成当前集合所能识别的字段,刪除沒用的con
            _cons = []
            for con in cur_cons:
                _con = con.copy()
                for k, v in con.items():
                    if k in info["field_refl"].keys():
                        if k != info["field_refl"][k]:
                            _con[info["field_refl"][k]] = _con[k]
                            _con.pop(k)
                    else:
                        _con.pop(k)
                if _con:
                    _cons.append(_con)
            if not _cons:
                continue
            print("将要在{col}里查询：".format(col=col), _cons)
            # 开始查询，_cons是一个列表，包含若干查询集合，每一个查询集合是一个查询条件
            find_res = self._find(_cons, db, col, ctype=info.get("ctype"), resource=info.get("resource"))
            # 反映射操作
            _res = []
            # 按照映射关系循环
            for one_res in find_res:
                _one = one_res.copy()
                for k, v in info["field_refl"].items():
                    if k != v:
                        _one[k] = one_res.get(v, "")
                        if _one.get(v):
                            _one.pop(v)
                if "first_name" in _one.keys():
                    f_name = str(_one.get("first_name"))
                    l_name = str(_one.get("last_name", ""))
                    t_name = merge_name(f_name, l_name)
                    _one["name"] = t_name
                if _one.get("tel"):
                    _one["tel"] = stringfy(_one.get("tel"))
                if _one.get("cid"):
                    _one["cid"] = stringfy(_one.get("cid"))
                _res.append(_one)
            # 反映射结束
            # 继续寻找钩子函数，因为此时返回的结果不是我想要的结果，需要进一步处理
            # 此时不再单独指定字段
            af_attr = "after_{db}_{col}".format(db=db, col=col)
            af_attr = af_attr.replace("-", "_")
            if hasattr(db_hook, af_attr):
                hook = getattr(db_hook, af_attr)
                _res = hook(_res)
            # 将每个表查询到的数据加到总结果中
            o_list.extend(_res)
        return o_list

    def _find(self, conditions, db, col, ctype=None, resource=None):
        _res = []
        for onr_con in conditions:
            res = self.conn[db][col].find(onr_con).limit(MONGO_ONE_LIMIT)
            # 数据加工
            for one in res:
                one["i_col"] = col
                one["i_db"] = db
                one["db_type"] = "mongo"
                if ctype:
                    one["ctype"] = ctype
                if resource:
                    one["resource"] = resource
                _res.append(one)
        return _res


if __name__ == '__main__':
    mdb = MongoDatabase()
    # res = mdb.find({"type": "tel", "val": "3525210652"})
    res = mdb.find({"val": "2561054395", "type": "cid"})
    # res = mdb.find({"val": "jacob tom", "type": "name"})

    # res = mdb.find({"val": "15153", "type": "tel"})
    # res = mdb.find({"val": "萌系小妹纸！！", "type": "uname"})

    # res = mdb.find({"val": "mara morais", "type": "name"})
    for onr in res:
        print(onr)
