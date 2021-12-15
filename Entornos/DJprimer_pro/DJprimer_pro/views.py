from django.shortcuts import render 

def inicio(request):
	producto = [
			{"nombre":"Computadora", "precio":120},
			{"nombre":"Televisor", "precio":90}, 
	]
	
	usuario={
			"nombre":"Pablo"
	}

	context={
			"usuario":usuario,
			"producto":producto
	}
	return render(request, "inicio.html",context)

