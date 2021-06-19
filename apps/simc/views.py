from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from django.shortcuts import render
from django.core import serializers

from .models import Card, Character, Monster, BattleField, User
from apps.simc.battle.battle_flow import BattleFlow

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
            response = {'code': 200, 'data': total,
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
            response = {'code': 200, 'data': total,
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
            response = {'code': 200, 'data': total,
                        'msg': 'success', 'total': len(list(total))}
        except Exception as e:
            response = {'code': 500, 'data': None,
                        'msg': str(e), 'total': None}

        return Response(response)


class BattleSimc(APIView):

    def post(self, request):
        editor = self.request.user.id
        received_json_data = json.loads(request.body)
        keys = ["name", "monsters", "character", "cards"]
        battle_data = {key: received_json_data.get(key) for key in keys}
        BattleField.objects.update_or_create(name=received_json_data.get('name'),
                                             summary=received_json_data.get(
            'summary', ""), editor=editor
        )
        battle_flow = BattleFlow(**battle_data)
        battle_flow.battle()

        response = {'code': 200, 'data': str(battle_flow),
                    'msg': 'success', 'total': 1}
        BattleField.objects.filter(name=received_json_data.get(
            'name')).update(combat_log=str(battle_flow))

        return Response(response)


class BattleView(APIView):

    def get(self, request):
        try:
            editor = self.request.user.id
            pg = sealPagination()
            page_roles = pg.paginate_queryset(
                queryset=BattleField.objects.filter(delete_flag=0, editor=editor), request=request, view=self)
            data = json.loads(serializers.serialize("json", page_roles))
            total = json.loads(serializers.serialize(
                "json", BattleField.objects.filter(delete_flag=0)))
            response = {'code': 200, 'data': total,
                        'msg': 'success', 'total': len(list(total))}
        except Exception as e:
            response = {'code': 500, 'data': None,
                        'msg': str(e), 'total': None}

        return Response(response)


class BattleIsExist(APIView):

    def get(self, request):
        try:
            name = request.GET['name']
            total = json.loads(serializers.serialize(
                "json", BattleField.objects.filter(delete_flag=0, name=name)))
            print(total)
            response = {'code': 200, 'data': total != [],
                        'msg': 'success'}
        except Exception as e:
            response = {'code': 500, 'data': None,
                        'msg': str(e)}

        return Response(response)
