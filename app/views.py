from django.db.models import F
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly ,IsAdminUser


from .models import *
from .serializers import *
from rest_framework import generics
from .serializers import RegisterSerializer 
from rest_framework.permissions import AllowAny 

class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
#perform is a method of viewset which is overriding its method
    def perform_create(self, serializer):
        # Get the user from the request
        user = self.request.user

        # Get the category from the request data
        category_id = self.request.data.get('category')

        serializer.validated_data['user'] = user
        serializer.validated_data['category_id'] = category_id

        # Save the image with the user and category information
        serializer.save()


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]



class LikeViewset(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def perform_create(self, serializer):
        user = self.request.user
        image_id = self.request.data.get('image')
#first : get alternate ,if query does not exist return blank
        like = Like.objects.filter(user=user, image_id=image_id).first() 
        img = Image.objects.get(id=image_id)  # Assuming you want to update the like_count on the Image model

        if like:
            # If a Like instance already exists, update its 'liked' field
            like.liked = not like.liked
            img.like_count = F('like_count') + 1 if like.liked else F('like_count') - 1
            like.save()

        else:
            # If the Like instance doesn't exist, create a new one with 'liked' set to True
            serializer.validated_data['user'] = user
            serializer.validated_data['image_id'] = image_id
            serializer.save()
            img.like_count = F('like_count') + 1

        img.save()

# user registraion
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

