from django.urls import path

from webapp.views import cat_view, create_name

urlpatterns = [
    path('add-name/', cat_view),
    path('', create_name)
]

