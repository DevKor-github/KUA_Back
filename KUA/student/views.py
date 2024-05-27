from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
    
class PointGetView(APIView): #포인트 값과 user를 받아 해당 포인트 값만큼 유저가 포인트를 얻는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        point_type = request.data['point_type']
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        if point_type == 'answer':
            student.points += 5
            student.save()
            return Response("Get 5 Points")
        elif point_type == 'chosen':
            student.points += 20
            student.save()
            return Response("Get 20 Points")
        elif point_type == 'survey':
            student.points += 10
            student.save()
            return Response("Get 10 Points")
        else:
            return Response({'error': ' invalid getting points type'})
    
class PointUseView(APIView): #포인트를 이용하여 이용권을 구매하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    
    def post(self, request):
        user = request.user
        point_type = request.data['point_type']
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status = 400)
        
        if point_type == '1':
            if student.points <80:
                return Response('Not enough points')
            student.points -= 80
            student.permission_date = timezone.now()
            student.permission_type = '1'
            student.save()
            return Response("Get 1 day permission")
        
        elif point_type == '7':
            if student.points <160:
                return Response('Not enough points')
            student.points -= 160
            student.permission_date = timezone.now()
            student.permission_type = '7'
            student.save()
            return Response("Get 7 day permission")
        
        elif point_type == '14':
            if student.points <240:
                return Response('Not enough points')
            student.points -= 240
            student.permission_date = timezone.now()
            student.permission_type = '14'
            student.save()
            return Response("Get 14 day permission")
        
        elif point_type == '30':
            if student.points <300:
                return Response('Not enough points')
            student.points -= 300
            student.permission_date = timezone.now()
            student.permission_type = '30'
            student.save()
            return Response("Get 30 day permission")
        
        else:
            return Response({'error': ' invalid using points type'})

