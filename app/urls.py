from unicodedata import name
from django.urls import path
from .views import HomepageView, create, read, update, delete, SearchResultsView
urlpatterns = [
    # path('admin/' , name = 'admin'),
    path('new/', create, name='create'),
    path('', read, name='read'),
    path('<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    # path('search/',search , name='search'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('home/',HomepageView.as_view(), name='home'),
]