from django.conf.urls import url
from BRMApp import views

urlpatterns=[
    url('view-books',views.viewBooks),
    url('edit-books',views.editBooks),
    url('delete-books',views.deleteBooks),
    url('search-books',views.searchBooks),
    url('new-books',views.newBooks),
    url(r'^add',views.add),
    url('search',views.search),
    url('edit',views.edit),
    url('login',views.userLogin),
    url('logout',views.userLogout),
]
