"""QuestionForum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles import views as static_views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^authentication/', include('authentication.urls')),
    url(r'^forum/', include('forum.urls')),
    url(r'^announcement/', include('announcement.urls')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^', include('website.urls')),
    url(r'^chat/', include('chat.urls')),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', static_views.static.serve, {'document_root': settings.STATIC_ROOT},
            name='static'),
        url(r'^media/(?P<path>.*)$', static_views.static.serve, {'document_root': settings.MEDIA_ROOT},
            name='media'),

    ]
