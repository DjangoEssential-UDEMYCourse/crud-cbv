from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto


class IndexView(ListView):
    models = Produto
    template_name = 'index.html'
    queryset = Produto.objects.all()
    # context_object_name = 'produtos'
    paginate_by = 3
    ordering = 'id'


class CreateProdutoView(CreateView):
    model = Produto
    template_name = 'produto.form.html'
    fields = ['nome', 'preco', 'descricao']
    success_url = reverse_lazy('index')


class UpdateProdutoView(UpdateView):
    model = Produto
    template_name = 'produto.form.html'
    fields = ['nome', 'preco', 'descricao']
    success_url = reverse_lazy('index')


class DeleteProdutoView(DeleteView):
    model = Produto
    template_name = 'produto.delete.html'
    success_url = reverse_lazy('index')
