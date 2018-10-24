from django.shortcuts import render
from django.views import generic
from storage.models import Category, Item, ItemAction
from django.views.generic import UpdateView, CreateView, DeleteView, DetailView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


# Create your views here.

def test(request):
    return render(request, 'test.html', context=None)

@login_required
# @permission_required('categorys.view_category')
def storage_index(request):
    # if not request.user.is_staff:
        # raise PermissionDenied()
    return render(request, 'storage_index.html', context=None)


# ---------------------------------------------------------------------
# CATEGORY FORM: LIST, DETAIL, CREATE, UPDATE, DELETE
# ---------------------------------------------------------------------

class CategoryList(PermissionRequiredMixin, generic.ListView):
    permission_required = ('storage.view_category',)
    
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


class CategoryDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ('storage.view_category',)

    model = Category
    template_name = "storage/category_detail.html"


class CategoryCreateView(PermissionRequiredMixin, CreateView):

    permission_required = ('storage.add_category',)
    # permission_denied_message = "alibaba"
    def get_permission_denied_message(self):
        return "123-alibaba"

    model = Category
    template_name = "storage/category_form.html"
    fields = '__all__'
    # success_url = reverse_lazy('categories')

    # go to parent detail
    def get_success_url (self):
        pk = self.object.id
        return reverse('category_detail', kwargs={"pk": pk})


class CategoryUpdateView(PermissionRequiredMixin, UpdateView):

    permission_required = ('storage.change_category',)

    model = Category
    template_name = "storage/category_form.html"
    fields = '__all__'
    # success_url = reverse_lazy('categories')
    # def get_success_url(self):
        # previous_url = self.request.POST.get('previous_url', None)
        # return previous_url

    # # return category detail
    # def form_valid(self, form):
    #     # name = form.cleaned_data["name"]
    #     pk = self.get_object().pk
    # return super().form_valid(form)

    # go to parent detail (category-detail)
    def get_success_url (self):
        # pk = self.get_object().pk
        pk = self.object.pk
        return reverse('category_detail', kwargs={"pk": pk})


class CategoryDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ('storage.delete_category',)

    model = Category
    # template_name = "storage/category_confirm_delete.html"
    # success_url = reverse_lazy('categories')

    # def get(self, *args, **kwargs):
    #     return self.post(*args, **kwargs)

    # go to parent detail
    def get_success_url(self):
        # previous_url = self.request.POST.get('previous_url', None)
        # return previous_url
        return reverse_lazy('categories')


# ---------------------------------------------------------------------
# ITEM FORM: LIST, DETAIL, CREATE, UPDATE, DELETE
# ---------------------------------------------------------------------

class ItemList(PermissionRequiredMixin, generic.ListView):

    permission_required = ('storage.view_item',)

    model = Item
    context_object_name = 'item_list'
    template_name = 'storage/item_list.html'
    paginate_by = 10


class ItemDetailView(PermissionRequiredMixin, DetailView):

    permission_required = ('storage.view_item',)

    model = Item
    # print("item: " + model.image)
    template_name = "storage/item_detail.html"


class ItemCreateView(PermissionRequiredMixin, CreateView):

    permission_required = ('storage.add_item',)

    model = Item
    template_name = "storage/item_form.html"
    fields = ['category', 'name', 'image', 'description']
    # fields = '__all__'
    # success_url = reverse_lazy('items')

    # go to parent detail
    def get_success_url(self):
        # Returns None if user came from another website
        # previous_url = self.request.META.get('HTTP_REFERER')
        # print("previous_url >>> " + previous_url)

        category_pk = self.object.category.pk
        return reverse("category_detail", kwargs={"pk": category_pk})


class ItemUpdateView(PermissionRequiredMixin, UpdateView):

    permission_required = ('storage.change_item',)

    model = Item
    template_name = "storage/item_form.html"
    fields = ['category', 'name', 'image', 'description']
    # fields = '__all__'
    # success_url = reverse_lazy('items')

    # go to parent detail
    def get_success_url(self):
        category_pk = self.object.category.pk
        return reverse("category_detail", kwargs={"pk": category_pk})


class ItemDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ('storage.delete_item',)

    model = Item
    # template_name = "storage/item_confirm_delete.html"
    # success_url = reverse_lazy('items')

    # go to parent detail
    def get_success_url(self):
        category_pk = self.object.category.pk
        return reverse("category_detail", kwargs={"pk": category_pk})


# ---------------------------------------------------------------------
# ITEMACTION FORM: LIST, DETAIL, CREATE, UPDATE, DELETE
# ---------------------------------------------------------------------

class ItemActionList(PermissionRequiredMixin, generic.ListView):

    permission_required = ('storage.view_itemaction',)

    model = ItemAction
    context_object_name = 'itemaction_list'
    template_name = 'storage/itemaction_list'
    paginate_by = 10


class ItemActionCreateView(PermissionRequiredMixin, CreateView):

    permission_required = ('storage.add_itemaction',)

    model = ItemAction
    fields = ['date', 'item', 'status', 'price', 'quantity']
    # fields = '__all__'
    template_name = "storage/itemaction_form.html"
    # success_url = reverse_lazy('itemactions')

    # go to parent detail
    def get_success_url(self):
        item_pk = self.object.item.pk
        return reverse("item_detail", kwargs={"pk": item_pk})


class ItemActionUpdateView(PermissionRequiredMixin, UpdateView):

    permission_required = ('storage.change_itemaction',)

    model = ItemAction
    fields = ['date', 'item', 'status', 'price', 'quantity']
    # fields = '__all__'
    template_name = "storage/itemaction_form.html"
    # success_url = reverse_lazy('itemactions')

    # go to parent detail
    def get_success_url(self):
        item_pk = self.object.item.pk
        return reverse("item_detail", kwargs={"pk": item_pk})


class ItemActionDeleteView(PermissionRequiredMixin, DeleteView):

    permission_required = ('storage.delete_itemaction',)

    model = ItemAction
    template_name = "storage/itemaction_confirm_delete.html"
    # success_url = reverse_lazy('itemactions')

    # go to parent detail
    def get_success_url(self):
        item_pk = self.object.item.pk
        return reverse("item_detail", kwargs={"pk": item_pk})
