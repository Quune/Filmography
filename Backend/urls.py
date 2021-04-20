from django.conf.urls import url
from Backend import views

urlpatterns = [
    url(r'^api/files$', views.file_list),
    url(r'^api/files/(?P<pk>[0-9]+)$', views.file_detail)
]
