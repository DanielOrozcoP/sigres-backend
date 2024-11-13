from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.

    This serializer is used to validate and create a new user account. It also handles password validation,
    email uniqueness, and optional group assignment.

    Attributes:
    password2 (CharField): The repeated password for confirmation.
    group (CharField): The name of the group to which the user should be assigned.

    Methods:
    save(): Creates a new user account, sets the password, and assigns the user to a group if specified.
    """

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    group = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password','password2','group']
        extra_kwargs = {
            'password': {'write_only' :True}
        }

    def save(self):
        """
        Creates a new user account, sets the password, and assigns the user to a group if specified.

        Validates the password confirmation, checks for email uniqueness, and handles group assignment.

        Returns:
        User: The newly created user account.
        """

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'El password de confirmacion no coincide'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'El email del usuario ya existe'})
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        group_name = self.validated_data.get('group')
        if group_name:
            try:
                group = Group.objects.get(name=group_name)
                account.groups.add(group)
            except Group.DoesNotExist:
                raise serializers.ValidationError({'error': 'El grupo especificado no existe'})

        return account