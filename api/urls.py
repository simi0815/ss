from django.urls import re_path
from api.views import InfoList, TOXML, SearchByFile, SearchPost, CheckFile,FileStatus

urlpatterns = [
    re_path(r'^(?P<version>[v1|v2]+)/infolist$', InfoList.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/toxml$', TOXML.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/checkfile$', CheckFile.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/searchbyfile$', SearchByFile.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/filestatus$', FileStatus.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/searchpost$', SearchPost.as_view()),

]
