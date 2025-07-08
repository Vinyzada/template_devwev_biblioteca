from rest_framework.serializers import SerializerMethodField, ModelSerializer, CharField
from core.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()

    def get_total(self, obj):
        return obj.livro.preco * obj.quantidade

    class Meta:
        model = ItensCompra
        fields = '__all__'
        read_only_fields = ['id', 'compra', 'livro']

class CompraSerializer(ModelSerializer):
    usuario = CharField(source='usuario.email', read_only=True) 
    status = CharField(source='get_status_display', read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    depth = 1

    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ['id', 'usuario', 'status']