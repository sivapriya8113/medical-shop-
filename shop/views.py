from django.shortcuts import render,get_object_or_404, redirect
from . models import Category,Product


def allProdCat(request, c_slug=None): #used to show all products in that category
	c_page = None #for categories
	products_list = None
	if c_slug!=None:
		c_page = get_object_or_404(Category,slug=c_slug)
		products = Product.objects.filter(category=c_page,available=True) #filtering products according to category 
	else:
		products = Product.objects.all().filter(available=True)
	return render(request,'shop/category.html',{'category':c_page,'products':products})


def ProdCatDetail(request, c_slug, product_slug): #Used to show detail product view
	try:
		product = Product.objects.get(category__slug=c_slug, slug=product_slug)
	except Exception as e:
		raise e
	return render(request, 'shop/product.html', {'product':product})


