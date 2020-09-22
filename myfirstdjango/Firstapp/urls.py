from django.conf.urls import url
from Firstapp import views
from django.conf import settings
from django.conf.urls.static import static # new
app_name = "Firstapp"

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^users/',views.users,name='users'),
    url('^formpage/',views.user,name = "form_name"),
    url('^relative/',views.relative,name = "relative"),
    url("^register/",views.register,name ="register"),
    url("^user_login/$",views.user_login,name="user_login"),
    url("^other/",views.other,name="other")]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

