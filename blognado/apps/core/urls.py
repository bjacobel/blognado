from django.conf.urls import url
from blognado.apps.core import views

urlpatterns = [
    url(r'^$', views.BlogListView, name="bloglist"),
    url(r'^liveblog/(?P<id>\d+)/', views.BlogDetailView, name="blogdetail"),
    url(r'^liveblog/(?P<slug>.+)/', views.BlogDetailView, name="blogdetail"),
]