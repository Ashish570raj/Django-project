# created by me


from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello ashish raj</h1> 
#                         <a href="https://www.w3schools.com/django/django_views.php">
#                         django w3schools</a>''')

# def about(request):
#     return HttpResponse(" about ashish raj")

def index(request):
    return render(request,'index.html')
   # return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext=request.POST.get('text','defautl')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    #print(removepunc)
    #print(djtext)
    #analyzed=djtext
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'TEXT ANALYZED ', 'analyzed_text': analyzed}
        djtext=analyzed

    
    if (fullcaps=='on'):
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'TEXT ANALYZED ', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(newlineremover=='on'):
        analyzed=''
        for char in djtext:
            if char!='\n' and char!="\r":    
                analyzed=analyzed+char
            else:
                print("no")
        print("pre",analyzed)
        params = {'purpose': 'TEXT ANALYZED ', 'analyzed_text': analyzed}
        djtext=analyzed
    
    if(extraspaceremover=='on'):
        analyzed=''
        for index,char in enumerate(djtext[:-1]):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'TEXT ANALYZED ', 'analyzed_text': analyzed}
                          
    if(removepunc !='on' and newlineremover!='on' and extraspaceremover!='on' and fullcaps!='on'):
        return HttpResponse('error')
    
    
    return render(request, 'analyze.html', params)

        
    
def navigation(request):
    s='''<h1>Navigation bar<br></h1>
        <a href="https://www.youtube.com/watch?v=fbgKj0myUOk&t=3616s"> Art of letting go</a> <br>
        <a href="https://www.youtube.com/watch?v=Q7bPssMKxYI&t=15s"> why not you</a><br>
        <a href="https://www.kaggle.com/code"> my kaggle profile </a> <br>
        <a href="https://www.w3schools.com/python/scipy/scipy_intro.php"> scipy tutorial </a> '''
    return HttpResponse(s)

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("remove new line")

# def spaceremove(request):
#     return HttpResponse("remove spaces <a href='/'> back </a>")

# def charcount(request):
#     return HttpResponse("count C har")