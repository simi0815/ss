ES_DB_REFL = {
    "telegram": {
        "index": "telegram_user*,tele_admin_*",
        "field_refl": {
            "uname": "username",
            "cid": "id",
            "gid": "gid",
            "tel": "phone",
            "last_name": "last_name",
            "first_name": "first_name",
        },
        "ctype": "telegram",
        "resource": 5
    },
    "facebook": {
        "index": "fb_user*",
        "field_refl": {
            # "name": "fullname",
            "uname": "fullname",
            "cid": "facebook_id",
            "tel": "phone_number",
            "email": "email",
            "birthday": "birthday",
            "gender": "gender",
            "location": "country",
        },
        "ctype": "facebook",
        "resource": 1
    },
    "twitter": {
        "index": "tw_user*",
        "field_refl": {
            "name": "name",
            "cid": "id",
            "uname": "username",
            "location": "location",

        },
        "ctype": "twitter",
        "resource": 3
    },
    "fbm": {
        "index": "fbm_user*",
        "field_refl": {
            "last_name": "last_name",
            "first_name": "first_name",
            "gender": "gender"
        },
        "ctype": "fbm",
        "resource": 6
    },
    "vx": {
        "index": "vx_user*",
        "field_refl": {
            "first_name": "first",
            "last_name": "last",
            "username": "username",
            "cid": "voxer_id"
        },
        "ctype": "vx",
        "resource": 7
    },
    "taiwan_office": {
        "index": "civil_servant_st-00001",
        "field_refl": {
            "name": "name",
            "birthday": "birthday",
            "tel": "phone"
        },
        "resource": 9
    },
    "white_house": {
        "index": "white_house_figures_sa",
        "field_refl": {
            "name": "name",
            "location": "position"
        },
        "resource": 10
    },
    "weibo_tel": {
        "index": "wb_phone*",
        "field_refl": {
            "tel": "phone",
            "cid": "id"
        },
        "ctype": "weibo",
        "resource": 11
    },
    "jinbo": {
        "index": "jinbo_*",
        "field_refl": {
            "name": "name",
            "location": "address"
        },
        "resource": 12
    },
    # 比特币中国用户
    "bit_china": {
        "index": "bitman_china_user"
    }
}
