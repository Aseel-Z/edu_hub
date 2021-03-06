from django.db.models import fields
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from edu_hub_project import settings
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class LoginSerializer(serializers.ModelSerializer):
     class Meta:
         model=User
         fields=('email','password') 


class RegisterSerializer(serializers.Serializer):

    email = serializers.EmailField(required=settings.ACCOUNT_EMAIL_REQUIRED)
    first_name = serializers.CharField(required=False, write_only=True)
    last_name = serializers.CharField(required=False, write_only=True)
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('email', )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'

class UserSignUp(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

 
    class Meta:
        
        # fields = "__all__"
        model = User
        fields = ("id", "username","password","email","first_name","city","member", "mobile_number","specialization","interests","biography","hourly_tutoring_rate",'organization_summary', 'gender',)
        # fields = ("id", "username","password","email",)

        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            city=validated_data['city'],
            member=validated_data['member'],
            mobile_number=validated_data['mobile_number'],
            specialization=validated_data['specialization'],
            interests=validated_data['interests'],
            biography=validated_data['biography'],
            hourly_tutoring_rate=validated_data['hourly_tutoring_rate'],
            gender=validated_data['gender'],
            organization_summary=validated_data['organization_summary'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user