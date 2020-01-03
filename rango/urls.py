"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rango import views
from rango.views import AboutView


app_name = 'rango'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('category/<slug:category_name_slug>/', views.ShowCategoryView.as_view(), name='show_category'),
    path('category/<category_name_slug>/add_page/', views.AddPageView.as_view(), name='add_page'),
    path('restricted/', views.RestrictedView.as_view(), name='restricted'),
    path('goto/', views.GotoView.as_view(), name='goto'),
    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('suggest/', views.CategorySuggestionView.as_view(), name='suggest'),
    path('search_add_page/', views.SearchAddPageView.as_view(), name='search_add_page'),
    # path('profile/', views.profile, name='profile'),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),
    # path('search/', views.search, name='search'),
]


