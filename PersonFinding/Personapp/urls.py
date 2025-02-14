from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('Stationregister',views.Stationregister,name='Stationregister'),
    path('Hospitalregister',views.Hospitalregister,name='Hospitalregister'),
    path('Userregister',views.Userregister,name='Userregister'),
    path('Stationlog',views.Station_list_view,name='Stationlog'),
    path('Hospitallog',views.Hospital_list_view,name='Hospitallog'),
    path('Userlog',views.User_list_view,name='Userlog'),
    path('user_edit/<int:id>/',views.user_edit,name='user_edit'),
    path('logins',views.custom_login_view,name='logins'),
    path('userhome',views.userhome,name='userhome'),
    path('stationhome',views.stationhome,name='stationhome'),
    path('hospitalhome',views.hospitalhome,name='hospitalhome'),
    path('userhomeprofile',views.userhomeprofile,name='userhomeprofile'),
    path('stationhomeprofile',views.stationhomeprofile,name='stationhomeprofile'),
    path('hospitalhomeprofile',views.hospitalhomeprofile,name='hospitalhomeprofile'),
    path('stationsearch',views.stationsearch,name='stationsearch'),
    path('hospitalsearch',views.hospitalsearch,name='hospitalsearch'),
    path('missingregister',views.missform,name='missingregister'),
    path('table/',views.user_list_view,name='table'),
    path('user_delete/<int:id>/',views.user_delete,name='user_delete'),
    path('user_edit/<int:id>/',views.user_edit,name='user_edit'),
    path('station_missing_details',views.station_missing_details,name='station_missing_details'),
    path('missing_list_view',views.missing_list_view,name='missing_list_view'),
    path('create_complaint',views.create_complaint,name='create_complaint'),
    path('ListComplaints',views.ListComplaints,name='ListComplaints'),
    path('DeleteComplaint/<int:id>/',views.DeleteComplaint,name='DeleteComplaint'),
    path('EditComplaint/<int:id>/',views.EditComplaint,name='EditComplaint'),
    path('ViewComplaints',views.ViewComplaints,name='ViewComplaints'),
    path('ComplaintReply/<int:id>/',views.ComplaintReply,name='ComplaintReply'),
    path('ShowReply/<int:id>/',views.ShowReply,name='ShowReply'),
    path('accidentregform',views.accidentregform,name='accidentregform'),
    path('ListAccident',views.ListAccident,name='ListAccident'),
    path('accident_edit/<int:id>/',views.accident_edit,name='accident_edit'),
    path('accident_delete/<int:id>/',views.accident_delete,name='accident_delete'),
    path('station_accidents', views.station_accidents, name='station_accidents'),
    path('station/enquiry/<int:station_id>/', views.station_enquiry, name='station_enquiry'),
     path('station/enquiries/', views.station_enquiries_list, name='station_enquiries_list')
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

