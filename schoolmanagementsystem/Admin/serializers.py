from rest_framework import serializers
from Admin.models import User,OfficeStaff,Librarian,LibraryHistory,Student,FeesHistory
import logging

class UserSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    password=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password1","password2","phone_number","password","profile_picture","role","address"]

    def create(self, validated_data):
        password1=validated_data.pop("password1")
        password2=validated_data.pop("password2")
        return User.objects.create_user(**validated_data,password=password1)
    
    def validate(self, data):
        if data["password1"]!=data["password2"]:
            raise serializers.ValidationError("password mismatch")
        
        return data
    

logger = logging.getLogger(__name__)

class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            logger.debug(f"Found user by username: {user.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this username.")

        # Check user role
        if not (user.role=="admin"):
            raise serializers.ValidationError('This is not a admin account.')

        # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.username}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs
    
class StaffLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            logger.debug(f"Found user by username: {user.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this username.")

        # Check user role
        if not (user.role=="office_staff"):
            raise serializers.ValidationError('This is not a office stafff account.')

        # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.username}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs
    

class LibrarianLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(username=username)
            logger.debug(f"Found user by username: {user.username}")
        except User.DoesNotExist:
            raise serializers.ValidationError("No account found with this username.")

        # Check user role
        if not (user.role=="librarian"):
            raise serializers.ValidationError('This is not a librarian account.')

        # Verify password
        if not user.check_password(password):
            logger.debug(f"Password verification failed for user: {user.username}")
            raise serializers.ValidationError('Invalid password.')
        
        logger.debug("Authentication successful.")
        attrs['user'] = user
        return attrs
    


class OfficeStaffSerializer(serializers.ModelSerializer):
    user_profile = UserSerializer()

    class Meta:
        model =OfficeStaff
        fields = ['id', 'user_profile', 'department', 'position', 'joined_date', 'is_active', 'created_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user_profile')
        password1=user_data.pop("password1")
        password2=user_data.pop("password2")
        user = User.objects.create_user(**user_data,password=password1)
        office_staff = OfficeStaff.objects.create(user_profile=user, **validated_data)
        return office_staff

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user_profile')
        user = instance.user_profile

        instance.department = validated_data.get('department', instance.department)
        instance.position = validated_data.get('position', instance.position)
        instance.joined_date = validated_data.get('joined_date', instance.joined_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        user.email = user_data.get('email', user.email)
        user.profile_picture = user_data.get('profile_picture', user.profile_picture)
        user.role = user_data.get('role', user.role)
        user.phone_number = user_data.get('phone_number', user.phone_number)
        user.address = user_data.get('address', user.address)
        user.save()

        return instance



class LibraryStaffSerializer(serializers.ModelSerializer):
    user_profile = UserSerializer()

    class Meta:
        model =Librarian
        fields = ['id', 'user_profile', 'department', 'position', 'joined_date', 'is_active', 'created_date']

    def create(self, validated_data):
        user_data = validated_data.pop('user_profile')
        password1=user_data.pop("password1")
        password2=user_data.pop("password2")
        user = User.objects.create_user(**user_data,password=password1)
        office_staff = Librarian.objects.create(user_profile=user, **validated_data)
        return office_staff

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user_profile')
        user = instance.user_profile

        instance.department = validated_data.get('department', instance.department)
        instance.position = validated_data.get('position', instance.position)
        instance.joined_date = validated_data.get('joined_date', instance.joined_date)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()

        user.email = user_data.get('email', user.email)
        user.profile_picture = user_data.get('profile_picture', user.profile_picture)
        user.role = user_data.get('role', user.role)
        user.phone_number = user_data.get('phone_number', user.phone_number)
        user.address = user_data.get('address', user.address)
        user.save()

        return instance
    


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'grade', 'address', 'email', 'phone_number', 'is_active', 'created_date']
        read_only_fields = ['created_date']


class FeesHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeesHistory
        fields = ['id', 'student', 'amount', 'fee_type', 'remarks', 'payment_date']
        read_only_fields = ['payment_date']


class LibraryHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryHistory
        fields = ['id', 'student', 'book_name', 'borrow_date', 'return_date', 'status']
