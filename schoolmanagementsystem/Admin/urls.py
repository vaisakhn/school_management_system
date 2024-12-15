from django.urls import path
from Admin import views

urlpatterns = [
    path('admin-login/',views.AdminLoginView.as_view(),name="admin-login"),
    path('user-reg/',views.UserRegistrationView.as_view(),name="user-create"),
    path('create-staff/',views.OfficeStaffCreateView.as_view(),name="staff-create"),
    path('staff/<int:pk>/',views.OfficeStaffDetailAPIView.as_view(),name="staff"),
    path('create-librarian/',views.LibraryStaffCreateView.as_view(),name="librarian-create"),
    path('librarian/<int:pk>/',views.LibraryStaffDetailAPIView.as_view(),name="loibrarian"),
    path('students/', views.StudentListCreateAPIView.as_view(), name='student-list-create'), 
    path('students/<int:pk>/',views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail-update-delete'),
    path('feeshistory/',views.FeesHistoryListCreateAPIView.as_view(), name='feeshistory-list-create'), 
    path('feeshistory/<int:pk>/',views.FeesHistoryRetrieveUpdateDestroyAPIView.as_view(), name='feeshistory-detail-update-delete'), 
    path('libraryhistory/',views.LibraryHistoryListCreateAPIView.as_view(), name='libraryhistory-list-create'),
    path('libraryhistory/<int:pk>/',views.LibraryHistoryRetrieveUpdateDestroyAPIView.as_view(), name='libraryhistory-detail-update-delete'),
]
