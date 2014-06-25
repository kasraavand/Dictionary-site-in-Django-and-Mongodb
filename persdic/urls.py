from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$','persdicapp.views.main_page'),
    (r'^register/$', 'persdicapp.views.register_page'),
    (r'^register/success/$', TemplateView.as_view(template_name="registration/success.html")),
    (r'^login/$','persdicapp.views.login'),
    (r'^loggedin/$','persdicapp.views.loggedin'),
    # Examples:
    #url(r'^$', 'persdic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
