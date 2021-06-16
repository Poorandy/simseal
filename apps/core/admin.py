import uuid
from django.contrib import admin, messages
from apps.simc.models import Monster, Card, Character, BattleField
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin, ExportActionModelAdmin
from simpleui.admin import AjaxAdmin

from datetime import datetime

from django.http import JsonResponse

# Register your models here.

# 怪物admin


class MonsterResource(resources.ModelResource):
    class Meta:
        exclude = ('id',)
        model = Monster


@admin.register(Monster)
class MonsterAdmin(ExportActionModelAdmin, AjaxAdmin):
    resource_class = MonsterResource
    search_fields = ('name', 'unit_flag',)
    list_filter = ('name',)
    date_hierarchy = 'update_time'
    list_display = ('id', 'name',
                    'behavior_script', 'health', 'sync', 'editor', 'update_time')
    ordering = ['name']
    list_per_page = 100
    # actions = ['make_copy', ]

    def message_success(self, request, queryset, context):
        messages.add_message(request, messages.SUCCESS, context)

    # @admin.action(description='COPY')
    def make_copy(self, request, queryset):
        post = request.POST
        if not post.get('_selected_action'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据! '
            })
        else:
            querysetlist = list()
            for i in post.getlist('_selected_action'):
                random = '__' + str(datetime.now())
                monster = Monster.objects.get(id=i)
                monster.name += random
                monster.id = uuid.uuid4()
                querysetlist.append(monster)
            Monster.objects.bulk_create(querysetlist)

            self.message_success(request, queryset, context='复制成功！')
        pass

    make_copy.short_description = '复制'
    make_copy.icon = 'fas fa-paste'
    make_copy.style = 'background:orange;color:white'
    make_copy.confirm = '是否确认复制一份？'


# 卡牌admin
class CardResource(resources.ModelResource):
    class Meta:
        exclude = ('id',)
        model = Card


@admin.register(Card)
class CardAdmin(ExportActionModelAdmin, AjaxAdmin):
    resource_class = CardResource
    search_fields = ('name', 'type',)
    list_filter = ('name',)
    date_hierarchy = 'update_time'
    list_display = ('id', 'name',
                    'behavior_script', 'editor', 'update_time')
    ordering = ['name']
    list_per_page = 100

    # actions = ['make_copy', 'link_module', 'run_index']
    # actions = ['make_copy', ]

    def message_success(self, request, queryset, context):
        messages.add_message(request, messages.SUCCESS, context)

    def make_copy(self, request, queryset):
        post = request.POST
        if not post.get('_selected_action'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据! '
            })
        else:
            querysetlist = list()
            for i in post.getlist('_selected_action'):
                random = '__' + str(datetime.now())
                card = Card.objects.get(id=i)
                card.name += random
                card.id = uuid.uuid4()
                querysetlist.append(card)
            Card.objects.bulk_create(querysetlist)

            self.message_success(request, queryset, context='复制成功！')
        pass

    make_copy.short_description = '复制'
    make_copy.icon = 'fas fa-paste'
    make_copy.style = 'background:orange;color:white'
    make_copy.confirm = '是否确认复制一份？'


# 主角admin
class CharacterResource(resources.ModelResource):
    class Meta:
        exclude = ('id',)
        model = Character


@admin.register(Character)
class CharacterAdmin(ExportActionModelAdmin, AjaxAdmin):
    resource_class = CharacterResource
    search_fields = ('name',)
    list_filter = ('name',)
    date_hierarchy = 'update_time'
    list_display = ('id', 'name',
                    'behavior_script', 'health', 'sync', 'editor', 'update_time')
    ordering = ['name']
    list_per_page = 100

    # actions = ['make_copy', 'link_module', 'run_index']
    # actions = ['make_copy', ]

    def message_success(self, request, queryset, context):
        messages.add_message(request, messages.SUCCESS, context)

    def make_copy(self, request, queryset):
        post = request.POST
        if not post.get('_selected_action'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请先选中数据! '
            })
        else:
            querysetlist = list()
            for i in post.getlist('_selected_action'):
                random = '__' + str(datetime.now())
                character = Character.objects.get(id=i)
                character.name += random
                character.id = uuid.uuid4()
                querysetlist.append(character)
            Character.objects.bulk_create(querysetlist)

            self.message_success(request, queryset, context='复制成功！')
        pass

    make_copy.short_description = '复制'
    make_copy.icon = 'fas fa-paste'
    make_copy.style = 'background:orange;color:white'
    make_copy.confirm = '是否确认复制一份？'


# 战斗admin

class BattleFieldResource(resources.ModelResource):
    class Meta:
        exclude = ('id',)
        model = BattleField


@admin.register(BattleField)
class BattleFieldAdmin(ExportActionModelAdmin, AjaxAdmin):
    resource_class = BattleFieldResource
    search_fields = ('name',)
    list_filter = ('name',)
    date_hierarchy = 'update_time'
    list_display = ('name',
                    'summary', 'editor', 'update_time')
    ordering = ['name']
    list_per_page = 100

    # actions = ['make_copy', 'link_module', 'run_index']
    # actions = ['make_copy', ]

    def message_success(self, request, queryset, context):
        messages.add_message(request, messages.SUCCESS, context)
