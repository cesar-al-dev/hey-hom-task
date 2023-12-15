from django.urls import path
from .views import CustomTokenObtainPairView, PropertyList, PropertyDetail, PropertyInsert

urlpatterns = [
    path('properties/', PropertyList.as_view(), name='property-list'),
    path('properties/', PropertyInsert.as_view(), name='property-insert'),
    path('properties/<int:pk>/', PropertyDetail.as_view(), name='property-detail'),
    path('auth/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
