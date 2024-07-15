from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
        
class SubmitTimeTableView(generics.CreateAPIView): #id, 학수번호, 개설년도와 학기 정보를 통해 시간표를 등록하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        print(user.username)
        course_id = request.data['course_id']
        year = request.data['year']
        semester = request.data['semester']
        timetable = {
            'username': user.username,
            'course_id': course_id,
            'year': year,
            'semester': semester
        }
        serializer = serializers.TimeTableSerializer(data = timetable)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'Time Table Saved'})
        return Response({'response': 'Time Table Rejected'})
    


