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
    # exclude = (
    #     'up_code', 'up_name', 'is_valid', 'create_date', 'update_date', 'uuid', 'sys_insert_date', 'sys_update_date',
    #     'float')
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

    def link_module(self, request, queryset):

        post = request.POST
        # if not post.get('_selected'):
        #     return JsonResponse(data={
        #         'status': 'error',
        #         'msg': '请先选中数据! '
        #     })
        # else:
        #     querysetlist = list()
        #     for i in post.get('_selected').split(','):
        #         programs = Monster.objects.get(index_name=i)
        #         programs = json.loads(str(programs))
        #         querysetlist.append(
        #             InxModule(rule_id=programs.get('rule_id'), index_name=programs.get('index_name'),
        #                       module_id=post.get('module_id'),
        #                       product_name=post.get('product_name'),
        #                       product_code=post.get('product_code'),
        #                       operator_id=post.get('operator_id'),
        #                       area_id=post.get('area_id'), is_exist=1 if post.get('is_exist') else 0))
        #     InxModule.objects.bulk_create(querysetlist)

        #     self.message_success(
        #         request, queryset, context='组合成功！请在Inx_module表中查看！')

        #     return JsonResponse(data={
        #         'status': 'success',
        #         'msg': '处理成功!',
        #         'data': json.dumps(post, ensure_ascii=False)
        #     })
        pass

    link_module.short_description = '组合Module'
    link_module.icon = 'fab fa-staylinked'
    link_module.style = 'background:brown;color:white'

    link_module.layer = {
        'title': '组合module',
        'tips': '对选中的rule包装一个通用的module',
        'confirm_button': '确认',
        'cancel_button': '取消',
        'params': [{
            # 这里的type 对应el-input的原生input属性，默认为input
            'type': 'input',
            # key 对应post参数中的key
            'key': 'module_id',
            # 显示的文本
            'label': '模型ID',
            # 为空校验，默认为False
            'require': True
        }, {
            'type': 'input',
            'key': 'product_code',
            'label': '产品代码',
            'require': True
        }, {
            'type': 'input',
            'key': 'product_name',
            'label': '产品名',
            'require': True
        },
            {
                'type': 'input',
                'key': 'operator_id',
                'label': '操作人',
                'require': True,

        },
            {
                'type': 'input',
                'key': 'area_id',
                'label': '项目ID',
                'require': True,
                # 'options': [
                #     {
                #         'key': '',
                #         'label': ''
                #     }
                # ],
                # 'value': 'DX'
        },
            {
                'type': 'switch',
                'key': 'is_exist',
                'label': '是否存在',
                'value': True
        }
        ]
    }

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
                print(i)
                random = '__' + str(datetime.now())
                monster = Monster.objects.get(id=i)
                print(monster.name)
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
