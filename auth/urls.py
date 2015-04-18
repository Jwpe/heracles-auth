from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import UserViewSet

urlpatterns = [
    url(r'^tokens/auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^tokens/verify/', 'rest_framework_jwt.views.verify_jwt_token'),
]

router = DefaultRouter()
router.register(prefix='users', viewset=UserViewSet)

urlpatterns += router.urls
