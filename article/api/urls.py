from django.urls import path , include 
from .view import(
ListView,DetailView,
DetailView,  CreateView, 
UpdateView ,DestroyView,
FacebookLogin)


urlpatterns = [ 
	path('',ListView.as_view()),
    path('<pk>/',DetailView.as_view()),
    path('app/create/',CreateView.as_view()),
    path('<pk>/update/',UpdateView.as_view()),
    path('<pk>/delete/',DestroyView.as_view()),
    path('rest-auth/facebook/',FacebookLogin.as_view(), name='fb_login')

]