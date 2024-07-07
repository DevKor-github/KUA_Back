from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class PointGetView(APIView):  # 포인트 값과 user를 받아 해당 포인트 값만큼 유저가 포인트를 얻는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    point_reward = {
        'answer': 5,
        'chosen': 20,
        'survey': 10
    }

    def post(self, request):
        user = request.user
        point_type = request.data['point_type']
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        reward = self.point_reward.get(point_type)

        if reward:
            student.points += reward
            student.save()
            return Response(f"Get {reward} Points")

        else:
            return Response({'error': ' invalid getting points type'})


class PointUseView(APIView):  # 포인트를 이용하여 이용권을 구매하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    point_costs = {
        '1': 80,
        '7': 160,
        '14': 240,
        '30': 300
    }

    def post(self, request):
        user = request.user
        point_type = request.data['point_type']
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        cost = self.point_costs.get(point_type)

        if cost:
            if student.points < cost:
                return Response('Not Enough Points')
            student.points -= cost
            student.permission_date = timezone.now()
            student.permission_type = '1'
            student.save()
            return Response(f"Get {point_type} day permission")

        else:
            return Response({'error': ' invalid using points type'})
