import stripe
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, authentication, permissions

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Order, OrderItem
from . serializers import OrderSerializers


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializers(data=request.data)
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amound = sum(item.get('quantity')* item.get('product').price for item in serializer.validated_data['items'])
        try:
            charge = stripe.Charge.create(
                amount= int(paid_amound *100),
                currency = 'USD',    
                description = "Charge from E-Commerce",         
                source =   serializer.validated_data['stripe_token']
            )
            serializer.save(user= request.user, paid_amound = paid_amound)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
            