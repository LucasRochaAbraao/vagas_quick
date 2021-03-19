from django.urls import path
from .views import VagaList, VagaDetail, VagaCreate, VagaUpdate, CustomDeleteView, CustomLoginView, VagasApi
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('vagas/', VagasApi.as_view(), name='vagas_api'),

    path('', VagaList.as_view(), name='vagas'),
    path('vaga/<int:pk>/', VagaDetail.as_view(), name='vaga'),
    path('criar-vaga/', VagaCreate.as_view(), name='vaga-create'),
    path('atualizar-vaga/<int:pk>/', VagaUpdate.as_view(), name='vaga-update'),
    path('deletar-vaga/<int:pk>/', CustomDeleteView.as_view(), name='vaga-delete'),
]
