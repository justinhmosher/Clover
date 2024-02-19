from Clover import settings
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
import win32com.client as win32
import pythoncom
from . tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
import requests
from decouple import config
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count,F,ExpressionWrapper,fields
from datetime import datetime
from itertools import chain
from collections import defaultdict
from datetime import datetime
from django.utils import timezone
import json

def homepage(request):
	return render(request,"authentication/homepage.html")
