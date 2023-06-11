from django.shortcuts import render
from django.http import JsonResponse
from .chatbot import Chatbot

chatbot = Chatbot()

def index(request):
    return render(request, 'chat.html')

def send_message(request):
    user_input = request.GET.get('message')
    response = chatbot.process_input(user_input)
    return JsonResponse({'message': response})
