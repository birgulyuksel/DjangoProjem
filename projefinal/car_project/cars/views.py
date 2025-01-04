from pyexpat import model
from django.shortcuts import render
from .models import Car
import requests
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from cars.scraper import get_car_data
import pandas as pd



def get_models(request):
    marka = request.GET.get('marka')
    if marka:
        models = Car.objects.filter(marka=marka).values_list('model', flat=True).distinct()
        return JsonResponse({'models': list(models)})
    return JsonResponse({'models': []})

def fetch_data(request):
    # Örnek veri çekme (Arabam.com'dan gerçek veri çekimi burada yapılabilir)
    data = {"status": "success", "message": "Veri çekildi!"}
    return JsonResponse(data)

def trend_analysis(request):
    return render(request, '/trend_analysis.html')

def scraping(request):
    car_data = get_car_data()  # Verileri scraping fonksiyonundan alıyoruz
    return render(request, 'cars/scraping.html', {'cars': car_data})  # Verileri şablona gönderiyoruz


def home(request):
    marka = request.GET.get('marka')
    model = request.GET.get('model')
    renk = request.GET.get('renk')
    yil = request.GET.get('yil', '')
    km_min = request.GET.get('km_min', '')
    km_max = request.GET.get('km_max', '')
    fiyat_min = request.GET.get('fiyat_min', '')
    fiyat_max = request.GET.get('fiyat_max', '')
    kaza_raporu = request.GET.get('kaza_raporu', '')
    yakit_turu = request.GET.get('yakit_turu', '')
    vites_turu = request.GET.get('vites_turu', '')
    arac_durumu = request.GET.get('arac_durumu', '')
    takas_durumu = request.GET.get('takas_durumu', '')
    cekis = request.GET.get('cekis', '')
    motor_gucu = request.GET.get('motor_gucu', '')
    motor_hacmi = request.GET.get('motor_hacmi', '')
    cars = Car.objects.all()
    
    if marka:
        cars = cars.filter(marka=marka)
    if renk:
        cars = cars.filter(renk=renk)
    if model:
        cars = cars.filter(model=model)
    if yil:
        if yil == '2000once':
            cars = cars.filter(yil__lt=2000)
        elif yil == '2000_2005arasi':
            cars = cars.filter(yil__gte=2000, yil__lte=2005)
        elif yil == '2005_2010arasi':
            cars = cars.filter(yil__gte=2005, yil__lte=2010)
        elif yil == '2010_2020arasi':
            cars = cars.filter(yil__gte=2010, yil__lte=2020)
        elif yil == '2020sonra':
            cars = cars.filter(yil__gt=2020)
    if km_min or km_max:
        if km_min:
            cars = cars.filter(km__gte=int(km_min))
        if km_max:
            cars = cars.filter(km__lte=int(km_max))

    if fiyat_min or fiyat_max:
        if fiyat_min:
            cars = cars.filter(fiyat__gte=int(fiyat_min))
        if fiyat_max:
            cars = cars.filter(fiyat__lte=int(fiyat_max))
    if kaza_raporu:
        cars = cars.filter(kaza_raporu=kaza_raporu)
    if yakit_turu:
        cars = cars.filter(yakit_turu=yakit_turu)
    if vites_turu:
        cars = cars.filter(vites_turu=vites_turu)
    if arac_durumu:
        cars = cars.filter(arac_durumu=arac_durumu)
    if takas_durumu:
        cars = cars.filter(takas_durumu=takas_durumu)
    if cekis:
        cars = cars.filter(cekis=cekis)

    # Motor gücü aralığını temizleyip filtrelemek
    if motor_gucu:
        try:
            motor_gucu = float(motor_gucu)  # motor gücünü sayıya dönüştürme
            cars = cars.filter(motor_gucu__gte=motor_gucu)
        except ValueError:
            pass  # Hatalı değer girildiyse filtreyi uygulama

    if motor_hacmi:
        try:
            motor_hacmi = float(motor_hacmi)  # motor hacmini sayıya dönüştürme
            cars = cars.filter(motor_hacmi__gte=motor_hacmi)
        except ValueError:
            pass  # Hatalı değer girildiyse filtreyi uygulama

    return render(request, 'cars/home.html', {'cars': cars})

def trend_analysis(request):
    # Excel dosyasını okuyun
    file_path = "C:\\Users\\birgu\\Desktop\\projefinal\\car_project\\Araba_Verileri_Duzenli_pivot.xlsx"  # Dosya yolunu doğru girin
    df = pd.read_excel(file_path)

    # Renk analizini yap
    if 'Renk' in df.columns:
        top_colors = df['Renk'].value_counts().head(5).to_dict()
    else:
        top_colors = {}

    # Araç Durumu analizini yap
    if 'Araç Durumu' in df.columns:
        top_conditions = df['Araç Durumu'].value_counts().head(5).to_dict()
    else:
        top_conditions = {}

    return render(request, 'cars/trend_analysis.html', {
        'top_colors': top_colors,
        'top_conditions': top_conditions,
    })


