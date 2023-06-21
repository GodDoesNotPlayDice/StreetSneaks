from datetime import datetime, timedelta
from django.test import TestCase

# Create your tests here.

print((datetime.now().date() + timedelta(days=3)).strftime('%d de %B del %Y'))