from django.http import JsonResponse

class JsonErrorResponse(JsonResponse):
    def __init__(self, errno, msg):
        data = {
            "errno": errno,
            "msg": msg
        }
        super().__init__(data=data)
