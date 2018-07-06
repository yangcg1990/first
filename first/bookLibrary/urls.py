from django.urls import path

from bookLibrary.views import BookListView

app_name = 'bookLibrary'
urlpatterns = [
    path('book/list/', BookListView.as_view(), name='book_list'),
]
