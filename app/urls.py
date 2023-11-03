from rest_framework import routers
from .views import ImageViewset,CategoryViewset,LikeViewset
from django.urls import path,include
from app.views import RegisterView

router = routers.DefaultRouter()
router.register(r'images', ImageViewset)
router.register(r'category', CategoryViewset)
router.register(r'like', LikeViewset)


urlpatterns = [
    path("register/", RegisterView.as_view(), name="auth_register"),    # Other URL patterns
]

# Include the router's URLs in your project's urlpatterns
urlpatterns += router.urls
