from .models import Flight, Booking
from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from datetime import date
from .serializers import FlightSerializer, BookingSerializer 



class FlightListView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingListView(ListAPIView):
	queryset = Booking.objects.filter(date__gte=date.today())
	serializer_class = BookingSerializer