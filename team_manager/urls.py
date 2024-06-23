from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('user', views.UserViewSet)
router.register('project', views.ProjectViewSet)
router.register('project-member', views.ProjectMemberViewSet)
router.register('task', views.TaskViewSet)
router.register('comment', views.CommentViewSet)

urlpatterns = router.urls