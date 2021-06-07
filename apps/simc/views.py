from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import render
from django.core import serializers

from .models import Card, Character, Monster, BattleField

import json


class sealPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "size"
    max_page_size = 1000
    page_query_param = "page"

# Create your views here.


class CharacterView(APIView):

    def get(self, request):
        try:
            pg = sealPagination()
            page_roles = pg.paginate_queryset(
                queryset=Character.objects.filter(delete_flag=0), request=request, view=self)
            data = json.loads(serializers.serialize("json", page_roles))
            total = json.loads(serializers.serialize(
                "json", Character.objects.filter(delete_flag=0)))
            response = {'code': 200, 'data': data,
                        'msg': 'success', 'total': len(list(total))}
        except Exception as e:
            response = {'code': 500, 'data': None,
                        'msg': str(e), 'total': None}

        return Response(response)


class CardView(APIView):

    def get(self, request):
        try:
            pg = sealPagination()
            page_roles = pg.paginate_queryset(
                queryset=Card.objects.filter(delete_flag=0), request=request, view=self)
            data = json.loads(serializers.serialize("json", page_roles))
            total = json.loads(serializers.serialize(
                "json", Card.objects.filter(delete_flag=0)))
            response = {'code': 200, 'data': data,
                        'msg': 'success', 'total': len(list(total))}
        except Exception as e:
            response = {'code': 500, 'data': None,
                        'msg': str(e), 'total': None}

        return Response(response)


class MonsterView(APIView):

    def get(self, request):
        try:
            pg = sealPagination()
            page_roles = pg.paginate_queryset(
                queryset=Monster.objects.filter(delete_flag=0), request=request, view=self)
            data = json.loads(serializers.serialize("json", page_roles))
            total = json.loads(serializers.serialize(
                "json", Monster.objects.filter(delete_flag=0)))
            response = {'code': 200, 'data': data,
                        'msg': 'success', 'total': len(list(total))}
        except Exception as e:
            response = {'code': 500, 'data': None,
                        'msg': str(e), 'total': None}

        return Response(response)
