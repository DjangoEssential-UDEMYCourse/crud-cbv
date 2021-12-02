from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView,DeleteProdutoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add-produto/', CreateProdutoView.as_view(), name='add-produto'),
    path('produto/<int:pk>/update', UpdateProdutoView.as_view(), name='update-produto'),
    path('produto/<int:pk>/delete', DeleteProdutoView.as_view(), name='delete-produto'),

]