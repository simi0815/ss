# 此文件用于存放查询某数据库时需要使用的钩子函数,主要用于查询前后的数据清洗工作
import api.middleware.tel as tel_util
from api.lib.name.parse_name import handle_name


# pdl_coll
def before_lingying_db_pdl_coll_tel(con):
    s_c_tel = tel_util.strfy_add_crossing(con.get("val"))
    s_con = [
        {"tel": con.get("val")},
        {"tel": s_c_tel},
    ]
    return s_con
def after_lingying_db_pdl_coll(res):
    _res = []

    for one in res:
        _one = one.copy()
        if _one.get("tel"):
            _one["tel"] = list(map(lambda x:x.replace("-",""),_one["tel"]))
        _res.append(_one)
    return _res


# emailrecords
def before_verifications_db_emailrecords_tel(con):
    s_c_tel = tel_util.strfy_add_crossing(con.get("val"))
    s_con = [
        {"tel": s_c_tel},
    ]
    return s_con


# businessleads
def before_verifications_db_businessleads_tel(con):
    i_tel = tel_util.tel_to_int(con.get("val"))
    return [
        {
            "tel": i_tel
        }
    ]


# email_with_phone
def before_verifications_db_email_with_phone_tel(con):
    s_c_tel = tel_util.strfy_add_crossing(con.get("val"))
    i_tel = tel_util.tel_to_int(con.get("val"))
    return [
        {"tel": s_c_tel},
        {"tel": i_tel}
    ]


def before_verifications_db_email_with_phone_name(con):
    name = con.get("val")
    f_name, l_name = handle_name(name, format="upper")
    cap_con = {
        "first_name": f_name
    }
    if l_name:
        cap_con["last_name"] = l_name
    f_name, l_name = handle_name(name, format="lower")
    low_con = {
        "first_name": f_name
    }
    if l_name:
        low_con["last_name"] = l_name
    return [
        cap_con,
        low_con
    ]
def after_verifications_db_email_with_phone(res):
    _res = []
    for one in res:
        _one = one.copy()
        _one["tel"] = _one["tel"].replace("-","")
        _res.append(_one)
    return _res
# facebook 数据库
# aomen_tel
def before_facebook_db_aomen_tel_tel(con):
    tel = con.get("val")
    if not tel.startswith("853"):
        tel = "853" + con.get("val")
    i_tel = tel_util.tel_to_int(tel)
    return [
        {
            "tel": i_tel
        }
    ]


def before_facebook_db_aomen_tel_cid(con):
    # cid是数字,不走查询通道
    try:
        cid = int(con.get("val"))
    except Exception:
        return []
    return [
        {
            "cid": "https://www.facebook.com/profile.php?id={cid}".format(cid=cid)
        }
    ]


def after_facebook_db_aomen_tel(res):
    _res = []
    for onr in res:
        _onr = onr.copy()
        if onr.get("cid"):
            cid = onr.get("cid").split("=")[-1]
            _onr["cid"] = cid
        _res.append(_onr)
    return _res


# china_tel
def before_facebook_db_china_tel_tel(con):
    tel = con.get("val")
    if not tel.startswith("853"):
        tel = "853" + con.get("val")
    i_tel = tel_util.tel_to_int(tel)
    return [
        {
            "tel": i_tel
        }
    ]


def before_facebook_db_china_tel_cid(con):
    return before_facebook_db_aomen_tel_cid(con)


def after_facebook_db_china_tel(res):
    return after_facebook_db_aomen_tel(res)


# hongkong_tel
def before_facebook_db_hongkong_tel_tel(con):
    tel = con.get("val")
    if not tel.startswith("8532"):
        tel = "852" + con.get("val")
    i_tel = tel_util.tel_to_int(tel)
    return [
        {
            "tel": i_tel
        }
    ]


def before_facebook_db_hongkong_tel_cid(con):
    return before_facebook_db_aomen_tel_cid(con)


def after_facebook_db_hongkong_tel(res):
    return after_facebook_db_aomen_tel(res)


# taiwan_tel
def before_facebook_db_taiwan_tel_tel(con):
    tel = con.get("val")
    if not tel.startswith("886"):
        tel = "886" + con.get("val")
    i_tel = tel_util.tel_to_int(tel)
    return [
        {
            "tel": i_tel
        }
    ]


def before_facebook_db_taiwan_tel_cid(con):
    return before_facebook_db_aomen_tel_cid(con)


def after_facebook_db_taiwan_tel(res):
    return after_facebook_db_aomen_tel(res)


# manycountries_tel
def before_facebook_db_manycountries_tel_cid(con):
    return [
        {
            "cid": "https://www.facebook.com/{cid}".format(cid=con.get("val"))
        }
    ]


def before_facebook_db_manycountries_tel_tel(con):
    tel = con.get("val")
    i_tel = tel_util.tel_to_int(tel)
    return [
        {
            "tel": i_tel
        }
    ]


def after_facebook_db_manycountries_tel(res):
    _res = []
    for onr in res:
        _onr = onr.copy()
        if onr.get("cid"):
            cid = onr.get("cid").split("/")[-1]
            _onr["cid"] = cid
        _res.append(_onr)
    return _res


# id_email_02
def before_facebook_db_id_email_02_cid(con):
    cid = con.get("val")
    try:
        cid = int(cid)
    except Exception:
        return [
            {"uname": cid}
        ]
    return [
        {"cid": cid}
    ]


# id_tel_02
def before_facebook_db_id_tel_02_cid(con):
    cid = con.get("val")
    try:
        cid = int(cid)
    except Exception:
        return [{
            "cid": "facebook.com/{cid}".format(cid=cid)
        }]
    else:
        return []


def before_facebook_db_id_tel_02_name(con):
    name = con.get("val")
    return [
        {"name": name.capitalize()}
    ]


def after_facebook_db_id_tel_02_tel(res):
    return after_facebook_db_manycountries_tel(res)


# id_tel_email

def before_facebook_db_id_tel_email_tel(con):
    return before_verifications_db_businessleads_tel(con)


def before_facebook_db_id_tel_email_cid(con):
    cid = con.get("val")
    try:
        cid = int(cid)
    except Exception:
        return [{
            "cid": "https://www.facebook.com/{cid}".format(cid=cid)
        }]
    else:
        return []


def after_facebook_db_id_tel_email(res):
    return after_facebook_db_manycountries_tel(res)


# id_tel_name_email_01
def before_facebook_db_id_tel_name_email_01_tel(con):
    return before_verifications_db_businessleads_tel(con)


def before_facebook_db_id_tel_name_email_01_cid(con):
    cid = con.get("val")
    try:
        cid = int(cid)
    except Exception:
        return []
    else:
        return [
            {"cid": cid}
        ]


# younow-db.fb_twitter_id_name_email
def before_younow_db_fb_twitter_id_name_email_cid(con):
    return before_facebook_db_id_tel_name_email_01_cid(con)


# qq-db.id_tel
def before_qq_db_id_tel_tel(con):
    return before_verifications_db_businessleads_tel(con)


def before_qq_db_id_tel_cid(con):
    return before_facebook_db_id_tel_name_email_01_cid(con)


if __name__ == '__main__':
    print(before_lingying_db_pdl_coll_tel({"type": "tel", "val": "13219316112"}))
