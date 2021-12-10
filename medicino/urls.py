from django.conf.urls import url 

from medicino import views 

urlpatterns = [ 
    url(r'^medicino/$', views.customer_list),
    url(r'^medicino/(?P<pk>[0-9]+)$', views.customer_detail),
]