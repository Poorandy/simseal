import uuid
from django.contrib import admin, messages
from apps.simc.models import Monster, Card, Character, BattleField
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from simpleui.admin import AjaxAdmin

from datetime import datetime

from django.http import JsonResponse

# Register your models here.


class MonsterResource(resources.ModelResource):
    class Meta:
        exclude = ('id',)
        model = Monster


@admin.register(Monster)
class MonsterAdmin(ImportExportActionModelAdmin, AjaxAdmin):
    resource_class = MonsterResource
    search_fields = ('name', 'unit_flag',)
    list_filter = ('name',)
    date_hierarchy = 'update_time'
    list_display = ('id', 'name', 'summary',
                    'behavior', 'health', 'sync', 'update_time')
    ordering = ['name']
    list_per_page = 100

    # actions = ['make_copy', 'link_module', 'run_index']
    actions = ['make_copy', ]

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

    def run_index(self, request, queryset):
        pass

    run_index.short_description = '跑指标'
    run_index.icon = 'far fa-play-circle'
    run_index.style = 'background:green;color:white'
    run_index.confirm = '是否确认执行指标？'
