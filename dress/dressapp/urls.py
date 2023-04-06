from django.urls import path
from . import views
app_name='dressapp'
urlpatterns = [

    path('',views.dress,name='dress'),
    path('dress/<int:dress_id>/',views.product,name='product'),
    path('add/',views.add_dress,name='add_dress'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]