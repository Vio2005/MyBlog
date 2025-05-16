from django.contrib import admin
from django.urls import path, include
from blogapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('blog/',blogdata,name='blog'),
    path('createblog/',createblog,name='createblog'),
    path('blogdetail/<int:id>/',blogdetail,name='blogdetail'),
    path('blogdelete/<int:id>/',blogdelete,name='blogdelete'),
    path('updateblog/<int:id>/',updateblog,name='updateblog'),


]
