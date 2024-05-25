from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CarouselSlide
from .serializers import CarouselSlideSerializer

@api_view(['GET'])
def carousel_slide_list(request):
    if request.method == 'GET':
        slides = CarouselSlide.objects.all().order_by('position')
        serializer = CarouselSlideSerializer(slides, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def carousel_slide_create(request):
    if request.method == 'POST':
        position = request.data.get('position')
        if CarouselSlide.objects.filter(position=position).exists():
            return Response(
                {'error': 'Slide with this position already exists.'},
            )
        serializer = CarouselSlideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def carousel_slide_get(request,id):
    slide=CarouselSlide.objects.get(id=id)
    if request.method == 'GET':
        serializer = CarouselSlideSerializer(slide)
        return Response(serializer.data)


@api_view(['PUT'])
def carousel_slide_update(request, id):
    slide = CarouselSlide.objects.get(id=id)
    if request.method == 'PUT':
        serializer = CarouselSlideSerializer(instance=slide, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def carousel_slide_delete(request, id):
    slide = CarouselSlide.objects.get(id=id)
    if request.method == 'DELETE':
        slide.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






