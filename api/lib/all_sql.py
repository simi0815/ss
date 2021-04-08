from api.lib.mon_sql import MongoDatabase
from api.lib.es_sql import ESDatabase
from api.utils.clean_mutil import clean_mul, array_sub
from api.lib.data.data_deal import MeageData


class Searilizer():
    def __init__(self, rd):
        self.rd = rd

    def get_con(self):
        val = self.rd.get("val")
        type = self.rd.get("type")
        ctype = self.rd.get("ctype")
        # if type in ["cid","gid"] and not ctype:
        #     raise Exception("查询社交id,群id需选定社交类型")
        if not val or not type:
            return None
        val = str(val)
        con = {
            "val": val,
            "type": type
        }

        return con


class AllDatabase(object):

    def find(self, res_dict):
        ser = Searilizer(res_dict)
        con = ser.get_con()
        if not con:
            return self.err_msg(5, "未接收到有效数据")
        back_re = self._find_in_all_db(con)
        if not back_re:
            return self.err_msg(2, "没有查询到结果")
        res = {
            "errno": 0,
            "data": {
                "all_data": back_re,
                "count": len(back_re)
            }
        }
        return res

    # 升级功能,深度查询
    def find_deepth(self, res_dict):
        back_re = self.find(res_dict)
        if back_re["errno"] == 0:
            back_re = back_re["data"]["all_data"]
        else:
            return back_re
        _res = []
        for onr_res in back_re:
            onr_all = self._find_one_deepth(onr_res, res_dict)
            _res.extend(onr_all)
        # for i in _res:
        #     print(i)
        back_re = self._clean_data(_res)
        res = {
            "errno": 0,
            "data": {
                "all_data": back_re,
                "count": len(back_re)
            }
        }
        return res

    def _find_one_deepth(self, one_res, con):
        _one_all, cur_eamils, cur_tels, has_searched_emails, has_searches_tels = [], [], [], [], []
        _one_all.append(one_res)
        type = con.get("type")
        val = con.get("val")
        if type == "tel":
            has_searches_tels.append(val)
        elif type == "email":
            has_searched_emails.append(val)
        # 将已有数据添加到已有表中
        def add_cur_emails_tels(one_res):
            nonlocal cur_eamils,cur_tels
            if one_res.get("email"):
                if isinstance(one_res.get("email"), list):
                    cur_eamils.extend(one_res.get("email"))
                else:
                    cur_eamils.append(one_res.get("email"))
                cur_eamils = clean_mul(cur_eamils)
            if one_res.get("tel"):
                if isinstance(one_res.get("tel"), list):
                    cur_tels.extend(one_res.get("tel"))
                else:
                    cur_tels.append(one_res.get("tel"))
                cur_tels = clean_mul(cur_tels)

        add_cur_emails_tels(one_res)
        while True:
            need_search_emails = array_sub(cur_eamils, has_searched_emails)
            need_search_tels = array_sub(cur_tels, has_searches_tels)
            if not need_search_emails and not need_search_tels:
                break
            for email in need_search_emails:
                deepth_res = self._find_in_all_db({"val": email, "type": "email"})
                _one_all.extend(deepth_res)
                has_searched_emails.append(email)
                for one in deepth_res:
                    add_cur_emails_tels(one)
            for tel in need_search_tels:
                deepth_res = self._find_in_all_db({"val": tel, "type": "tel"})
                _one_all.extend(deepth_res)
                has_searches_tels.append(tel)
                for one in deepth_res:
                    add_cur_emails_tels(one)
        return _one_all

    def _find_in_all_db(self, con):
        back_re = []
        db = MongoDatabase()
        mongo_res = db.find(con)
        back_re.extend(mongo_res)
        es_db = ESDatabase()
        es_res = es_db.find(con)
        back_re.extend(es_res)
        return back_re

    def _clean_data(self, data):
        return MeageData(data=data).clean_data()

    def err_msg(self, errno, msg):
        return {
            "errno": errno,
            "msg": msg
        }


if __name__ == '__main__':
    adb = AllDatabase()
    re = adb.find_deepth({"val": "13168713930", "type": "tel"})
    if re["errno"] == 0:
        al_da = re["data"]["all_data"]
        for e in al_da:
            print(e)
    else:
        print(re)
