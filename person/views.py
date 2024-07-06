from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Person, Category
from .serializers import PoetSerializers


class CRUDPoet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    # queryset = Person.objects.all()[:1]
    serializer_class = PoetSerializers

    def get_queryset(self):
        return Person.objects.all()

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})


# class ListCreatePoet(generics.ListCreateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
#
# class RetrivePoet(generics.RetrieveAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers
#
#
# class UpdateDeletePoet(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers






# class ListCreatePoet(APIView):
#     def get(self, request):
#         lst = Person.objects.all()
#         return Response({'Poet': PoetSerializers(lst, many=True).data})
#
#     def post(self, requests):
#         serializers = PoetSerializers(data=requests.data)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#
#         return Response({"posts": serializers.data})
#
#
#
#
#
# class UpdateDeletePoet(APIView):
#     def put(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method PUT not allowed!"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found!"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#
#
#     def patch(self, requests, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method PUT not allowed!"})
#
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"post": "Object not found!"})
#
#         serializers = PoetSerializers(data=requests.data, instance=instance, partial=True)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"post": serializers.data})
#
#
#     def delete(self, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"post": "Method PUT not allowed!"})
#         try:
#             instance = Person.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"post": "Object not found!"})
#
#         return Response({"answer": f"Deleted ID - {pk}"})

# class ListPoet(generics.ListAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PoetSerializers

