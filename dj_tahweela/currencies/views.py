from rest_framework.views import APIView
from rest_framework.response import Response

class ServerStatusView(APIView):
    def get(self, request):
        return Response({'Status': 'Currencies App Up!'})