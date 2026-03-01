from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
import pickle
import numpy as np
import os

# Carregar modelo (Singleton)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(BASE_DIR, 'ia_models.pkl'), 'rb') as f:
    AI_MODELS = pickle.load(f)

def index(request): return render(request, 'index.html')

class PredictAPI(APIView):
    def post(self, request):
        style = request.data.get('style')
        grades = request.data.get('grades')

        fmt_id = AI_MODELS['tree'].predict([np.array(style)])[0]
        formats = {0: "Vídeo Aulas", 1: "Podcast", 2: "Bootcamp"}

        topic_id = AI_MODELS['knn'].predict([np.array(grades)])[0]
        topics = {0: "Python Avançado", 1: "UX/UI Design", 2: "Gestão Ágil"}

        return Response({"format": formats.get(fmt_id), "topic": topics.get(topic_id)})