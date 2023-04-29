from django.urls import path, include
# from .views import Project, Category, Comment
from rest_framework import routers


from projects.views import ProjectViewSet, CategoryViewSet, CommentViewSet

router= routers.DefaultRouter()

router.register('projects', ProjectViewSet, basename="projects")
router.register('categories', CategoryViewSet,  basename="categories")

# router.register('comments', CommentViewSet)


urlpatterns = [
    # ex: /projects/
    path('',include(router.urls))

    # path('api/', include('rest_framework.urls', namespace='rest_framework'))
    # path('', views.index),
 
]