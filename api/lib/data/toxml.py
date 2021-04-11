from api.utils.xml import store_xml
from api.conf.resource_refl import RESOURCE_REFL
order_list = ["姓名", "地址", "出生日期", "性别", "电话", "邮箱", "用户名", "社交ID", "社交类型","数据来源"]
CTYPE_REFLECT = {
    "facebook": "facebook",
    "twitter": "twitter",
    "fbm": "fbm",
    "vx": "voxer",
    "weibo": "weibo",
    "ins": "instagram",
    "ly": "linkedln",
    "voxer": "voxer",
    "telegram": "telegram",
    "ws": "whatsapp",
    "qq":"qq"
}


class StoreToXML(object):
    def __init__(self, data,strenth_col=None,sheet_name="ALL_INFO"):
        self.data = data
        self.sheet_name = sheet_name
        self.strenth_col = strenth_col
    def paser_xml(self):
        d_list = self.paser_content()
        url = store_xml(d_list, order_list, strenth_col=self.strenth_col, sheet_name="INFO")
        return url

    def paser_content(self):
        data_list = []
        for onr in self.data:
            name = onr.get("name", "")
            addr = onr.get("location", "")
            birthday = onr.get("birthday", "")
            gender = onr.get("gender", "")
            tel = onr.get("tel", "")
            email = onr.get("email", "")
            uname = onr.get("uname", "")
            cid = onr.get("cid", "")
            ctype = onr.get("ctype", "")
            resource = onr.get("resource")

            if isinstance(resource,list):
                resource = list(map(lambda x: RESOURCE_REFL.get(x), resource))
            else:
                resource = RESOURCE_REFL.get(resource)
            if isinstance(ctype, list):
                ctype = list(map(lambda n: CTYPE_REFLECT.get(n, ""), ctype))
            else:
                ctype = CTYPE_REFLECT.get(ctype, "")
            row = [name, addr, birthday, gender, tel, email, uname, cid, ctype,resource]
            _row = []
            for i in row:
                if isinstance(i, list):
                    i = map(lambda x: str(x), i)
                    e = "\n".join(i)
                    _row.append(e)
                else:
                    _row.append(str(i))
            data_list.append(_row)

        return data_list
