from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.list ,name='list'),
    path('create/',views.create, name='create'),
    re_path('delete/(?P<delete_id>\w+)/$', views.delete, name='delete'),
    re_path('update/(?P<update_id>\w+)/$', views.update, name='update'),
    re_path('detail/(?P<detail_id>\w+)/$', views.detail, name='detail'),

]