from django.conf.urls import url, include

from . import views

app_name = 'boardgames'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^[?]pages=([0-9]+)/([?]results=([0-9]+))?/$', views.index, name='index'),
    # ex: /boardgames/100/101/ was to be sent to a view for url processing and redirecting 
    # url(r'^(?P<currBoardgameId>[0-9]+)(?:/([\w-]+))?/(?P<nextBoardgameId>[0-9]+)/$', views.next_detail, name='next_detail'),
    # ex: /boardgames/5/
    # url(r'^(?P<boardgameId>[0-9]+)(?:/([\w-]+))?/$', views.detail, name='detail'),
    # url(r'^(?P<boardgameId>[0-9]+)?/', include([
    #     url(r'^add_favourite/$', views.add_favourite, name='add_favourite'),
    #     url(r'^remove_favourite/$', views.remove_favourite, name='remove_favourite'),
    # ])),
    # The next two urls are in case multiple urls to the same destination is better than an optional path
    url(r'^(?P<boardgameId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<boardgameId>[0-9]+)/add_favourite/$', views.add_favourite, name='add_favourite'),
    url(r'^(?P<boardgameId>[0-9]+)/remove_favourite/$', views.remove_favourite, name='remove_favourite'),
    url(r'^(?P<boardgameId>[0-9]+)?/([\w-]+)/$', views.detail, name='detail'),

    url(r'^search/$', views.search, name='search'),
]