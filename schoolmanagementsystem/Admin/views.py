from django.shortcuts import render
from Admin.models import User,OfficeStaff,Student,FeesHistory,Librarian,LibraryHistory
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Admin.serializers import UserSerializer,AdminLoginSerializer,logger,StaffLoginSerializer,LibrarianLoginSerializer,OfficeStaffSerializer,LibraryStaffSerializer,StudentSerializer,FeesHistorySerializer,LibraryHistorySerializer
from rest_framework.permissions import BasePermission,IsAdminUser,IsAuthenticated
from django.shortcuts import get_object_or_404


# overriding isadminuser permision
class IsAdminUser(BasePermission):
    def has_permission(self, request, view): # Check if the user is authenticated and is a admin
        return request.user and (request.user.role=="admin")

# implemented user registration view
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer


# login view for admin 
class AdminLoginView(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = AdminLoginSerializer(data=request.data)
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
        

# creates New staff
class OfficeStaffCreateView(generics.CreateAPIView):
    serializer_class=OfficeStaffSerializer
    permission_classes=[IsAdminUser]


# retrive , update or delete the staf data
class OfficeStaffDetailAPIView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, pk):
        office_staff = get_object_or_404(OfficeStaff, pk=pk)
        serializer = OfficeStaffSerializer(office_staff)
        return Response(serializer.data)

    def put(self, request, pk):
        office_staff = get_object_or_404(OfficeStaff, pk=pk)
        serializer = OfficeStaffSerializer(office_staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        office_staff = get_object_or_404(OfficeStaff, pk=pk)
        office_staff.delete()
        return Response({"message":"staff deleted succesfully"},status=status.HTTP_204_NO_CONTENT)

# create new librarian accounts
class LibraryStaffCreateView(generics.CreateAPIView):
    serializer_class=LibraryStaffSerializer
    permission_classes=[IsAdminUser]


# retrive , update or delete the librarian data
class LibraryStaffDetailAPIView(APIView):
    permission_classes=[IsAdminUser]
    def get(self, request, pk):
        librarian = get_object_or_404(Librarian, pk=pk)
        serializer = LibraryStaffSerializer(librarian)
        return Response(serializer.data)

    def put(self, request, pk):
        librarian = get_object_or_404(Librarian, pk=pk)
        serializer = LibraryStaffSerializer(librarian,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        librarian = get_object_or_404(Librarian, pk=pk)
        librarian.delete()
        return Response({"message":"librarian deleted succesfully"},status=status.HTTP_204_NO_CONTENT)
    

# create students accounts,take list of students
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[IsAdminUser]

# get,update and delete student data
class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes=[IsAdminUser]

    def delete(self, request, *args, **kwargs): 
        student = self.get_object() 
        student.delete() 
        return Response({"message": "Student deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
    
# get list of fees history and create fee history
class FeesHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes=[IsAdminUser]

# fee history get,update,delete view
class FeesHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeesHistory.objects.all()
    serializer_class = FeesHistorySerializer
    permission_classes=[IsAdminUser]
    def delete(self, request, *args, **kwargs): 
        fees_history = self.get_object() 
        fees_history.delete() 
        return Response({"message": "fees history deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)


# get list of library history and create fee history
class LibraryHistoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes=[IsAdminUser]


# library history get,update,delete view
class LibraryHistoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LibraryHistory.objects.all()
    serializer_class = LibraryHistorySerializer
    permission_classes=[IsAdminUser]
    def delete(self, request, *args, **kwargs): 
        library_history = self.get_object() 
        library_history.delete() 
        return Response({"message": "library details deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

