from rest_framework.serializers import ModelSerializer
# Importing blog model
from .models import Blog
from .models import Tags
from rest_framework.serializers import CharField
from rest_framework.serializers import SerializerMethodField

class CKEditorField(CharField):
    def to_internal_value(self, value):
        # Custom logic to handle CKEditor data if needed
        return super().to_internal_value(value)

    def to_representation(self, value):
        # Custom logic to represent CKEditor data if needed
        return super().to_representation(value)

class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = ['id','uuid','tag_name']

class BlogSerializer(ModelSerializer):
    content = CKEditorField()
    tags = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Blog
        fields = ['uuid','title','user','content','tags']

    
    def get_tags(self,obj):
        tags = obj.tags.all()
        serializer = TagsSerializer(tags,many=True)
        return serializer.data
    
    def get_user(self,obj):
        return obj.user.email
