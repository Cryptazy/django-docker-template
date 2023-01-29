from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

# Create your views here.

class Index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'landing/index.html'

    def get(self,request):
        return Response({'message':'Hello MLTA community'})