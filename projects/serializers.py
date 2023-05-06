from rest_framework import serializers
from .models import Project, Comment, Category



#create serializers here


class CategorySerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Category
        #fields=['id','name']
        fields='__all__'

class ProjectSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    # commentsby=CommentSerializer(many=True, read_only=True)
    #categories=CategorySerializer(many=False, read_only=True)
    class Meta:
        model=Project
        #fields=['id','title','description','categories','created_at','updated_at']
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Comment
        fields='__all__'

    
            


