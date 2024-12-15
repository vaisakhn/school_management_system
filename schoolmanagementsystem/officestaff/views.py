from django.shortcuts import render
from Admin.serializers import StaffLoginSerializer,StudentSerializer,LibraryHistorySerializer,FeesHistorySerializer
from rest_framework import generics,status
from rest_framework.response import Response
from Admin.models import User,Student,LibraryHistory,FeesHistory
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import BasePermission

# Create your views here.

# creating custom  permision for office staff
class IsOfficeStaff(BasePermission):
    def has_permission(self, request, view): # Check if the user is authenticated and is a admin
        return request.user and (request.user.role=="office_staff")

#login function for staff
class StaffLoginView(generics.GenericAPIView):
    serializer_class = StaffLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = StaffLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # fetch the user by username
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
        
            # Create JWT token
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'user_id': user.id,
                'email': user.email,
                'full_name': user.username,
                'user_type': user.role,
            }, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        

# take list of students
class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[IsOfficeStaff]

# get student details
class StudentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[IsOfficeStaff]


# creating fees history
class FeesHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes=[IsOfficeStaff]

# fee history get,update,delete view
class FeesHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes=[IsOfficeStaff]
    def delete(self, request, *args, **kwargs): 
        fees_history = self.get_object() 
        fees_history.delete() 
        return Response({"message": "fees history deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    

# view library history list
class LibraryHistoryListAPIView(generics.ListAPIView):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes=[IsOfficeStaff]


# view library history details for students
class LibraryHistoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes=[IsOfficeStaff]
