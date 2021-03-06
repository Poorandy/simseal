"""simseal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import RedirectView
from rest_framework.authtoken import views

from apps.simc.views import CharacterView, CardView, MonsterView, BattleView, BattleSimc, BattleIsExist

admin.site.site_title = f'PROJECT SEAL SIMULAION PLATFORM'
admin.site.site_header = f'SIMSEAL'

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api-token-auth/', views.obtain_auth_token),
                  path('api/character/', CharacterView.as_view()),
                  path('api/card/', CardView.as_view()),
                  path('api/monster/', MonsterView.as_view()),
                  path('api/battle/', BattleSimc.as_view()),
                  path('api/combat/', BattleView.as_view()),
                  path('api/combat_check/', BattleIsExist.as_view()),
                  url(r'^favicon\.ico$', RedirectView.as_view(
                      url='/static/images/favicon.ico')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]
