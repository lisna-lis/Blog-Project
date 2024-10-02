from django.db import models
import uuid
from ckeditor.fields import RichTextField
from users.models import Profile



# Create your models here.

class BaseClass(models.Model):
    uuid = models.SlugField(default=uuid.uuid4, unique=True)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
     abstract=True

class Tags(BaseClass):
   tag_name = models.CharField(max_length=200)

   def  __str__(self):
        return self.tag_name

   class Meta:
        ordering = ['-id']
        verbose_name =  'Tags'
        verbose_name_plural = 'Tags'

class Blog(BaseClass):
   user = models.ForeignKey(Profile,on_delete=models.CASCADE)
   title = models.CharField(max_length=100)
   content = RichTextField()
   tags = models.ManyToManyField(Tags,blank=True,null=True)

   def  __str__(self):
        return f'{self.user} -{ self.title}'

   class Meta:
        ordering = ['-id']
        verbose_name =  'Blog'
        verbose_name_plural = 'Blogs'  
   
