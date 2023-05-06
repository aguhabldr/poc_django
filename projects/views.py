from contextlib import nullcontext
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse

from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Project, Comment, Category

from .serializers import ProjectSerializer, CategorySerializer, CommentSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset= Project.objects.all()
    serializer_class=ProjectSerializer

    #projectss/{projectId}/comments
    @action(detail=True,methods=['get'])
    def comments(self,request,pk=None,ck=None): 
        try:
            print(f"Project id = {pk}")
            print(f"Comment id = {ck}")                          
            project=Project.objects.get(pk=pk)
            print(f"project = {project}")     
            comment=Comment.objects.filter(project=project)
            emps_serializer=CommentSerializer(comment,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Comment(s) might not exists !! Error'
            })
        


class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class=CommentSerializer

class ProjectCommentViewSet():
    @action(detail=True, methods=['get'])
    def getCommentsOnProject(self, pid, cid):       
       print(f"self = {self} ")
       print(f"Project id = {pid} ")
       print(f"Comments id = {cid} ")

       queryset = Comment.objects.filter(project=pid, id=cid).first()
       print({queryset})
       if queryset is None:
           return JsonResponse({'error':'Comment does not exists.'},
                                status=404,
                                safe=False)
       else:
            return Response({
                'message':'Comment(s) might not exists !! Error'
            })
       
      
       
       return JsonResponse(comment_serializer.data, safe=False)
     
       



