from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^(\d+)$', views.show),
    #url(r'^(\d+)/edit/', views.edit),
    #url(r'^(\d+)/destroy/$', views.destroy),
    #url(r'^create', views.create),
    url(r'^checkout', views.checkout),
    url(r'^update', views.update),
    #url(r'^new', views.new), 
    url(r'^$', views.index)
]