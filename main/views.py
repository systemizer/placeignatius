from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from placeignatius.main.models import PlaceImage
from PIL import Image
import PIL

def index(request):
    return render_to_response("index.html",{},RequestContext(request))

def place(request,width,height):
    size = (int(width),int(height))

    #Returns an image that will look ok when resized to width and height
    image = PlaceImage.fetch_image(width,height)
    img = Image.open(image.image.path)

    src_width, src_height = img.size
    src_ratio = float(src_width) / float(src_height)
    dst_width, dst_height = int(width), int(height)
    dst_ratio = float(dst_width) / float(dst_height)

    if dst_ratio < src_ratio:
        crop_height = src_height
        crop_width = crop_height * dst_ratio
        x_offset = int(float(src_width - crop_width) / 2)
        y_offset = 0
    else:
        crop_width = src_width
        crop_height = crop_width / dst_ratio
        x_offset = 0
        y_offset = int(float(src_height - crop_height) / 3)

    img = img.crop((x_offset, y_offset, x_offset+int(crop_width), y_offset+int(crop_height)))
    img = img.resize((int(dst_width), int(dst_height)), Image.ANTIALIAS)

    response = HttpResponse(mimetype="image/png")
    img.save(response,'PNG')
    return response
    
    
    
    
