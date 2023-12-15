from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
import os
import openai

openai.api_key_path = "openAiKey.txt"
openai.api_key = os.getenv("put your ai key here ")

class AiController:
    @staticmethod
    def main(request):
        if request.method == 'POST':
            prompt = request.POST.get('prompt')
            if prompt is not None:
                if prompt != '':

                
                    
                        prompt +='?'
                        response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant."},
                            {"role": "user", "content": prompt},
                        ],
                         
                        )
                        result = {"content":response['choices'][0]['message']['content'],"role":"chat"}
                        return JsonResponse({"data": result}, safe=False)

        return JsonResponse({"error": "Invalid request"}, status=400)

