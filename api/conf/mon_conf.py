MON_DB_REFL = {
    "lingying-db.pdl-coll": {
        "field_refl": {
            "name": "name",
            "email": "email",
            "tel": "tel",
            "cid": "liid",
            "location": "addr"
        },
        "ctype": "ly",
        "resource": 2
    },
    "verifications-db.emailrecords": {
        "field_refl": {
            "first_name":"first_name",
            "last_name":"last_name",
            "tel": "tel",
            "email": "email",
            "location": "city",
        },
        "resource": 8
    },
    "verifications-db.businessleads": {
        "field_refl": {
            "email": "email",
            "tel": "tel",
            "first_name": "first_name",
            "last_name": "last_name",
            "location": "city"
        },
        "resource": 8

    },
    "verifications-db.email_with_phone": {
        "field_refl": {
            "email": "email",
            "first_name": "first_name",
            "last_name": "last_name",
            "tel": "tel",
            "location": "city"
        },
        "resource": 8

    },
    "facebook-db.aomen_tel": {
        "field_refl": {
            "tel": "MOBILE",
            "email": "EMAIL",
            "cid": "FACEBOOK PROFILE",
            "first_name": "FNAME",
            "last_name": "LNAME",
            "gender": "GENDER",
            "location": "LOCATION1",
            "birthday": "DOB"
        },
        "ctype": "facebook",
        "resource": 1
    }
    , "facebook-db.china_tel": {
        "field_refl": {
            "tel": "MOBILE",
            "email": "EMAIL",
            "cid": "FACEBOOK PROFILE",
            "first_name": "FNAME",
            "last_name": "LNAME",
            "gender": "GENDER",
            "location": "LOCATION1",
            "birthday": "DOB"
        },
        "ctype": "facebook",
        "resource": 1

    }
    , "facebook-db.hongkong_tel": {
        "field_refl": {
            "tel": "MOBILE",
            "email": "EMAIL",
            "cid": "FACEBOOK PROFILE",
            "first_name": "FNAME",
            "last_name": "LNAME",
            "gender": "GENDER",
            "location": "LOCATION1",
            "birthday": "DOB"
        },
        "ctype": "facebook",
        "resource": 1
    }
    , "facebook-db.taiwan_tel": {
        "field_refl": {
            "tel": "MOBILE",
            "email": "EMAIL",
            "cid": "FACEBOOK PROFILE",
            "first_name": "FNAME",
            "last_name": "LNAME",
            "gender": "GENDER",
            "location": "LOCATION_01",
            "birthday": "DOB"
        },
        "ctype": "facebook",
        "resource": 1

    }
    # , "facebook-db.vietnam_tel": {
    #     "cid": "_source.facebook_id",
    #     "tel": "_source.phone_number",
    #     "uname": "_source.username",
    #     "name": "_source.fullname",
    #     "email": "_source.email",
    #     "gender": "_source.gender",
    #     "birthday": "_source.birthday",
    #     "location": "_source.hometown_location"
    # }
    , "facebook-db.manycountries_tel": {
        "field_refl": {
            "cid": "FACEBOOK ID",
            "tel": "PHONE",
            "first_name": "FNAME",
            "last_name": "LNAME",
            "email": "EMAIL",
            "birthday": "AGE"
        },
        "ctype": "facebook",
        "resource": 1

    }
    # , "facebook-db.id_email_01": {
    #     "cid": "FBUserId.S",
    #     "uname": "UserName.S",
    #     "email": "Email.S",
    #     "name": "Name.S"
    # }
    , "facebook-db.id_email_02": {
        "field_refl": {
            "cid": "fb_id",
            "uname": "fb_user",
            "first_name": "first",
            "last_name": "last",
            "email": "email",
            "gender": "gender",
            "location": "hometown"
        },
        "ctype": "facebook",
        "resource": 1
    }
    # , "facebook-db.id_tel_01": {
    #     "cid": "_source.facebook_id",
    #     "tel": "_source.phone_number",
    #     "email": "_source.email",
    #     "uname": "_source.username",
    #     "name": "_source.fullname",
    #     "gender": "_source.gender",
    #     "birthday": "_source.birthday",
    #     "location": "_source.hometown_location"
    # }
    , "facebook-db.id_tel_02": {
        "field_refl": {
            "cid": "profile",
            "tel": "tel",
            "name": "name",
            "email": "email",
            "location": "hometown",
            "birthday": "birthday"
        },
        "ctype": "facebook",
        "resource": 1

    }
    , "facebook-db.id_tel_email": {
        "field_refl": {
            "cid": "FACEBOOK ID",
            "first_name": "FNAME",
            "last_name": "LNAME",
            "tel": "PHONE",
            "email": "EMAIL",
            "birthday": "AGE"
        },
        "ctype": "facebook",
        "resource": 1

    }
    , "facebook-db.id_tel_name_email_01": {
        "field_refl": {
            "tel": "phone",
            "cid": "uid",
            "first_name": "first_name",
            "last_name": "last_name",
            "location": "hometown",
            "gender": "gender",
            "email": "email",
            "birthday": "birthday"
        },
        "ctype": "facebook",
        "resource": 1

    },
    # ******
    "facebook-db.id_tel_name_email_02": {
        "field_refl": {
            "tel": "tel",
            "cid": "uid",
            # "first_name": "first_name",
            # "last_name": "last_name",
            "location": "hometown",
            "gender": "gender",
            "email": "email",
        },
        "ctype": "facebook",
        "resource": 1

    },

    "younow-db.fb_twitter_id_name_email": {
        "field_refl": {
            "cid": "facebook_id",
            "email": "facebook_email",
            # "first_name": "first_name",
            # "last_name": "last_name"
        },
        "ctype": "facebook",
        "resource": 1

    },
    # **************
    # , "facebook-db.email_pwd": {
    #     "email": "email",
    #     "pwd": "pwd"
    # }
    # ***********
    # , "twitter-db.email_pwd": {
    #     "email": "email",
    #     "pwd": "pwd"
    # },
    "facebook-db.id_uname_email": {
        "field_refl": {
            "cid": "uid",
            "uname": "uname",
            "location": "location1",
            "email": "email",
        },
        "ctype": "facebook",
        "resource": 1
    },
    # "eamil-db.email_pwd": {
    #     "field_refl": {
    #         "email":"email",
    #         "pwd":"pwd",
    #     },
    #     "ctype": "facebook",
    #     "resource": 1
    #
    # },
    "microblog-db.microblog_id_tel": {
        "field_refl": {
            "cid": "microblog_id",
            "tel": "tel"
        },
        "ctype": "weibo",
        "resource": 11
    },
    "qq-db.id_nickname_sex_age": {
        "field_refl": {
            "cid": "qq_id",
            "uname": "nickname",
            "gender": "sex",
            "location": "addr",
            "birthday": "age",
        },
        "ctype": "qq",
        "resource": 14
    },
    "qq-db.id_tel": {
        "field_refl": {
            "cid": "qq_id",
            "tel": "tel"
        },
        "ctype": "qq",
        "resource": 14
    },
}
