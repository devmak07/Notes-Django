from django.urls import path 
from . import views 

app_name="core"

urlpatterns=[
    # path('',views.index,name='index'),
    path('',views.create,name='create'),
    path('view/',views.view,name='view'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('unlock/<int:pk>',views.unlock_note),
    path('view/unlock/<int:pk>/', views.unlock_note, name='unlock'),
]