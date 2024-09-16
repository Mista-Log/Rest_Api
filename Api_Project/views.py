from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from api_app.serializers import StudentsSerializer
from api_app.models import Students



class TestView(APIView):

    permission_classes = (IsAuthenticated, )


    def get(self, request, *args, **kwargs):
        qs = Students.objects.all()
        student1 = qs.first()
        serializer = StudentsSerializer(student1)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)



