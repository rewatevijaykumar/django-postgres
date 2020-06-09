from rest_framework import serializers
from enquiries.models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Enquiry
        fields = ('id',
        'name',
        'email',
        'mobile',
        'subject',
        'description')