from django.urls import path
from librarian import views

urlpatterns = [
    path('librarian-login/',views.LibrarianLoginView.as_view(),name="librarian-login"),
    path('library-history/',views.LibraryHistoryListAPIView.as_view(),name="library"),
    path('students/<int:pk>/',views.StudentRetrieveAPIView.as_view(), name='student-detail'),
    path('libraryhistory/<int:pk>/',views.LibraryHistoryRetrieveAPIView.as_view(), name='libraryhistory'),
    path('students/', views.StudentListAPIView.as_view(), name='student-list'), 
]
