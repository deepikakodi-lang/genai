from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # Homepage
    # Individual Apps
    path('supplier/', include('supplier_contract_review.urls')),
    path('logistic/', include('logistic.urls')),
    path('underwriter/', include('underwriter.urls')),
    path('medical_claims/', include('medical_claims.urls')),
]
