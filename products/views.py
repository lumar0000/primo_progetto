from django.shortcuts import render
from products.models import Product, Manufacturer
from django.http import JsonResponse

# Create your views here.

def product_list (request):
    products = Product.objects.all() # [:30]
    data = {"products": list(products.values())} # .values("pk", “name")
    print (type(data) )
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product. objects. get (pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer.name,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity,
        }}
        response = JsonResponse (data)

    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "prodotto non trovato!"
            }},
            status=404)
    return response


def manufacturer_list(request):
    manufacturers=Manufacturer.objects.all()
    data = {"manufacturers": list (manufacturers.values())} 
    response = JsonResponse(data)
    return response

def manufacturer_detail (request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        manufacturer_products = manufacturer.products.all() 
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer. location, "active": manufacturer.active,
            "products": list (manufacturer_products.values())
        }}
        response = JsonResponse(data)
    except Manufacturer. DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "produttore non trovato!"
            }},
            status=404)
        return response