from rest_framework import serializers 
from .models import * 


class DriverSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Driver
        fields = "__all__"


class PrivateAgentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PrivateAgent
        fields = "__all__"


class MunicipalAgentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MunicipalAgent
        fields = "__all__"



class AdminSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Admin
        fields = "__all__"


class PaymentLogSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PaymentLog
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Transaction
        fields = "__all__"


class ParkingLotSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ParkingLot
        fields = "__all__"

class MunicipalityZoneSerializer(serializers.ModelSerializer):
    class Meta: 
        model = MunicipalityZone
        fields = "__all__"

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Car
        fields = "__all__"

class ViolationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Violation
        fields = "__all__"