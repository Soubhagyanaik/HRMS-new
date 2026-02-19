from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attendance
        fields = '__all__'

    def validate(self, data):
        if Attendance.objects.filter(
            employee=data['employee'],
            date=data['date']
        ).exists():
            raise serializers.ValidationError("Attendance already marked for this date.")
        return data
