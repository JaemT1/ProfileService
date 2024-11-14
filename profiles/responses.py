# perfiles/responses.py
from django.http import JsonResponse

class ApiError(JsonResponse):
    def __init__(self, status, error, message, path, **kwargs):
        data = {
            "status": status,
            "error": error,
            "message": message,
            "path": path
        }
        super().__init__(data, status=status, **kwargs)


class ApiSuccess(JsonResponse):
    def __init__(self, status, success, message, path, **kwargs):
        data = {
            "status": status,
            "success": success,
            "message": message,
            "path": path
        }
        super().__init__(data, status=status, **kwargs)

