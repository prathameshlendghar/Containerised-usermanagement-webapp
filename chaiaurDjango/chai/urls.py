
from django.urls import path
from . import views

urlpatterns = [
    path('', views.func1, name='func1'),
    path('func2', views.func2, name='func2'),
    path('renderHtml/',views.renderIndex, name='renderHtml'),
    path('rendNestHtml/',views.rendNestHtml, name='renderNestHtml')
]
