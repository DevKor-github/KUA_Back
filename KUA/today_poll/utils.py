from django.http import JsonResponse
from .utils import get_class_time

def class_time_view(request, period_number):
    time = get_class_time(period_number)
    return JsonResponse({"period_number": period_number, "time": time})