from django.conf.urls import url, include
from . import views

app_name = 'ekart'

urlpatterns =[

    # /ekart/
    url(r'^$', views.index, name='index'),
    # /ekart/21/
    url(r'^(?P<food_id>\d+)/$', views.details, name='details'),
    # /ekart/register/
    url(r'^register/$', views.register, name='register'),
    # /ekart/user_login/
    url(r'^user_login/$', views.user_login, name='user_login'),
    # /ekart/user_logout/
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    # /ekart/login_page/
    url(r'^login_page/$', views.login_page, name='login_page'),
    url(r'^cyclone/add_cyclone_image/$', views.add_cyclone_image, name='add_cyclone_image'),


]
