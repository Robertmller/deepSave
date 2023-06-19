from rest_framework import viewsets
from core.models import Link, Document
from core.serializer import LinkSerializer, DocumentSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
