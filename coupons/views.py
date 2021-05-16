from django.contrib.auth.models import User
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, viewsets

from coupons.models import CouponsMod
from coupons.serializers import CouponsModSerializer, RedeemSerializer
from .permissions import IsOwner
# Create your views here.

def index(request):
    "Method to sort the coupons table by discount"
    coupons = CouponsMod.objects.all()
    sorted_by_discount = sorted(coupons, key=lambda CouponsMod:CouponsMod.discount )
    return render(request, 'coupons/index.html', context={'sorted_by_discount':sorted_by_discount})

class CreateView(generics.ListCreateAPIView):
    """This class handles the GET and POST requests"""
    queryset = CouponsMod.objects.all()
    serializer_class = CouponsModSerializer

class DetailsView(generics.RetrieveDestroyAPIView):
    """This class handles GET and DELETE requests."""

    queryset = CouponsMod.objects.all()
    serializer_class = CouponsModSerializer

    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)

class RedeemViewSet(viewsets.ModelViewSet):
    queryset = CouponsMod.objects.all()
    serializer_class = RedeemSerializer