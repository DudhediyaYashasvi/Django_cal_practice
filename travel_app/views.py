from django.shortcuts import render, HttpResponse

# Create your views here.
def addition_view(request,num1,num2):
    a=num1
    b=num2
    result=a+b
    return HttpResponse(f"the result of {a} + {b} is: {result}")
def areaOfCircle_view(request,radius):
    r=radius
    area=3.14*r*r
    return HttpResponse(f"the area of circle with radius {r} is: {area}")
def subtraction_view(request,num1,num2):
    a=num1
    b=num2
    result=a-b
    return HttpResponse(f"the result of {a} - {b} is: {result}")
def multiplication_view(request,num1,num2):
    a=num1
    b=num2
    result=a*b
    return HttpResponse(f"the result of {a} * {b} is: {result}")
def division_view(request,num1,num2):
    a=num1
    b=num2
    if b!=0:
        result=a/b
        return HttpResponse(f"the result of {a} / {b} is: {result}")
    else:
        return HttpResponse("Division by zero is not allowed.")
def palindrome_view(request,word):
    w=word
    if w==w[::-1]:
        return HttpResponse(f"{w} is a palindrome.")
    else:
        return HttpResponse(f"{w} is not a palindrome.")

