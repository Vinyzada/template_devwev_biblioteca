from rest_framework.viewsets import ModelViewSet
from core.serializers import LivroSerializer, LivroListSerializer, LivroRetrieveSerializer 
from core.models import Livro

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroRetrieveSerializer
        return LivroSerializer