"""
URL configuration for backend_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

    http post http://127.0.0.1:8000/api/token/ username=admin password=root

    http http://127.0.0.1:8000/api/vendors/ "Authorization Bearer: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkwNjI4NDA4LCJpYXQiOjE2OTA2MjgxMDgsImp0aSI6IjY0NmM0NTc3MTkyZDQ2NThhZDg0ZTllMTNmZWMxNTM1IiwidXNlcl9pZCI6MX0.L69BD1KHU5OZmses-2axrkDGklUi7xitS0tsD22u_2g"

"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt import views as views_jwt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/token/',views_jwt.TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/', views_jwt.TokenRefreshView.as_view(),name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),

]
