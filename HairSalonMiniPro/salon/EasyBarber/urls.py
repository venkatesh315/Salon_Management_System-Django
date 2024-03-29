from django.urls import path
from . import views
from .views import render_pdf_view
# app_name='payment'

urlpatterns=[
    path('home',views.welcome,name='home'),
    path('owner_signup',views.owner_signup,name='fos'),
    path('cust_signup',views.cust_signup,name='fcs'),
    path('about_us',views.about_us,name='about'),
    path('cust_pass',views.register_cust,name='cust_pass'),
    path('own_pass',views.register_owner,name='own_pass'),
    path('shop_names',views.list_of_shops,name='store'),
    path('bookings',views.display_booked,name='display_booked'),
    path('reviews', views.my_reviews, name='reviews'),
    path('feedbacks',views.display_feedbacks,name='display_feedbacks'),
    path('appointment',views.my_appointments,name='schedule'),
    path('online_payment',views.pay_now, name='amount'),
    path('paidpdf',render_pdf_view,name="pay_view"),


]
