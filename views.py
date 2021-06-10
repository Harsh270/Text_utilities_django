from django.shortcuts import *

def index(request):
    return render(request,'index.html')
def analyze(request):
    pun=request.POST.get('punctuation')
    text=request.POST.get('text')
    upper=request.POST.get('upper')
    count=request.POST.get('count')
    space=request.POST.get('space')
    if pun=='on':
        analyze=""
        p='''? …!.,—––:;'"><@#$“‘[ ]( )'''
        for i in text:
            if i not in p:
                analyze=analyze+i
        text=analyze
        params={'analyze_text':text}
        return render(request,"analyze.html",params)
    if upper=='on':
        analyze=''
        for i in text:
            analyze=analyze+i.upper()
        text=analyze
        params={'analyze_text':text}
        return render(request,'analyze.html',params)
    if count=='on':
        analyze=0
        for i in text:
            analyze=analyze+1
        text=analyze
        params={'analyze_text':text}
        return render(request,'analyze.html',params)
    if space=='on':
        analyze=''
        for i in text:
            if i !=' ':
                analyze=analyze+i
        text = analyze
        params = {'analyze_text': text}
        return render(request, 'analyze.html', params)