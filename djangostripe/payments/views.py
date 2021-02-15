from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe
from django.http import HttpResponseRedirect

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
        
def charge(request):
    return render(request, 'charge.html')    
        
def payment_intent(request):
    print(request.POST)
    if request.POST:
        intent = stripe.PaymentIntent.create(
			amount = int(request.POST['amount']) * 100,
			currency = 'usd',
			metadata={'integration_check': 'accept_a_payment'},
	    )
        return render(request, 'checkout.html', {'client_secret': intent.client_secret, 'pk_key': settings.STRIPE_PUBLISHABLE_KEY })
    return render(request, 'payment_intent.html')       
	





	