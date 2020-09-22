from django.urls import path
from searchengine.views import *

urlpatterns = [
    path('',Home.as_view(),name="home"),
    path('find',FindWorker.as_view(),name='find'),
    path('detail_proson/<int:pk>',DetailPorson.as_view(),name="detail_proson"),
    path('dashaboard',Dashaboard.as_view(),name="dashaboard"),
    path('addworker',AddWorker.as_view(),name="addworker"),
    path('aboutus',AboutUs.as_view(),name="aboutus"),
    path('add_category',AddCategory.as_view(),name = "add_category"),
    path('allworker',All_Workers.as_view(),name ="all_worker"),
    path('update/<int:pk>',UpdatePorson.as_view(),name="update_proson"),
    path('contact',Contact.as_view(),name = "contact"),
    path('profile',Profile.as_view(),name="profile"),
    path('updateprofile/<int:pk>/',UpdateProfile.as_view(),name="updateprofile"),
    path('login',Login.as_view(),name = 'login'),
    path('logout',Logout.as_view(),name = "logout"),
]


