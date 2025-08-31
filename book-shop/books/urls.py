from django.urls import path
from .views import BookListView , BookDetailView , BookTemplateView

urlpatterns = [
    path('book-list' , BookListView.as_view(), name ='book-list' ),
    path('book-detail/<int:pk>/' , BookDetailView.as_view(), name='book-detail'),
    path('' , BookTemplateView.as_view(), name= 'book-template'),
path("favicon.ico", lambda request: HttpResponse(status=204)),
] 
