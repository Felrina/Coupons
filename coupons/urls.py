from django.urls import path
from coupons import views


# app_name = 'coupons'

urlpatterns = [
    path('coupons/', views.index, name="sorted_coupons"),
    path('api/coupons/',  views.CreateView.as_view(), name='create'),
    path('api/coupons/<int:pk>/',  views.DetailsView.as_view(), name='details'),
    path('api/redeem/',  views.RedeemViewSet, name='Redeem'),
]
