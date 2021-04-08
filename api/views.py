from django.views import View
from django.http import HttpResponse, JsonResponse
from api.lib.data.toxml import StoreToXML
from api.lib.all_sql import AllDatabase
from api.lib.search_file import XmlPostHander
from api.lib.jsone import JSONEncoder
from api.lib.searchpost import SearchPost as SP
from api.conf.api_config import STATIC_ROOT
from api.lib.data.xml_title import get_title
from api.lib.response import JsonErrorResponse
import json
import os
import time


class InfoList(View):
    def get(self, request, version, *args, **kwargs):
        adb = AllDatabase()
        res = adb.find_deepth(request.GET)
        json_res = json.dumps(res, cls=JSONEncoder)
        response = HttpResponse(json_res)
        response['content-type'] = 'application/json'
        return response


class TOXML(View):
    def post(self, request, version, *args, **kwargs):
        info = request.body.decode("utf8")
        info = json.loads(info)
        info = info["infoList"]
        stx = StoreToXML(info)
        url = stx.paser_xml()
        return JsonResponse({
            "errno": 0,
            "url": url
        })


class CheckFile(View):
    def post(self, requests, version, *args, **kwargs):
        file = requests.FILES.get('file')
        print("已接收到文件：", file)
        if file:
            if file.name.split(".")[-1] != 'xlsx':
                return JsonErrorResponse(1, "文件格式暂不识别,暂只支持.xlsx格式")
            path_dir = os.path.join(STATIC_ROOT, "upload")
            if not os.path.exists(path_dir):
                os.makedirs(path_dir, exist_ok=True)
            file_name = str(time.time_ns()) + file.name
            path = os.path.join(path_dir, file_name)
            destination = open(path, 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
            title_info = get_title(path)
            if not title_info["allCol"]:
                return JsonErrorResponse(2, "未读取到有效行标题，请查看文件第一行")
            return JsonResponse({
                "errno": 0,
                "title_info": title_info,
                "file_name": file_name
            })
        else:
            return JsonErrorResponse(5, "未得到文件")


class SearchByFile(View):
    def post(self, request, version, *args, **kwargs):
        info = request.body.decode("utf8")
        file_info = json.loads(info)
        if not file_info:
            return JsonErrorResponse(1, "没有接收到文件信息")
        file_name = file_info.get("file_name")
        select_col = file_info.get("select_col")
        if not file_name or not select_col:
            return JsonErrorResponse(2,"接受到数据缺乏有效字段")
        path = os.path.join(STATIC_ROOT,"upload",file_name)
        if not os.path.exists(path):
            return JsonErrorResponse(3,"未找到文件")
        xph = XmlPostHander(path,select_col)
        url = xph.get_res()
        print(url)
        return JsonResponse({
            "errno": 0,
            "url": url
        })


class SearchPost(View):
    def get(self, requests, version, *args, **kwargs):
        cid = requests.GET.get("cid")
        ctype = requests.GET.get("ctype")
        if not cid or not ctype:
            return JsonErrorResponse(1, "没有接受到有效数据")
        sp = SP(cid=cid, ctype=ctype)
        res = sp.search()
        if not res:
            return JsonErrorResponse(2, "未查询到结果")
        else:
            bac = {
                "errno": 0,
                "data": res
            }
            return JsonResponse(bac)
