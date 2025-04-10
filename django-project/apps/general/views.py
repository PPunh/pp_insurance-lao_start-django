# coding=utf-8
from django.shortcuts import render
import qrcode
from io import BytesIO
from django.http import HttpResponse
import qrcode.constants
import base64



def home(request):

    context = {
        'title': 'Home',
    }
    template_name = 'general/home.html'
    return render(request, template_name, context)

def generate_qr(request):
    img_data = None
    if request.method == 'POST':
        data = request.POST.get('data')
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", bacjk_color="white"),
        img_io = BytesIO()
        img[0].save(img_io, 'PNG')
        img_io.seek(0)


        #Convert to base64 for showing in HTML
        img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
        img_data = f'data:image/png;base64, {img_base64}'

    context = {
        'title':'Generate QR Code',
        'img_data': img_data,
    }
    template_name = 'general/generate_qr.html'
    return render(request, template_name, context)



def contact_us(request):
    
    context = {
        'title':'Contact US'
    }
    template_name = 'general/contact_us.html'
    return render(request, template_name, context)


def about_us(request):

    context = {
        'title': 'About US'
    }
    template_name = 'general/about_us.html'
    return render(request, template_name, context)