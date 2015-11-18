from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^\d*$', views.result_for_page),
    url(r'^upload$', views.upload_image),
    url(r'^upload_result$', views.result_for_upload),
    url(r'^detail_\w*$', views.detail),
    url(r'^both_\d*$', views.result_both),
    url(r'^bfs_\d*$', views.result_bfs),
    url(r'^default_\d*$', views.result_default),
]