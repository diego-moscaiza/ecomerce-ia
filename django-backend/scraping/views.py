import asyncio
from . import scrape
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import InfoPrendasScrapingSerializer


def fetch_products(request):
    prendas = asyncio.run(scrape.scrape_async())
    return HttpResponse(str(prendas))


@api_view(["POST"])
def register_scrape_products(request):
    # Get the data from the frontend
    serializer = InfoPrendasScrapingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        return Response(
            {"info_productos": serializer.data},
            status=status.HTTP_202_ACCEPTED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
