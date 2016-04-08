from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'sfgym2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'login.views.home', name='home'),
   #url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^profile/$', 'login.views.profile', name='profile'),
    url(r'^logout/$', 'login.views.logout1', name='logout1'),
    url(r'^members/$', 'login.views.members1', name='members1'),
     url(r'^todaysschedule/$', 'login.views.todaysschedule', name='todaysschedule'),
     url(r'^todaysdiet/$', 'login.views.todaysdiet', name='todaysdiet'),
     url(r'^addoffer/$', 'login.views.addoffer', name='addoffer'),
     url(r'^allmembers/$', 'login.views.allmembers', name='allmembers'),
     url(r'^allinstructors/$', 'login.views.allinstructors', name='allinstructors'),
     url(r'^ldate/$', 'login.views.ldate', name='ldate'),
     url(r'^offers/$', 'login.views.offers', name='offers'),
     url(r'^iprofile/$', 'login.views.iprofile', name='iprofile'),
     url(r'^inventory/$', 'login.views.inventory', name='inventory'),
     url(r'^inventory/showinventory/$', 'login.views.showinventory', name='showinventory'),
     url(r'^inventory/addinventory/$', 'login.views.addinventory', name='addinventory'),
     url(r'^inventory/addinventory/addMachine/$', 'login.views.addMachine', name='addMachine'),
     url(r'^inventory/addinventory/addDumbell/$', 'login.views.addDumbell', name='addDumbell'),
     url(r'^inventory/addinventory/addPlatesAndBar/$', 'login.views.addPlatesAndBar', name='addPlatesAndBar'),
     url(r'^inventory/addinventory/addOtherAccessory/$', 'login.views.addOtherAccessory', name='addOtherAccessory'),
     url(r'^inventory/showinventory/showMachines/$', 'login.views.showMachines', name='showMachines'),
     url(r'^inventory/showinventory/showDumbells/$', 'login.views.showDumbells', name='showDumbells'),
     url(r'^inventory/showinventory/showOtherAccessories/$', 'login.views.showOtherAccessories', name='showOtherAccessories'),
     url(r'^inventory/showinventory/showPlatesAndBars/$', 'login.views.showPlatesAndBars', name='showPlatesAndBars'),
     url(r'^inventory/removeinventory/$', 'login.views.removeinventory', name='removeinventory'),
     url(r'^inventory/removeinventory/removeMachine/$', 'login.views.removeMachine', name='removeMachine'),
     url(r'^inventory/removeinventory/removeDumbell/$', 'login.views.removeDumbell', name='removeDumbell'),
     url(r'^inventory/removeinventory/removePlatesAndBar/$', 'login.views.removePlatesAndBar', name='removePlatesAndBar'),
     url(r'^inventory/removeinventory/removeOtherAccessory/$', 'login.views.removeOtherAccessory', name='removeOtherAccessory'),
     url(r'^persinst/$', 'login.views.persinst', name='persinst'),
   # url(r'^members/(?P<member_name>\w+)/$', 'login.views.assign', name='members1'),
	 url(r'^adduser/$', 'login.views.adduser', name='adduser'),
	 url(r'^adduser/(?P<user_name>[\w{}.-]+)/', 'login.views.addprofile', name='addprofile'),
	 url(r'^members/(?P<user_name>[\w{}.-]+)/$', 'login.views.sched_diet', name='sched_diet'),
	 url(r'^members/(?P<user_name>[\w{}.-]+)/exercise/$', 'login.views.schedule', name='schedule'),
	 url(r'^members/(?P<user_name>[\w{}.-]+)/diet/$', 'login.views.diet', name='diet'),
	 url(r'^allmembers/(?P<user_name>[\w{}.-]+)/$', 'login.views.memberprofile', name='memberprofile'),
	 url(r'^allinstructors/(?P<user_name>[\w{}.-]+)/$', 'login.views.instructorprofile', name='instructorprofile'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.STATIC_URL,document_root=settings.MEDIA_ROOT)