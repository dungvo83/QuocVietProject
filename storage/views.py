from django.shortcuts import render
from django.views import generic
from storage.models import Category, Item, ItemAction
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy


# Create your views here.

def test(request):
    return render(request, 'test.html', context=None)


def storage_index(request):
    return render(request, 'storage_index.html', context=None)


class CategoryList(generic.ListView):
    model = Category
    context_object_name = 'category_list'
    template_name = 'storage/category_list.html'
    paginate_by = 10

    # def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context["aaa"] = 123
    #    return context

    # def get_queryset(self):
    #    return Category.objects.all()


class ItemDetailView(DetailView):
    model = Item
    template_name = "storage/item_detail.html"


class ItemList(generic.ListView):
    model = Item
    context_object_name = 'item_list'
    template_name = 'storage/item_list.html'
    paginate_by = 10


class ItemActionList(generic.ListView):
    model = ItemAction
    context_object_name = 'itemaction_list'
    template_name = 'storage/itemaction_list'
    paginate_by = 10


# ----------------------------------------------
# CATEGORY FORM: DETAIL, CREATE, UPDATE, DELETE
# ----------------------------------------------


class CategoryDetailView(DetailView):
    model = Category
    template_name = "storage/category_detail.html"


class CategoryCreateView(CreateView):
    model = Category
    template_name = "storage/category_form.html"
    fields = '__all__'
    success_url = reverse_lazy('categories')


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "storage/category_form.html"
    fields = '__all__'
    success_url = reverse_lazy('categories')


class CategoryDeleteView(DeleteView):
    model = Category

    # template_name = "storage/category_confirm_delete.html"
    success_url = reverse_lazy('categories')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

    # def get_success_url(self):
    #    return reverse('categories')

    # template_name = "storage/category_confirm_delete.html"
    success_url = reverse_lazy('categories')


# ----------------------------------------------
# ITEM FORM: CREATE, UPDATE, DELETE
# ----------------------------------------------


class ItemCreateView(CreateView):
    model = Item
    template_name = "storage/item_form.html"
    fields = '__all__'
    success_url = reverse_lazy('items')


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "storage/item_form.html"
    fields = '__all__'
    success_url = reverse_lazy('items')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = "storage/item_confirm_delete.html"
    success_url = reverse_lazy('items')


# ----------------------------------------------
# ITEMACTION FORM: CREATE, UPDATE, DELETE
# ----------------------------------------------
class ItemActionCreateView(CreateView):
    model = ItemAction
    fields = '__all__'
    template_name = "storage/itemaction_form.html"
    success_url = reverse_lazy('itemactions')


class ItemActionUpdateView(UpdateView):
    model = ItemAction
    fields = '__all__'
    template_name = "storage/itemaction_form.html"
    success_url = reverse_lazy('itemactions')


class ItemActionDeleteView(DeleteView):
    model = ItemAction
    template_name = "storage/itemaction_confirm_delete.html"
    success_url = reverse_lazy('itemactions')
