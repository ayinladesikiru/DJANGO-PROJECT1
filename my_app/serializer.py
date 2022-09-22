from rest_framework import serializers

from my_app.models import Book, Publisher


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name', 'email', 'url']


class BookSerializer(serializers.ModelSerializer):  # noqa
    # book_title = serializers.CharField(max_length=255, source="title")
    # publisher = PublisherSerializer()
    # publisher = serializers.PrimaryKeyRelatedField(read_only=True)
    # publisher = serializers.HyperlinkedRelatedField(
    #     queryset=Publisher.objects.all(),
    #     view_name='my_app:publisher-detail'
    # )

    class Meta:
        model = Book
        # fields = "__all__"
        fields = ['title', 'description', 'date_published', 'isbn', 'price', 'publisher']
        # exclude = [] to exclude some fields and show the rest
        # field1 = ['book_title', 'description', 'date_published', 'isbn', 'price']
