from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from placeignatius.main.models import PlaceImage
from PIL import Image

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def place(request,width,height):
    size = (int(width),int(height))

    #Returns an image that will look ok when resized to width and height
    image = PlaceImage.fetch_image(width,height)
    img = Image.open(image.image.path)
    img.thumbnail(size,Image.ANTIALIAS)
    response = HttpResponse(mimetype="image/png")
    img.save(response,'PNG')
    return response
    
    
    
    
