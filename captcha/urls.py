from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('captcha.views',
    url(r'image/(?P<key>\w+)/$', 'captcha_image', name='captcha-image'),
    url(r'audio/(?P<key>\w+)/$', 'captcha_audio', name='captcha-audio'),
    url(r'ajax_reload/$', 'captcha_ajax_reload', name='captcha-ajax-reload'),
)
