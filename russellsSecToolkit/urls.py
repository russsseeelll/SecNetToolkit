from django.contrib import admin
from django.urls import path
from scanner.views import index
from scanner.views import run_scan

urlpatterns = [
    path("", index, name="index"),  # Main page
    path("run-scan/", run_scan, name="run_scan"),  # AJAX scan endpoint
]

