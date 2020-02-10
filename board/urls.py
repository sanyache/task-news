from django.views.generic import TemplateView
from django.urls import path
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/reply/create', ReplyCreate.as_view(), name='reply-create'),
    path('post/create', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>', PostDetail.as_view(), name='post-detail'),


]