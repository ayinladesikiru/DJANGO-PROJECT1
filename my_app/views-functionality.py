from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Publisher
from rest_framework import status
from .serializer import BookSerializer, PublisherSerializer


def index(request):
    name = "Asa"
    return render(request, "my_app/index.html", context={'name': name})


def redirect(request):
    return HttpResponseRedirect(reverse('my_app:index'))


def about(request):
    return render(request, 'my_app/about.html')


def book_list(request):
    books = Book.objects.all()
    return render(request, 'my_app/book-list.html', {'books': list(books)})


def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        return render(request, 'my_app/book_detail.html', {'book': book})
    except Book.DoesNotExist:
        return HttpResponse("Book Does Not Exist")


def books_by_fiction(request):
    books = Book.objects.filter(genre='FICTION')
    return render(request, 'my_app/fiction-books.html', {'books': books})


def books_by_price(request):
    books = Book.objects.filter(price__gt=200)
    return render(request, 'my_app/book-price.html', {'books': books})


@api_view(['GET', 'POST'])
def books_api(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def book_detail_api(request, pk):
    # book = Book.objects.get(pk=pk)
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(Book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def publishers_api(request):
    if request.method == 'GET':
        queryset = Publisher.objects.all()
        serializer = PublisherSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def publisher_detail_api(request, pk):
    # book = Book.objects.get(pk=pk)
    book = get_object_or_404(Publisher, pk=pk)
    if request.method == 'GET':
        serializer = PublisherSerializer(book, context={'request': request})
        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = PublisherSerializer(Book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
