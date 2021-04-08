import openpyxl
from api.lib.all_sql import AllDatabase
from api.lib.data.toxml import StoreToXML
from api.utils.xml import store_xml

FIELD_LIST = ["姓名", "地址", "出生日期", "性别", "电话", "邮箱", "用户名", "社交ID", "社交类型", "数据来源"]

class XmlPostHander(object):
    def __init__(self, file, select_field):
        self.wb = openpyxl.load_workbook(file)
        self.sheet = self.wb.active
        self.select_field = select_field

    def get_res(self):
        rows = self.sheet.iter_rows()
        al_data = []
        count = 0
        # 去掉标题行
        next(rows)
        for row in rows:
            count = count + 1
            print("当前查询条数：", count)
            try:
                adb = AllDatabase()
                for field, col_info in self.select_field.items():
                    if col_info.get("isChecked") and col_info.get("col"):
                        col = col_info["col"]
                    else:
                        continue
                    col_val = str(row[col].value)
                    if col_val:
                        res = adb.find({"val": col_val, "type": field})
                        if res["errno"] == 0:
                            stx = StoreToXML(res["data"]["all_data"])
                            data_list = stx.paser_content()
                            al_data.extend(data_list)
                print("共得到{count}条结果".format(count=len(al_data)))
            except Exception as e:
                msg = "查询第{count}条时出现错误:{e}".format(count=count, e=e)
                print(msg)
                al_data.append([msg])
        url = store_xml(al_data, FIELD_LIST, "ALL_INFO")
        return url



