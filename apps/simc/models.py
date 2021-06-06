from django.db import models
from django.contrib.auth.models import User
import uuid
import json
from django.db.models.deletion import CASCADE
# Create your models here.


class Monster(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="单位名", max_length=50)
    summary = models.TextField(verbose_name="单位描述")
    health = models.IntegerField(verbose_name="血量")
    sync = models.IntegerField(verbose_name="同步值")
    # "@absDamage(5)|@consDamage(2,4)|absHeal(5)"
    behavior = models.TextField(verbose_name="单位行为")
    unit_flag = models.IntegerField(verbose_name="单位标记", default=0)
    update_time = models.DateTimeField(verbose_name="更新时间")
    create_time = models.DateTimeField(verbose_name="创建时间")
    delete_flag = models.SmallIntegerField(verbose_name="删除标记")

    class Meta:
        verbose_name = "怪物单位"

    def __str__(self):
        return json.dumps({'id': self.id, 'name': self.name}, ensure_ascii=False)


class BattleField(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="战斗名", max_length=255)
    summary = models.TextField(verbose_name="战斗描述")
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="账号ID")
    combat_log = models.TextField(verbose_name="战斗日志")
    update_time = models.DateTimeField(verbose_name="更新时间")
    create_time = models.DateTimeField(verbose_name="创建时间")
    delete_flag = models.SmallIntegerField(verbose_name="删除标记")

    class Meta:
        verbose_name = "战斗"


class Card(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)
    name = models.CharField(verbose_name="卡牌名", max_length=30)
    summary = models.TextField(verbose_name="卡牌描述")
    type = models.CharField(verbose_name="卡牌类型", default="Unit", max_length=16)
    behavior = models.TextField(verbose_name="单位行为")
    update_time = models.DateTimeField(verbose_name="更新时间")
    create_time = models.DateTimeField(verbose_name="创建时间")
    delete_flag = models.SmallIntegerField(verbose_name="删除标记")

    class Meta:
        verbose_name = "卡牌"


class Character(models.Model):
    id = models.UUIDField(
        verbose_name='ID', default=uuid.uuid4, primary_key=True)

    name = models.CharField(verbose_name="角色名", max_length=30)
    summary = models.TextField(verbose_name="角色描述")
    health = models.IntegerField(verbose_name="血量")
    sync = models.IntegerField(verbose_name="同步值")
    # "@absDamage(5)|@consDamage(2,4)|absHeal(5)"
    behavior = models.TextField(verbose_name="单位行为")
    update_time = models.DateTimeField(verbose_name="更新时间")
    create_time = models.DateTimeField(verbose_name="创建时间")
    delete_flag = models.SmallIntegerField(verbose_name="删除标记")

    class Meta:
        verbose_name = "角色"