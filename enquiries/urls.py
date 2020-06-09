#These are our routes:
# /api/enquiries: GET, POST, DELETE
# /api/enquiries/:id: GET, PUT, DELETE
# /api/enquiries/published: GET

from django.conf.urls import url
from enquiries import views

urlpatterns = [
    url(r'^api/enquiries$', views.enquiry_list),
    url(r'^api/enquiries/(?P<pk>[0-9]+)$', views.enquiry_detail)
]
