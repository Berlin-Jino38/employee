from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from myApp.models import EmployeeModel
from .serializers import MovieSerializer


class MovieListCreate(ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = MovieSerializer

class MovieRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = MovieSerializer