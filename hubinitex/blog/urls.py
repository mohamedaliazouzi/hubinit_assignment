from django.urls import path
from .import views

urlpatterns = [
    path("", views.blog, name="blog"),
    path("blog/", views.blog, name="blog"),
    path("blog/add/", views.add, name="add"),
    path("blog/addrec/", views.addrec, name="addrec"),
    path("blog/delete/<int:id>/", views.delete, name="delete"),
    path("blog/update/<int:id>/", views.update, name="update"),
    path("blog/update/uprec/<int:id>/", views.uprec, name="uprec"),
    path("blog/search/", views.search, name="search"),
]
