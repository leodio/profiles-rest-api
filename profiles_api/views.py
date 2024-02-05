from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        an_apiview = [
            'Uses HTTP  methods as function (get, post, etc.) ',
            'Similar to Django View',
            'Gives you the most control over your app logic'
        ]
    
        return Response({'message':'Hello!', 'an_apiview': an_apiview})