from django.conf.urls import url
from freelance import views
urlpatterns=[
    url(r'^$', views.index, name="Главная"),
    url(r'^create_order/$', views.create_order, name="Оформление заказа"),
    url(r'^create_order/save/$', views.save_order, name="Оформление заказа"),
    url(r'^login/$', views.login, name="Вход"),
    url(r'^login/check/$', views.login_check, name="Вход"),
    url(r'^register/$', views.register, name="Регистрация"),
    url(r'^register/new-user/$', views.register_create_user, name="Регистрация"),

]
