import openpyxl


def get_title(path):
    xt = XmlTitle(path)
    return xt.get_title()


col_keyword = {
    "name": ["姓名","name","名字"],
    "uname": ["用户", "作者", "昵称","nickname","uname"],
    "tel": ["机", "电话","tel"],
    "email": ["邮","mail","@"],
    "cid": ["ID", "id"],
    "gid": ["群id", "群ID","gid"]
}


class XmlTitle():
    def __init__(self, path):
        self.wb = openpyxl.load_workbook(path)
        self.ws = self.wb.active

    def get_title(self):
        rows = self.ws.iter_rows()
        title_row = next(rows)
        title_dict = {
            "name": {
                "isChecked": False,
                "col": None
            },
            "uname": {
                "isChecked": False,
                "col": None
            },
            "tel": {
                "isChecked": False,
                "col": None
            },
            "email": {
                "isChecked": False,
                "col": None
            },
            "cid": {
                "isChecked": False,
                "col": None
            },
            "gid": {
                "isChecked": False,
                "col": None
            },
        }
        all_title = []
        for i in range(len(title_row)):
            title_name = title_row[i].value
            if title_name:
                all_title.append({
                    "title": str(title_name),
                    "col": i
                })
            title = self._judge_title(title_name)
            if title:
                title_dict[title]["isChecked"] = True
                title_dict[title]["col"] = i
        res = {
            "selectInfo": title_dict,
            "allCol": all_title
        }
        return res

    def _judge_title(self, title):
        if not title or not isinstance(title, str):
            return None
        for field, key_list in col_keyword.items():
            for k in key_list:
                if k in title:
                    return field
        return None


if __name__ == '__main__':
    xt = get_title("3000.xlsx")
    print(xt)
