from django.conf.urls import url, include
from lists import views


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'lists/the-only-list-in-the-world/$', 'lists.views.list_view', 
    name='list_view'),
    # url(r'^admin/', include(admin.site.urls)),
]

