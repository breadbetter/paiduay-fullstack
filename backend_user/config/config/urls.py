"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
from django.conf.urls import url
# router = routers.DefaultRouter()
# router.register(r'api/v1', views.UserViewSet)
# router.register(r'api/v1/id', views.UserId)
# router.register(r'api/v1/firstname', views.UserFirstname)
# router.register(r'api/v1/lastname', views.UserLastname)
# router.register(r'api/v1/email', views.UserEmail)
# router.register(r'api/v1/gender', views.UserGender)
# router.register(r'api/v1/age', views.UserAge)
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('<str:id>/', include(router.urls)),
    # path('<str:first_name>/', include(router.urls)),
    # path('<str:last_name>/', include(router.urls)),
    # path('<str:email>/', include(router.urls)),
    # path('<str:gender>/', include(router.urls)),
    # path('<str:age>/', include(router.urls)),
    path('api/v1/', views.UserViewSet.as_view()),
    path('api/v1/age/<int:age>', views.UserId.as_view()),
    # path('api/v1/id/<int:pk>', views.UserDetail.as_view())

]
