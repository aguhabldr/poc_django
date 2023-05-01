from django.shortcuts import render
from django.contrib.auth import get_user_model
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

    @action(detail=True,methods=['get'])
    def projects(self,request,pk=None):   
        try:                
            project=Project.objects.get(pk=pk)
            return Response(project.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })


class CategoryViewSet(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset= Comment.objects.all()
    serializer_class=CommentSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     UserModel View.
#     """
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer
#     queryset = get_user_model().objects.all()


