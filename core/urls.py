"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from yelp.views.business import ListBusinessView, RetrieveBusinessView
from yelp.views.users import ListUsersView, RetrieveUsersView
from yelp.views.reviews import ListReviewsView, RetrieveReviewsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/business/', ListBusinessView.as_view()),
    path('retrieve/business/', RetrieveBusinessView.as_view()),
    path('list/users/', ListUsersView.as_view()),
    path('retrieve/users/', RetrieveUsersView.as_view()),
    path('list/reviews/', ListReviewsView.as_view()),
    path('retrieve/reviews/', RetrieveReviewsView.as_view()),
]
