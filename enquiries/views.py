from django.shortcuts import render

# Create your views here.

# We’re gonna create these API functions for CRUD Operations:
# – enquiry_list(): GET list of enquiries, POST a new enquiry, DELETE all enquiries
# – enquiry_detail(): GET / PUT / DELETE enquiry by ‘id’
# – enquiry_list_published(): GET all published enquiries

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from enquiries.models import Enquiry
from enquiries.serializers import EnquirySerializer
from rest_framework.decorators import api_view

@api_view (['GET', 'POST', 'DELETE'])
def enquiry_list(request):
    # GET list of enquiries, POST a new enquiry, DELETE all enquiries
    if request.method == 'GET':
        enquiries = Enquiry.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            enquiries = enquiries.filter(title__icontains=title)

        enquiries_serializer = EnquirySerializer(enquiries, many=True)
        return JsonResponse(enquiries_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        enquiry_data = JSONParser().parse(request)
        enquiry_serializer = EnquirySerializer(data=enquiry_data)
        if enquiry_serializer.is_valid():
            enquiry_serializer.save()
            return JsonResponse(enquiry_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(enquiry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Enquiry.objects.all().delete()
        return JsonResponse({'message': '{} Enquiries were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view (['GET', 'PUT', 'DELETE'])
def enquiry_detail(request, pk):
    # find enquiry by pk (id)
    try:
        enquiry = enquiry.objects.get(pk=pk)
        if request.method == 'GET':
            enquiry_serializer = EnquirySerializer(enquiry)
            return JsonResponse(enquiry_serializer.data)

        elif request.method == 'PUT':
            enquiry_data = JSONParser().parse(request)
            enquiry_serializer = EnquirySerializer(enquiry, data=enquiry_data)
            if enquiry_serializer.is_valid():
                enquiry_serializer.save()
                return JsonResponse(enquiry_serializer.data)
            return JsonResponse(enquiry_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            enquiry.delete()
            return JsonResponse({'message': 'Enquiry was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    except enquiry.DoesNotExist:
        return JsonResponse({'message': 'The enquiry does not exist'}, status=status.HTTP_404_NOT_FOUND)
    # GET / PUT/ DELETE enquiry
