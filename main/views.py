from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from placeignatius.main.models import PlaceImage
from PIL import Image

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def place(request,width,height):
    image = PlaceImage.fetch_image(width,height)
    img = Image.open(image.image.path)
    response = HttpResponse(mimetype="image/png")
    img.save(response,'PNG')
    return response
    
    
    
    
