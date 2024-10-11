import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.html import escape
from PIL import Image
from googletrans import Translator
import pytesseract
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return render(request, 'app1/index.html')


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract_text_from_image(image):
    img = Image.open(image)
    text = pytesseract.image_to_string(img, lang="vie")
    return text
 
 
@api_view(['POST']) 
def translate(request):
    if request.method == 'POST':
        data = request.data
        from_language = data.get('from', '')
        to_language = data.get('to', '')

        if 'image' in request.FILES:
            image = request.FILES['image']
            text = extract_text_from_image(image)
            ts = Translator()
            output = ts.translate(text, src=from_language, dest=to_language)
            content = {'input': text, 'output': output.text}
            return Response(content, status=status.HTTP_200_OK)
        
        elif 'input' in data:
            input_text = data['input']

            if not input_text:
                content = {'error': 'Empty input!'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)

            ts = Translator()
            output = ts.translate(input_text, src=from_language, dest=to_language)
            content = {'input': input_text, 'output': output.text}
            return Response(content, status=status.HTTP_200_OK)

    return JsonResponse({'error': 'Unexpected error!'})

            
