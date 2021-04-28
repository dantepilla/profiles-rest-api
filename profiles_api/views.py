from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list f APIVIEW features"""
        an_apiview = [
            'Users HTTP methods as function',
            'Is similar to traditional Django View',
            'Gives you the most control over your application logic',
            'is mappned manually to URLs',
        ]

        return Response({'Message': 'Hello', 'an_apiview': an_apiview})
