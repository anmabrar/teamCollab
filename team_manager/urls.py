from rest_framework import routers
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()

router.register('user/register', views.UserRegisterViewSet, basename='user-register')
router.register('user/login', views.UserLoginViewSet, basename='user-login')
router.register('users', views.UserViewSet)

router.register('projects', views.ProjectViewSet, basename='projects')
router.register('project-members', views.ProjectMemberViewSet)
router.register('tasks', views.TaskViewSet)
router.register('comments', views.CommentViewSet)
 
# Nested router
projects_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
projects_router.register('tasks', views.TaskViewSet, basename='project-tasks')

urlpatterns = router.urls + projects_router.urls 