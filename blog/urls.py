from django.urls import path # Yönlendirme işlemi için gerekli import
from . import views # Yönlendirme views'in içinde import et 

urlpatterns = [
    path('', views.post_list, name='post_list'), # path(yönlenecek şeyler, view belirt, name)
]