from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import generics, permissions
from .models import Blog
from .serializers import BlogSerializer

def home(request):
    return JsonResponse({"message": "Welcome to the Blog API!"})

def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})

# List and Create Blogs - CBV
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Retrieve, Update, and Delete a Single Blog - CBV
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
