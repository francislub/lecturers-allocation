from django.shortcuts import render, reverse, redirect
# from client.models import Voter, Position, Candidate, Votes
from account.models import CustomUser
from account.forms import CustomUserForm
# from client.forms import *
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.conf import settings

def dashboard(request):
    return render(request, "admin/dashboard.html")

def reqStatus(request):
    return render(request, "admin/reqStatus.html")

def reportStatus(request):
    return render(request, "admin/reportStatus.html")