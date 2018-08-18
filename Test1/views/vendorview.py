from django.db.models import Q
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from Test1.forms.vendorform import vendorForm
from Test1.models import vendorModel


class vendorFormView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.vendorform = vendorForm
        self.vendor = vendorModel.objects.all()
        return super(vendorFormView, self).dispatch(request, self, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        context= {
            'user': request.GET,
            'model': self.vendor,
            'form': self.vendorform
        }
        string = render_to_string("awamicrockery/index.html", context)
        return HttpResponse(string)
    def post(self, request,*args, **kwargs):
        self.form = vendorForm(request.POST)
        print (request.POST['first_name'])
        print (self.form.is_valid())
        if self.form.is_valid():
            data = self.form.cleaned_data
            print data
            firstname = data['first_name']
            lastname = data['last_name']
            price = data['price']
            itemcode = request.POST['item_code']
            print(firstname, lastname, price, itemcode)
            vendorModel.objects.update_or_create(
                first_name=firstname,
                last_name=lastname,
                price=price,
                item_code=itemcode
            )
            return HttpResponse('success')
        else:
            print ("Invalid Form")
        context={'model':self.vendor,
            'form':self.form
        }
        string = render_to_string("awamicrockery/index.html", context)
        return HttpResponse(string)
class searchView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(searchView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        try:
            search = request.GET.get('q')
            print (search)
            vendor = vendorModel.objects.filter(Q(Q(first_name__iexact=search) |
                                                  Q(first_name__icontains=search) | Q(last_name__iexact=search) | Q(last_name__icontains=search)))

            vendor_list = []
            print vendor_list
            for vendor in vendor:
                object = {'first_name': vendor.first_name,
                          'last_name': vendor.last_name,
                          'price': vendor.price,
                          'item_code':vendor.item_code}

                vendor_list.append(object)
            context={
                'vendorlist':vendor_list,
            }
            string =render_to_string("awamicrockery/_partial/_search.html",context)
            return HttpResponse(string)

        except Exception as e:
            print (e)
            response = {'status': 'failed', 'message': e}
            return HttpResponse(response)