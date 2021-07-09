from django.conf.urls import url
from . import views
from django.urls import path

# urlpatterns= [
#     url(r'^$', views.index, name='index'),
#     url(r'^create$', views.create, name='create'),
#     url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
#     url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
#     url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

#     # path('doituyen/', admin.site.urls),
# ]

urlpatterns = [
    # path('', views.index, name='index'),
    path('crud/', views.index, name='index'),
    
    path('bang/create', views.doituyen_create, name='doituyen_create'),
    path('bang/edit/<str:id>', views.doituyen_edit, name='doituyen_edit'),
    path('bang/edit/update/<str:id>', views.doituyen_update, name='doituyen_update'),
    path('bang/delete/<str:bang>/<str:id>', views.doituyen_delete, name='doituyen_delete'),
    path('bang/<str:bang>', views.doituyen, name='doituyen'),

    path('cauthu/create', views.cauthu_create, name='cauthu_create'),
    path('cauthu/<str:doituyen>', views.cauthu, name='cauthu'),
    path('cauthu/delete/<str:doituyen>/<str:id>', views.cauthu_delete, name='cauthu_delete'),
    # path('cauthu/<str:doituyen>/add', views.cauthu, name='cauthu'),
    path('cauthu/edit/<str:doituyen>/<str:id>', views.cauthu_edit, name='cauthu_edit'),
    path('cauthu/update/<str:doituyen>/<str:id>', views.cauthu_update, name='cauthu_update'),

    path('lich-thi-dau/', views.lichthidau, name='lichthidau'),
    path('lich-thi-dau/create', views.lichthidau_create, name='lichthidau_create'),
    path('lich-thi-dau/edit/<str:id>', views.lichthidau_edit, name='lichthidau_edit'),
    path('lich-thi-dau/update/<str:id>', views.lichthidau_update, name='lichthidau_update'),
    path('lich-thi-dau/delete/<str:id>', views.lichthidau_delete, name='lichthidau_delete'),
    
    path('phan-tich/tuoi-trung-binh', views.tuoitrungbinh, name='tuoitrungbinh'),
    path('phan-tich/chieu-cao-trung-binh', views.chieucaotrungbinh, name='chieucaotrungbinh'),

    # path('doituyen/', views.doituyen, name='doituyen'),
    # path('doituyen/create', views.doituyen_create, name='doituyen_create'),
    # path('doituyen/edit/<str:id>', views.doituyen_edit, name='doituyen_edit'),
    # path('doituyen/edit/update/<str:id>', views.doituyen_update, name='doituyen_update'),
    # path('doituyen/delete/<str:id>', views.doituyen_delete, name='doituyen_delete'),

    # url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),

    # path('doituyen/update/(?P<id>\d+)$', views.doituyen_update, name='doituyen_update'),

    # path('products/', views.products, name='products'),
    # path('customer/<str:pk_test>/', views.customer, name="customer"),

    # path('create_order/', views.createOrder, name="create_order"),
    # path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    # path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]