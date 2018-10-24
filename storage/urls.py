from django.urls import path
from storage import views
from django.conf import settings
from django.conf.urls.static import static


# storage url
urlpatterns = [
    path('', views.storage_index, name='storage_index'),
    path('test/', views.test, name='test'),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('items/', views.ItemList.as_view(), name='items'),
    path('itemactions/', views.ItemActionList.as_view(), name='itemactions'),
]


# category url
urlpatterns += [
    path('category/create/', views.CategoryCreateView.as_view(),
         name='category_create'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(),
         name='category_update'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(),
         name='category_delete'),
    path('category/<int:pk>/detail', views.CategoryDetailView.as_view(), 
         name='category_detail'),
]


# item url
urlpatterns += [
    path('item/create/', views.ItemCreateView.as_view(),
         name='item_create'),
    path('item/<int:pk>/update', views.ItemUpdateView.as_view(),
         name='item_update'),
    path('item/<int:pk>/delete', views.ItemDeleteView.as_view(),
         name='item_delete'),
    path('item/<int:pk>/detail', views.ItemDetailView.as_view(),
         name='item_detail'),
]


# itemaction url
urlpatterns += [
    path('itemaction/create/', views.ItemActionCreateView.as_view(),
         name='itemaction_create'),
    path('itemaction/<slug:pk>/update', views.ItemActionUpdateView.as_view(),
         name='itemaction_update'),
    path('itemaction/<slug:pk>/delete', views.ItemActionDeleteView.as_view(),
         name='itemaction_delete'),
]
