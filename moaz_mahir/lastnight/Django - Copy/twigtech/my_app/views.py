from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView
from my_app.models import Set_Price
from my_app.forms import SetPriceForm
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def table(request):
    return render(request, 'tables.html')

def notifications(request):
    return render(request, 'notifications.html')

def profile(request):
    return render(request, 'profile.html')

def sign_out(request):
    return render(request, 'sign_out.html')



class DashboardView (TemplateView):
    template_name = 'dashboard.html'

class SetPriceListView (ListView):
    template_name = 'tables.html'
    model = Set_Price

# class SetPriceListView (ListView):
#     template_name = 'tables.html'
#     model = Set_Price
#     context_object_name = 'Set_Price_List'
#     ordering = ['-Upper_Price']
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Set_Price_List'] = Set_Price.objects.all()
#         return context

    
# class SetPriceFormView (FormView):
#     template_name = 'my_app/set_price.html'
#     form_class = SetPriceForm
#     success_url = '/set_price_list/'

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         # form.save()
#         return super().form_valid(form)
    
class SetPriceCreateView (CreateView):
    template_name = 'tables.html'
    form_class = SetPriceForm
    model = Set_Price
    # fields = ['Upper_Price', 'Lower_Price']
    # fields = "__all__"
    success_url = reverse_lazy('my_app:Set_Price_List')
    
    def get_success_url(self):
        return reverse('my_app:Set_Price_List')
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Set_Price_List'] = Set_Price.objects.all()
        return context

'''
class SetPriceListView(ListView):
    template_name = 'tables.html'
    model = Set_Price
    context_object_name = 'set_prices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SetPriceForm()
        return context

    def post(self, request, *args, **kwargs):
        form = SetPriceForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)

class SetPriceCreateView(CreateView):
    template_name = 'tables.html'
    form_class = SetPriceForm
    model = Set_Price
    success_url = reverse_lazy('my_app:Set_Price_List')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['set_prices'] = Set_Price.objects.all()
        return context
'''