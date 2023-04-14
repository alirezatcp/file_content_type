from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import FileSerializer


class FileView(APIView):

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            filetype = file.content_type
            time = serializer.data['time']
            # file_type=magic.from_file(file)
            return Response({'file name': str(file), 'file type': filetype, 'time': time},
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
