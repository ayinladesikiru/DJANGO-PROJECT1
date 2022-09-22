from django.urls import path, include
from .views import index, redirect
from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

app_name = 'my_app'

router = SimpleRouter()
router.register('books', views.BookViewSet)

urlpatterns = [
    path('my_app', index, name='index'),
    path('', include(router.urls)),
    path('redirect/', redirect),
    # path('about/', about, name='about'),
    # path('book-list/', views.book_list, name='book-list'),
    # path('book-detail/<int:pk>', views.book_detail, name='book-detail'),
    # path('find-by-fiction/', views.books_by_fiction, name='find-book-by-fiction'),
    # path('find-by-price/', views.books_by_price, name='books-by-price'),
    # path('books/', views.BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetails.as_view(), name='book-detail'),
    # path('publishers/', views.publishers_api, name='publisher-list'),
    # path('publisher/<int:pk>/', views.publisher_detail_api, name='publisher-detail'),
]