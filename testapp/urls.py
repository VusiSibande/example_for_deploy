from django.urls import path, include
from .api.routers import router


urlpatterns = [
    path(r'emp_api/', include(router.urls))
]
