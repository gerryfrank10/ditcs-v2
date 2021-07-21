from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt
from rest_framework import viewsets
import io, base64
from rest_framework import viewsets
from .models import Junction, Traffic, Road, Light,Junction
from .serializers import TrafficSerializer, RoadSerializer, LightSerializer
from .forms import CreatePersonForm, RoadsForm
import requests

# Create your views here.
def index(request):

    # Draw a figure for tests
    fig, ax = plt.subplots()
    ax.plot([1,2,3,4], [4,2,1,4])
    # ax.set_title("Test plots from dummy data")
    
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()

    flike = io.BytesIO()
    ch, jf = plt.subplots()
    students = [22,33,12]
    langs = ["C++", "Java", "Python"]
    jf.pie(students, labels=langs)
    ch.savefig(flike)
    pie = base64.b64encode(flike.getvalue()).decode()

    context = {'chart': b64, 'pie': pie}

    return render(request, 'index.html', context=context)

def camera(request):

    context = {}
    return render(request, 'camera.html',context)

def roads(request):
    result = []
    # form = RoadsForm()
   
    
    if request.method == 'POST':    
        state= request.POST
        if 'road_a' in state:
            result.append(request.POST['road_a'])
            print(f'{result} ')
        else:
             result.append('off')
        
        if (request.POST['road_id'] == '1'):
            sname= 'Road A'
        elif(request.POST['road_id'] == '2'): 
            sname= 'Road B'
        elif(request.POST['road_id'] == '3'): 
            sname= 'Road C' 
        elif(request.POST['road_id'] == '4'): 
            sname= 'Road D'         
        elif(request.POST['road_id'] == '5'): 
            sname= 'Road E' 
        elif(request.POST['road_id'] == '6'): 
            sname= 'Road F' 
        elif(request.POST['road_id'] == '7'): 
            sname= 'Road G' 
            
        rId=request.POST['road_id']
        rd = Junction.objects.get(pk=int(rId))
        rd.name = sname
        rd.state = result[0]
        rd.save()
    roads = Junction.objects.all()
    x = {'name': rd.name, 'state': rd.state}
    requests.post('http://127.0.0.1:8000/api', data=x)
    print(x)
    context = {'data':roads}
    return render(request, 'roads.html',context)

def profile(request):

    context = {}
    return render(request, 'profile.html',context)

class TrafficViewSet(viewsets.ModelViewSet):
    queryset = Traffic.objects.all()
    serializer_class = TrafficSerializer

class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class LightViewSet(viewsets.ModelViewSet):
    queryset = Light.objects.all()
    serializer_class = LightSerializer

def maps(request):
    
    context = {}
    return render(request, 'maps.html', context)

def login(request):
    
    context = {}
    return render(request, 'login.html', context)

def forgot_password(request):
    
    context = {}
    return render(request, 'forgot-password.html', context)

def register(request):
    form = CreatePersonForm()
    if request.method == 'POST':
        form = CreatePersonForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register.html', context)
