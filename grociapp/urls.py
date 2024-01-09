from django.urls import path
from . import views

urlpatterns = [
    path('', views.func,name='func'),
    path('/home',views.home,name='home'),
    path('/about/',views.about,name='about'),
    path('/contact/',views.contact,name='contact'),

    path('/p1/',views.p1,name='p1'),
    path('/p2/',views.p2,name='p2'),
    path('/p3/',views.p3,name='p3'),
    path('/p4/',views.p4,name='p4'),
    path('/p5/',views.p5,name='p5'),
    path('/p6/',views.p6,name='p6'),
    path('/p7/',views.p7,name='p7'),

    path('/vegetables/',views.vegetables,name='vegetables'),
    path('/fruits/',views.fruits,name='fruits'),
    path('/spices/',views.spices,name='spices'),
    path('/pulses/',views.pulses,name='pulses'),
    path('/utensiles/',views.utensiles,name='utensiles'),
    path('/disinf/',views.disinf,name='disinf'),
    path('/milks/',views.milks,name='milks'),
    path('/biscuits/',views.biscuits,name='biscuits'),
    path('/drinks/',views.drinks,name='drinks'),
    path('/noodles/',views.noodles,name='noodles'),
    


    # path('/signup/',views.signup,name='signup'),


    path('/signup/',views.handleSignup,name='handleSignup'),



]