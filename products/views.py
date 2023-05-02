from django.shortcuts import render
from rest_framework.decorators import api_view
from products.models import Product
from rest_framework.response import Response

# Create your views here.

#here we imported a decorater.
@api_view(['GET','POST','PUT','PATCH','DELETE'])

#Here we define a Function Named ecom.
def ecom(request,pk=None,*args, **kwargs):

#this is the first method POST from which we are posting from the frontend data and its shows the functionality.
    if request.method == 'POST':
        pname = request.data['pname']
        p_description = request.data['p_description']
        price = request.data['price']
        a = Product(pname=pname,p_description=p_description,price=price)
        a.save()
        return Response('POST REQUEST CALLED and Data added')


#This is the second method GET from which we can get all the saved data from the backend and it is the functionality.
    if request.method == 'GET':
        pro = Product.objects.all().values()
        # pro = Product(pname=pname,p_description=p_description,price=price)
        return Response(pro)


#This is the third method PUT from which we can partially update our data from front end. 
    if request.method == 'PUT':
        pname = request.data['pname']
        val = request.data['p_description']
        person = Product.objects.filter(pname=pname).update(p_description=request.data['p_description'],price=request.data['price'])
        return Response("Data Updated Sucessfully")


#This is the fourth  method PATCH from which we can update the whole data passing from frontend.
    if request.method == 'PATCH':
        pname = request.data['pname']
        id = request.data['id']
        val = request.data['p_description']
        person = Product.objects.filter(id=id).update(pname=pname,p_description=request.data['p_description'],price=request.data['price'])
        return Response("Data Updated Sucessfully")


#this is fifth and last method from which we are going to delete the saved data from backend.  
    if request.method == "DELETE":
        id = Product.objects.get(id = pk)
        # dlt = Product.objects.get(id = id)
        id.delete()
        return Response('DELETE API CALLED SUCESSFULLY DATA DELETED')