from django.urls import path
from . import views


urlpatterns = [
    path('create/',views.CreatePost.as_view(),name='createpost'),
    path('profileEdit/<int:pk>/',views.profileEdit.as_view(),name='profileEdit'),
    path('newsfeed/', views.Posts_following, name='newsfeed'),
    path('follow_and_unfollow/', views.follow_and_unfollow, name='back'),
    path('mayknow/', views.ProfileListView.as_view(), name='mayknow'),
    path('<int:pk>', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('Trending/', views.Trending, name='trending'),
    path('popular/', views.Popular, name='popular'),
    path('search/', views.search, name='search'),




]
