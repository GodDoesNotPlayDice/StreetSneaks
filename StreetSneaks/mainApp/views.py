from django.shortcuts import render
from sneakerApp.models import Zapatilla
# Create your views here.
ZAPATILLA = Zapatilla.objects.all()
def index(request):
    ctx = {'items': ZAPATILLA}
    return render(request, 'index.html', ctx)
