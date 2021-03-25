from rest_framework import serializers
from rest_framework import Signup

class Signupserializers(serializers.ModelSerializer):
    class Meta:
        model = Signup
    fields = '__all__'