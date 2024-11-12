from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    group = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['username','email','password','password2','group']
        extra_kwargs = {
            'password': {'write_only' :True}
        }
    
    def save(self):
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