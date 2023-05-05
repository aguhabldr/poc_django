from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique = True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Project(models.Model):
    ISACTIVE = (
        ("NEW","NEW"),
        ("ACTIVATED","ACTIVATED"),
        ("NOT_ACTIVATED","NOT_ACTIVATED"),
        ("DONE","DONE") 
    )

    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,unique = True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date =  models.DateTimeField(null=True)
    start_date =  models.DateTimeField(null=True)
    status = models.CharField(max_length=50, choices=ISACTIVE,  default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(User, on_delete=models.)

    def __str__(self):
        return self.title
    
        # def get_num_comments(self):
    #     # Get the count of comments associated with this project
    #     return Comment.objects.filter(project=self).count()

    # def get_absolute_url(self):
    #      # Return the URL to view this project's detail page
    #     return reverse('project_detail', args=[str(self.id)])

    # def get_comments(self):
    #     # Retrieve all comments associated with this project
    #     return Comment.objects.filter(project=self)

    # def get_num_comments(self):
    #     # Get the count of comments associated with this project
    #     return Comment.objects.filter(project=self).count()

class Comment(models.Model):
    id=models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.project.title}'
