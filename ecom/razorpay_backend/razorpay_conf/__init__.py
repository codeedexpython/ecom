import razorpay
from ecom import settings

client = razorpay.Client(auth=(settings.KEY, settings.SECRET_KEY))

