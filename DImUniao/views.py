from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from DImUniao import models, forms
from django.views.generic.edit import FormView

# def home(request):
#     return render(request, 'index.html')

class home(FormView):
    template_name = 'index.html'
    form_class = forms.home
    # model = models.MemorialDescritivo
    success_url = '/{:0}/'
    
    def form_valid(self, form):
        self.success_url = self.success_url.format(form.cleaned_data["RIPU"])
        return super(home, self).form_valid(form)
  
def graficojson(request, RIPU):
    labels = []
    data = []
    
    queryset = models.Depreciacao.objects.filter(RIPU=RIPU).order_by('MES')
    for entry in queryset:
        labels.append(entry.MES)
        data.append(entry.VDEPRECACUMU)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'RIPU': RIPU,
    })
    
def grafico(request, RIPU):
    return render(request, 'grafico.html', {
        'RIPU': RIPU,
    })

def graficosjson(request):
    labels = []
    data = []
    RIPU = []
    
    queryset = models.Depreciacao.objects.all()
    for entry in queryset:
        labels.append(entry.REF)
        data.append(entry.VDEPRECACUMU)
        RIPU.append(entry.RIPU)
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'RIPU': RIPU,
    })
    
def graficos(request):
    return render(request, 'graficos.html')
