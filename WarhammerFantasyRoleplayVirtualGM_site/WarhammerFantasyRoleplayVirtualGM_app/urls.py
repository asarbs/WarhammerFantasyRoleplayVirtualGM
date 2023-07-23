from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addUser", views.addUser, name="addUser"),
    path('changePassword', views.changePassword, name="changePassword"),
    path('addUserConfirm', views.addUserConfirm, name="addUserConfirm"),
    path('editPlayer/(?P<pk>\d+)/',  views.UpdatePlayer.as_view(success_url="/"), name='updatePlayer'),
    path('remindPassword', views.RemindPassword, name="RemindPassword")
]