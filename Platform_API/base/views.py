from rest_framework import viewsets
from .models import ReactionTime
from .serializers import ReactionTimeSerializer, GameSerializer, MemorySerializer, AmpSerializer, HandEyeSerializer, \
    SimonTaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from Platform_API.Auth.login_get_token import login_and_retrieve_token

class ReactionTimeViewSet(viewsets.ModelViewSet):
    queryset = ReactionTime.objects.all()
    serializer_class = ReactionTimeSerializer

class ReactionTimeAPIView(APIView):
    def get(self, request):
        email = 'user@gmail.com'
        password = 'user123456'

        token = login_and_retrieve_token(email, password)
        url = 'http://localhost:3000/api/rt/'
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            data = response.json().get('data')
            print(data)
            serializer = ReactionTimeSerializer(data=data, many=True)

            if serializer.is_valid():

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        serializer = ReactionTimeSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemoryAPIView(APIView):
    def get(self, request):
        email = 'user@gmail.com'
        password = 'user123456'

        token = login_and_retrieve_token(email, password)
        url = 'http://localhost:3000/api/memory/'
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            serializer = MemorySerializer(data=data, many=True)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AmpAPIView(APIView):
    def get(self, request):
        email = 'user@gmail.com'
        password = 'user123456'

        token = login_and_retrieve_token(email, password)
        url = 'http://localhost:3000/api/apm/'  # Adjust the endpoint as needed
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            serializer = AmpSerializer(data=data, many=True)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class HandEyeAPIView(APIView):
    def get(self, request):
        email = 'user@gmail.com'
        password = 'user123456'

        token = login_and_retrieve_token(email, password)
        url = 'http://localhost:3000/api/handeye/'  # Adjust the endpoint as needed
        headers = {'Authorization': f'Bearer {token}'}

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            serializer = HandEyeSerializer(data=data, many=True)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SimonTaskAPIView(APIView):
    def get(self, request):
        email = 'user@gmail.com'
        password = 'user123456'

        token = login_and_retrieve_token(email, password)
        headers = {'Authorization': f'Bearer {token}'}
        url = 'http://localhost:3000/api/simonTask'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            serializer = SimonTaskSerializer(data=data, many=True)

            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class GameAPIView(APIView):
    def get(self, request):
        email = 'user@gmail.com'
        password = 'user123456'

        token = login_and_retrieve_token(email, password)
        headers = {'Authorization': f'Bearer {token}'}
        url = 'http://localhost:3000/api/gameStats/'

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json().get('data')
            serializer = GameSerializer(data=data, many=True)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def fetch_reaction_times_data():
    view = ReactionTimeAPIView()
    request = None
    return view.get(request)

    """ 
       if response.status_code == 200:

            data = response.json().get('data')

            serializer = ReactionTimeSerializer(data=data, many=True)

            #data_collector.save_data_to_excel(data, 'base/files/reaction_times.xlsx')
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        """

