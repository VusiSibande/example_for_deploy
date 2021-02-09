from rest_framework import routers
from .viewsets import EmployeeViewset


router = routers.DefaultRouter()

router.register(r'emp_list', EmployeeViewset)

# urlpatterns = [router.urls]
