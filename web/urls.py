"""web URL Configuration

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
from django.conf.urls import url
from django.contrib import admin, auth
from web import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^login/$', views.login_view),
    url(r'^logout/$', views.logout_view),

    url(r'^passwd/$', views.passwd_view),

    url(r'^article/(?P<name>\w+)/$', views.article_view),

    url(r'^admin/account/add/(?P<uid>\d+)/(?P<service_name>\w+)/$', views.views_admin.account_add),
    url(r'^admin/account/edit/(?P<account_id>\d+)/$', views.views_admin.account_edit),
    url(r'^admin/account/toggle/(?P<account_id>\d+)/$', views.views_admin.account_toggle),
    url(r'^admin/account/traffic/(?P<account_id>\d+)/$', views.views_admin.account_traffic),
    url(r'^admin/account/quick/(?P<account_id>\d+)/(?P<action>\w+)/$', views.views_admin.account_quick),
    url(r'^admin/quota/add_to/(?P<account_id>\d+)/$', views.views_admin.quota_add),
    url(r'^admin/quota/edit/(?P<quota_id>\d+)/$', views.views_admin.quota_edit),
    url(r'^admin/quota/toggle/(?P<quota_id>\d+)/$', views.views_admin.quota_toggle),
    url(r'^admin/quota/remove/(?P<quota_id>\d+)/$', views.views_admin.quota_remove),
    url(r'^admin/quota/reset/(?P<quota_id>\d+)/$', views.views_admin.quota_reset),
    url(r'^admin/user/$', views.views_admin.user_list),
    url(r'^admin/user/toggle/(?P<uid>\d+)/$', views.views_admin.user_toggle),
    url(r'^admin/user/edit/(?P<uid>\d+)/$', views.views_admin.user_edit),
    url(r'^admin/user/add/$', views.views_admin.user_add),
    url(r'^admin/', admin.site.urls),

    url(r'^account/$', views.account_view),
    url(r'^account/traffic/(?P<service>\w+)/$', views.traffic_view),
    url(r'^account/edit/(?P<service>\w+)/$', views.account_edit_view),

    url(r'^qr\.svg$', views.qr_view),
]
