from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book, Publisher
from rest_framework import status
from .serializer import BookSerializer, PublisherSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookList(ListCreateAPIView):
#     query_set = Book.objects.all()
#     serializer_class = BookSerializer
    # def get(self, request):
    #     queryset = Book.objects.all()
    #     serializer = BookSerializer(queryset, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = BookSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


class BookDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # def get(self, request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def patch(self, request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     serializer = BookSerializer(book, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, request, pk):
    #     book = get_object_or_404(Book, pk=pk)
    #     book.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


def index(request):
    name = "Asa"
    return render(request, "my_app/index.html", context={'name': name})


def redirect(request):
    return HttpResponseRedirect(reverse('my_app:index'))

#
