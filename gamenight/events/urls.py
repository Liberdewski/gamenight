from django.conf.urls import url

from . import views
#r stands for regular expression, ^ is the beginning, end is $
#?P<VARIABLE TO PASS TO FUNCTION[range of integers i.e. 0-9]+ means greater than 9>
#urls directs to views (directs to templates)
app_name = 'events'
urlpatterns = [
    #handles requests for index
    url(r'^$', views.index, name='index'),
    #handles requests for specific event according to event_id
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),
	#event creation
	url(r'^create/$', views.create_event, name='create',),
    #question creation
	url(r'^createquestion/(?P<event_id>[0-9]+)/$', views.create_question, name='createquestion',),
    #choice creation
	url(r'^createchoice/(?P<question_id>[0-9]+)/$', views.create_choice, name='createchoice',),
    #choice edit
	url(r'^editc/(?P<choice_id>[0-9]+)/$', views.edit_choice, name='editchoice',),
	#message creation
	url(r'^createmessage/(?P<event_id>[0-9]+)/$', views.create_message, name='createmessage',),
    #edits event
	url(r'^editevent/(?P<pk>\d+)/$', views.EditEventView.as_view(), name='editevent',),
    #edit question
    url(r'^editq/(?P<pk>\d+)/$', views.EditQuestionView.as_view(), name='editquestion',),
    #edit message
    url(r'^editm/(?P<pk>\d+)/$', views.EditMessageView.as_view(), name='editmessage',),
    #delete question
    url(r'^deleteq/(?P<pk>\d+)/$', views.DeleteQuestionView.as_view(), name='deletequestion',),
    #edit choice
    url(r'^editc/(?P<pk>\d+)/$', views.EditChoiceView.as_view(), name='editchoice',),
    #delete choice
    url(r'^deletec/(?P<pk>\d+)/$', views.DeleteChoiceView.as_view(), name='deletechoice',),
	#delete message
    url(r'^deletem/(?P<pk>\d+)/$', views.DeleteMessageView.as_view(), name='deletemessage',),
	#delete event
    url(r'^deleteevent/(?P<pk>\d+)/$', views.DeleteEventView.as_view(), name='delete_event',),
	#vote
    url(r'^(?P<choice_id>[0-9]+)/vote/$', views.vote, name='vote'),

    #creates choice
    #url(r'^addq/(?P<pk>\d+)/$', views.CreateChoiceView.as_view(), name='addchoice',),
    #VOID creates question
    #url(r'^addq/(?P<pk>\d+)/$', views.CreateQuestionView.as_view(), name='addquestion',),
    ]
