from django.conf.urls import url
from ckdApp import views
from django.urls import path

app_name = 'ckdApp'

urlpatterns = [
    path('', views.dataUploadView.as_view(), name = 'ckd'),
    #path('whats', views.WhatsappAnalaysis.as_view(), name = 'whats'),
    #path('result', views.finalresult.as_view(), name= 'result'),
    #path('success', views.Success.as_view(), name = 'success'),
    #path('fail',views.Failure.as_view(),name='fail'),
    #path('filenot',views.FileNotfound.as_view(), name='filenot'),
    #path('aboutus',views.AboutUs.as_view(), name='aboutus')
]
