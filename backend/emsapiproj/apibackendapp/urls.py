from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, EmployeeViewSet, ProjectViewSet

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('employees', EmployeeViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = router.urls
