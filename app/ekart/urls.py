from django.conf.urls import url, include
from . import views

app_name = 'ekart'

urlpatterns =[

    # /ekart/
    url(r'^$', views.index, name='index'),
    # /ekart/21/
    url(r'^(?P<food_id>\d+)/$', views.details, name='details'),
    # ekart/21/favourite_food/
    url(r'^(?P<food_id>\d+)/favourite_food/$', views.favourite_food, name='favourite_food'),
    # # /ekart/21/favourite_song/
    # url(r'^(?P<food_id>\d+)/favourite_song/(?P<song_id>\d+)/$', views.favourite_song, name='favourite_song'),
    # /ekart/food/create/
    url(r'^food/create/$', views.add_food, name='add_food'),
    # # /ekart/21/add_song/
    # url(r'^(?P<food_id>\d+)/add_song/$', views.add_song, name='add_song'),
    # /ekart/21/update_food/
    url(r'(?P<food_id>\d+)/update_food/$', views.update_food, name='update_food'),
    # # /ekart/21/update_song/1/
    # url(r'(?P<food_id>\d+)/update_song/(?P<song_id>\d+)/$', views.update_song, name='update_song'),
    # /ekart/21/delete_food/
    url(r'(?P<food_id>\d+)/delete_food/', views.delete_food, name='delete_food'),
    # # /ekart/21/delete_song/1/
    # url(r'^(?P<food_id>\d+)/delete_song/(?P<song_id>\d+)/$', views.delete_song, name='delete_song'),
    # /ekart/register/
    url(r'^register/$', views.register, name='register'),
    # /ekart/user_login/
    url(r'^user_login/$', views.user_login, name='user_login'),
    # /ekart/user_logout/
    url(r'^user_logout/$', views.user_logout, name='user_logout'),
    # /ekart/login_page/
    url(r'^login_page/$', views.login_page, name='login_page'),
    # # /ekart/all_songs/
    # url(r'^all_songs/$', views.all_songs, name='all_songs'),

]
