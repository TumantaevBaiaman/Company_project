from django.contrib import admin
from django.urls import path, include
from .views import (
    PostListView,
    CategoryListView,
    InfoDetailView,
    CategoryDetailView,
    show_category,
    index, InfoCreateView,
    InfoUpdateView, InfoDeleteView,
    LicensesCreateView, LicensesDetailView,
    FormaCreateView, FormaDetailView,
    CategoryCreateView,
)


urlpatterns = [
    path('', index, name='home'),
    path('category/', CategoryListView.as_view(), name='company'),
    path('info/<int:pk>/', InfoDetailView.as_view(), name='detail'),
    path('category/<int:cat_id>/', show_category, name='category'),
    path('licenses/<int:pk>/', LicensesDetailView.as_view(), name='detail_l'),
    path('forma/<int:pk>/', FormaDetailView.as_view(), name='detail_f'),
    path('info/new/', InfoCreateView.as_view(), name='create'),
    path('licenses/new/', LicensesCreateView.as_view(), name='create_l'),
    path('forma/new/', FormaCreateView.as_view(), name='create_f'),
    path('info/<int:pk>/update/', InfoUpdateView.as_view(), name='update'),
    path('info/<int:pk>/delete/', InfoDeleteView.as_view(), name='delete'),
    path('category/new/', CategoryCreateView.as_view(), name='create_cat'),
]
