from rest_framework import viewsets
from .models import ReactionTime, MyModel
from .serializers import ReactionTimeSerializer, MyModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .data import data_collector


class ReactionTimeViewSet(viewsets.ModelViewSet):
    queryset = ReactionTime.objects.all()
    serializer_class = ReactionTimeSerializer


class ReactionTimeAPIView(APIView):
    def get(self, request):

        url = 'http://localhost:3000/api/rt/'
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json().get('data')

            serializer = ReactionTimeSerializer(data=data, many=True)

            if serializer.is_valid():
                serializer.save()  # Save the objects to the database
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

class MyView(APIView):
    def get(self, request):
        my_models = MyModel.objects.all()
        serializer = MyModelSerializer(my_models, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def fetch_reaction_times_data():
    view = ReactionTimeAPIView()
    request = None  # You can pass a request object if needed
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

