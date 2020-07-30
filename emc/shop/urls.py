from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="HomePage"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productview, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("privacy/", views.privacypolicy, name="PrivacyPolicy"),
    path("terms/", views.termscondition, name="Terms&Condition"),
    path("ultra/", views.ultra, name="Ultra"),
    path("ultracatridges/", views.ultracartridges, name="UltraCartridges"),
    path("neo/", views.neo, name="Neo"),
    path("neocartridges/", views.neocartridges, name="NeoCartridges"),
    path("productdetails0/", views.productdetails0, name="ProductDetails0"),
    path("productdetails1/", views.productdetails1, name="ProductDetails1"),
    path("productdetails2/", views.productdetails2, name="ProductDetails2"),
    path("productdetails3/", views.productdetails3, name="ProductDetails3"),
    path("productdetails4/", views.productdetails4, name="ProductDetails4"),
    path("productdetails5/", views.productdetails5, name="ProductDetails5"),
    path("productdetails6/", views.productdetails6, name="ProductDetails6"),
    path("productdetails7/", views.productdetails7, name="ProductDetails7"),
    path("productdetails8/", views.productdetails8, name="ProductDetails8"),
    path("productdetails9/", views.productdetails9, name="ProductDetails9"),
    path("productdetails10/", views.productdetails10, name="ProductDetails10"),
    path("productdetails11/", views.productdetails11, name="ProductDetails11"),
    path("productdetails12/", views.productdetails12, name="ProductDetails12"),
    path("productdetails13/", views.productdetails13, name="ProductDetails13"),
    path("productdetails14/", views.productdetails14, name="ProductDetails14"),
    path("productdetails15/", views.productdetails15, name="ProductDetails15"),
    path("productdetails16/", views.productdetails16, name="ProductDetails16"),
    path("productdetails17/", views.productdetails17, name="ProductDetails17"),
    path("productdetails18/", views.productdetails18, name="ProductDetails18"),
    path("productdetails19/", views.productdetails19, name="ProductDetails19"),
    path("productdetails20/", views.productdetails20, name="ProductDetails20"),
    path("productdetails21/", views.productdetails21, name="ProductDetails21"),
    path("productdetails22/", views.productdetails22, name="ProductDetails22"),
    path("productdetails23/", views.productdetails23, name="ProductDetails23"),
    path("cart/", views.cart, name="Cart")
]