from django.urls import path
from basic_app import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('', views.index, name="index"),
    path('other', views.other, name="other"),
    path('relative', views.relative_url_templates, name="relative"),
]
