from rest_framework import serializers 
from coupons.models import CouponsMod
from django.utils.timezone import now

class CouponsModSerializer(serializers.ModelSerializer):

    class Meta:
        model = CouponsMod
        fields = ('id', 'name', 'user', 'valid_from', 'valid_to', 'discount')


class RedeemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CouponsMod
        fields = ('name', 'user', 'discount','active')
    
    def validate(self,data):

        coupon = data['CouponsMod']
        user = data['user']

        if CouponsMod.active == False:
            raise serializers.ValidationError("Coupon is not active")

        if CouponsMod.valid_to < now:
            CouponsMod.active = False
            raise serializers.ValidationError("Expiration date set in the past")

        if CouponsMod.user != user:
            raise serializers.ValidationError("Coupon bound to another user")