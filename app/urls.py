# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .popups import *
# from .views  import *
from .views import *



urlpatterns = [
    # Matches any html file 
    re_path(r'^.*\.html', pages, name='pages'),

    # The home page
    path('', Home, name='home'),
    # path('category/', CategoryDetail, name='category-list'),
    # path('category/<int:id>/', CatsDetail, name='cats-detail'),
    path('notes/', Notes, name='notes'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path("category/<str:pk_test>/", CategoryView, name='category-detail'),
    path('notes/<int:pk>/update/', UpdateNote.as_view(), name='note-update'),
    path('notes/new_note/', NewNote.as_view(), name='new_note'),
    path('notes/add_category/', AddCategory.as_view(), name='add_category'),
    path('panel/', panel, name='panel')
    # path('category/<int:category_id>/', ContentByCategory.as_view(), 
        # name='category-detail'),
    # path('category/', CategoryList.as_view(), name='category'),
]
