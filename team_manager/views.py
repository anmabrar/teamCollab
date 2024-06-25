from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from .models import(
    User,
    Project,
    ProjectMember,
    Task,
    Comment
)
from .serializers import(
    UserSerializer,
    UserLoginSerializer,
    ProjectSerializer,
    ProjectMemberSerializer,
    TaskSerializer,
    CommentSerializer,

)


class UserRegisterViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserSerializer


class UserLoginViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = UserLoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # If user is authenticated, generate JWT token
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)
        

class UserViewSet(ModelViewSet):
    http_method_names = ['get', 'put', 'patch', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = PageNumberPagination

class ProjectMemberViewSet(ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    pagination_class = PageNumberPagination

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination