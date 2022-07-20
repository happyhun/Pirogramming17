from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('post/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('tool/list/', views.tool_list, name="tool_list"),
    path('tool/create/', views.tool_create, name="tool_create"),
    path('tool/post/<int:id>', views.tool_detail, name="tool_detail"),
    path('tool/update/<int:id>', views.tool_update, name="tool_update"),
    path('tool/delete/<int:id>', views.tool_delete, name="tool_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)