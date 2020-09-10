from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from django.utils.decorators import method_decorator
from SGCapp.models import Cliente, Cobrador, Banco, Cheque
from SGCapp.forms import ClienteForm, CobradorForm, BancoForm, ChequeForm

# Create your views here.


class dashboardView(TemplateView):
    template_name = 'SGCapp/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administración'

        return context


# vista basada en funcion


def clientes_list(request):
    data = {
        'title': 'Listado de Clientes-vista basada en funcion',
        'clientes': Cliente.objects.all()
    }
    return render(request, 'SGCapp/clientes/list.html', data)

# vista basada en Clase - con el decorador (login_required) valido que el
# usuario este logueado para ver la vista


class ClienteListView (ListView):
    model = Cliente
    template_name = 'SGCapp/clientes/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        # data = Cliente.objects.get(pk=request.POST['id']).toJSON
        # return JsonResponse(data)
        # el siguiente codigo es para renderizar con ayax cuando son miles de
        # filas en la tabla se utiliza con el list.js y el toJson
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cliente.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Litado de Clientes'
        context['create_url'] = reverse_lazy('SGCapp:ClienteCreateView')
        context['list_url'] = reverse_lazy('SGCapp:ClienteListView')
        context['entity'] = 'Clientes'
        return context


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'SGCapp/clientes/create.html'
    success_url = reverse_lazy('SGCapp:ClienteListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        #  print(request.POST)
        #  form = ClienteForm(request.POST)
        #  if form.is_valid():
        #      form.save()
        #      return HttpResponseRedirect(self.success_url)
        #  self.object = None
        #  context = self.get_context_data(**kwargs)
        #  context['form'] = form
        #  return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('SGCapp:ClienteListView')
        context['action'] = 'add'
        return context


class ClienteUpdateView(UpdateView):

    model = Cliente
    form_class = ClienteForm
    template_name = 'SGCapp/clientes/create.html'
    success_url = reverse_lazy('SGCapp:ClienteListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar cliente'
        context['entity'] = 'Clientes'
        context['list_url'] = reverse_lazy('SGCapp:ClienteListView')
        context['action'] = 'edit'
        return context


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'SGCapp/clientes/delete.html'
    success_url = reverse_lazy('SGCapp:ClienteListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        print(self.success_url)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar cliente'
        context['entity'] = 'Cliente'
        context['list_url'] = self.success_url
        return context


# vista form Cliente
class ClienteFormView(FormView):
    form_class = ClienteForm
    template_name = 'SGCapp/clientes/create.html'
    success_url = reverse_lazy('SGCapp:ClienteListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario cliente'
        context['entity'] = 'Cliente'
        context['list_url'] = self.success_url
        return context

# vistas Cobrador


class CobradorListView (ListView):

    model = Cobrador
    template_name = 'SGCapp/cobradores/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        # data = Cobrador.objects.get(pk=request.POST['id']).toJSON
        # return JsonResponse(data)
        # el siguiente codigo es para renderizar con ayax cuando son miles de
        # registros en la tabla
        # se utiliza con el list.js y el toJson
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cobrador.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cobradores'
        context['create_url'] = reverse_lazy('SGCapp:CobradorCreateView')
        context['list_url'] = reverse_lazy('SGCapp:CobradorListView')
        context['entity'] = 'Cobradores'
        print(reverse_lazy('SGCapp:CobradorListView'))
        return context


class CobradorCreateView(CreateView):
    model = Cobrador
    form_class = CobradorForm
    template_name = 'SGCapp/cobradores/create.html'
    success_url = reverse_lazy('SGCapp:CobradorListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        #  print(request.POST)
        #  form = ClienteForm(request.POST)
        #  if form.is_valid():
        #      form.save()
        #      return HttpResponseRedirect(self.success_url)
        #  self.object = None
        #  context = self.get_context_data(**kwargs)
        #  context['form'] = form
        #  return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear cobrador'
        context['entity'] = 'Cobradores'
        context['list_url'] = reverse_lazy('SGCapp:CobradorListView')
        context['action'] = 'add'
        return context


class CobradorUpdateView(UpdateView):

    model = Cobrador
    form_class = CobradorForm
    template_name = 'SGCapp/cobradores/create.html'
    success_url = reverse_lazy('SGCapp:CobradorListView')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar cobrador'
        context['entity'] = 'Cobradores'
        context['list_url'] = reverse_lazy('SGCapp:CobradorListView')
        context['action'] = 'edit'
        return context


class CobradorDeleteView(DeleteView):
    model = Cobrador
    template_name = 'SGCapp/cobradores/delete.html'
    success_url = reverse_lazy('SGCapp:CobradorListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar cobrador'
        context['entity'] = 'Cobrador'
        context['list_url'] = self.success_url
        return context


# VISTAS BANCO ------------------------------------


class BancoListView (ListView):
    model = Banco
    template_name = 'SGCapp/bancos/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)

        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Banco.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Bancos'
        context['create_url'] = reverse_lazy('SGCapp:BancoCreateView')
        context['list_url'] = reverse_lazy('SGCapp:BancoListView')
        context['entity'] = 'Bancos'
        print(reverse_lazy('SGCapp:BancoListView'))
        return context

# vista form Banco -------------------


class BancoFormView(FormView):
    form_class = BancoForm
    template_name = 'SGCapp/bancos/create.html'
    success_url = reverse_lazy('SGCapp:BancoListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario banco'
        context['entity'] = 'Bancos'
        context['list_url'] = self.success_url
        return context


class BancoCreateView(CreateView):
    model = Banco
    form_class = BancoForm
    template_name = 'SGCapp/bancos/create.html'
    success_url = reverse_lazy('SGCapp:BancoListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear banco'
        context['entity'] = 'Bancos'
        context['list_url'] = reverse_lazy('SGCapp:BancoListView')
        context['action'] = 'add'
        return context


class BancoUpdateView(UpdateView):

    model = Banco
    form_class = BancoForm
    template_name = 'SGCapp/bancos/create.html'
    success_url = reverse_lazy('SGCapp:BancoListView')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar bancos'
        context['entity'] = 'Bancos'
        context['list_url'] = reverse_lazy('SGCapp:BancoListView')
        context['action'] = 'edit'
        return context


class BancoDeleteView(DeleteView):
    model = Banco
    template_name = 'SGCapp/bancos/delete.html'
    success_url = reverse_lazy('SGCapp:BancoListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar banco'
        context['entity'] = 'Bancos'
        context['list_url'] = self.success_url
        return context


#  VISTAS Cheques --------------------------------


class ChequeListView (ListView):
    model = Cheque
    template_name = 'SGCapp/cheques/list.html'

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        # print(request.FILE)

        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Cheque.objects.all()[:]:
                    # print(i)
                    # print(data)
                    cheque = i.toJSON()
                    # asigno el nombre del campo en el diccionario
                    cheque['cheque_banco'] = i.cheque_banco.nombre
                    print(cheque)
                    data.append(cheque)
                    # data.append(i.toJSON())
                # for i in Cheque.objects.all():
                #     data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Cheques'
        context['create_url'] = reverse_lazy('SGCapp:ChequeCreateView')
        context['list_url'] = reverse_lazy('SGCapp:ChequeListView')
        context['entity'] = 'Cheques'
        print(reverse_lazy('SGCapp:ChequeListView'))
        return context

# cheque form


class ChequeFormView(FormView):
    form_class = ChequeForm
    template_name = 'SGCapp/cheques/create.html'
    success_url = reverse_lazy('SGCapp:ChequeListView')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario cheque'
        context['entity'] = 'Cheques'
        context['list_url'] = self.success_url
        return context


class ChequeCreateView(CreateView):
    model = Cheque
    form_class = ChequeForm
    template_name = 'SGCapp/cheques/create.html'
    success_url = reverse_lazy('SGCapp:ChequeListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear cheque'
        context['entity'] = 'Cheques'
        context['list_url'] = reverse_lazy('SGCapp:ChequeListView')
        context['action'] = 'add'
        return context


class ChequeUpdateView(UpdateView):

    model = Cheque
    form_class = ChequeForm
    template_name = 'SGCapp/cheques/create.html'
    success_url = reverse_lazy('SGCapp:ChequeListView')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        print('imprimir post')
        print(request.POST)
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar cheques'
        context['entity'] = 'Cheques'
        context['list_url'] = reverse_lazy('SGCapp:ChequeListView')
        context['action'] = 'edit'
        return context


class ChequeDeleteView(DeleteView):
    model = Cheque
    template_name = 'SGCapp/cheques/delete.html'
    success_url = reverse_lazy('SGCapp:ChequeListView')

    @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

        print(request.POST)
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar cheque'
        context['entity'] = 'Cheques'
        context['list_url'] = self.success_url
        return context
