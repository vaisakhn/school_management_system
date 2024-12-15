from django.urls import path,include
from officestaff import views

urlpatterns = [
    path('staff-login/',views.StaffLoginView.as_view(),name="staff-login"),
    path('students/', views.StudentListAPIView.as_view(), name='student-list'), 
    path('students/<int:pk>/',views.StudentRetrieveAPIView.as_view(), name='student-detail'),
    path('feeshistory/',views.FeesHistoryListCreateAPIView.as_view(), name='feeshistory-list-create'), 
    path('feeshistory/<int:pk>/',views.FeesHistoryRetrieveUpdateDestroyAPIView.as_view(), name='feeshistory-detail-update-delete'),
    path('libraryhistory/',views.LibraryHistoryListAPIView.as_view(), name='libraryhistory-list'),
    path('libraryhistory/<int:pk>/',views.LibraryHistoryRetrieveAPIView.as_view(), name='libraryhistory-detail'),
]
