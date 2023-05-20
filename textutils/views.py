from tkinter import OFF
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   
   return render(request,'index.html')
   

def analyze(request):
   #get the text
   djtext = (request.POST.get('text','default'))

   # Check the check box
   removepunc = (request.POST.get('removepunc',OFF))
   fullcaps = (request.POST.get('fullcaps',OFF))
   newlilneremover = (request.POST.get('newlilneremover',OFF))
   extraspaceremover = (request.POST.get('extraspaceremover',OFF))

   
   # Check which check box is on
   if removepunc == "on":
      punctuations = '''!().-[]{};:'"\,<>/?@#$^&*_~'''
      analyzed = ""
      for char in djtext:
         if char not in punctuations:
            analyzed = analyzed+char
      params = {'purpose':'Remove Punctuations','analyzed_text':analyzed}
      djtext = analyzed
      # return render(request,'analyze.html',params)
   
   if(fullcaps == 'on'):
      analyzed=""
      for char in djtext:
         analyzed = analyzed + char.upper()
      params={'purpose': 'Change to uppercase' , 'analyzed_text':analyzed}
      djtext = analyzed
      # return render(request,'analyze.html',params)
   
   if(newlilneremover == 'on'):
      analyzed=""
      for char in djtext:
         if char !="\n" and char !="\r":
            analyzed = analyzed + char
         else:
            print("no")
      params={'purpose': 'New lines removed' , 'analyzed_text':analyzed}
      djtext = analyzed
      # return render(request,'analyze.html',params)
   
   if(extraspaceremover == 'on'):
      analyzed=""
      for index, char in enumerate(djtext):
         if not( djtext[index ] == " " and djtext[index+1] == " "):
            analyzed = analyzed + char
      params={'purpose': 'New lines removed' , 'analyzed_text':analyzed}
   
   if(removepunc != "on" and newlilneremover !='on' and fullcaps !='on' and extraspaceremover !='on'):
      return HttpResponse('Select atleast one operation')
   

 
   
   return render(request,'analyze.html',params)



# def capfirst(request):
#    return HttpResponse ("Capitalize first")

# def newlineremove (request):
#    return HttpResponse ("remove the new line")

# def spaceremover (request):
#    return HttpResponse ("remove space <a href='/'>back</a>")

# def charcount (request):
#    return HttpResponse ("Char count")



