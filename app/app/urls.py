from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.home'),
    url(r'^programa/', 'app.views.schedule'),
    url(r'^charlistas/', 'app.views.speakers'),
    url(r'^talleres/', 'app.views.workshops'),
    url(r'^colaboradores/', 'app.views.sponsors'),
    url(r'^prensa/', 'app.views.press'),
    url(r'^formulario/', 'app.views.attendee_form'),
    url(r'^recursos/', 'app.views.resources'),

    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^app/', include('app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    pass

