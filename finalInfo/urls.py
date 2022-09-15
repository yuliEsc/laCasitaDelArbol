from django.urls import re_path as url
from django.contrib import admin
from django.urls import path
from apps.contactos import views, urls
from apps.usuarios_app import views as viewsUsers
from apps.noticias_app import views as viewsNotice
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewsNotice.index, name='index'),
    path('noticias', viewsNotice.notices, name='notices'),
    path('noticia/<int:id>', viewsNotice.noticeDetail, name='Noticia'),
    path('nosotros', viewsNotice.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro', viewsUsers.register, name='registro'),
    path('login', LoginView.as_view(template_name='perfiles/login.html'), name='login'),
    path('comentarios/<int:id>', viewsNotice.commentAproved, name='comentAproved'),
    path('logout', LogoutView.as_view(template_name='perfiles/logout.html'), name='logout'),
    path('categoria/<int:id>', viewsNotice.categoriaDetail, name='Categoria'),
    path('proyectos', viewsNotice.proyectos, name='proyectos'),
    path('donar', viewsNotice.donar, name='donar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
