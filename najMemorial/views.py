
from logging import exception
from sqlite3 import paramstyle
from django.shortcuts import render,redirect
from najMemorialApp.models import Contact, frontImg, Gallary, Commentq,verify_bot
from datetime import date, datetime
from django.http import JsonResponse
import random
from PIL import Image, ImageDraw, ImageFont

def index(request):
    # taking comment data from index.html
    if request.method=="POST":
        name=request.POST.get('name')
        sub=request.POST.get('sub')
        desc=request.POST.get('desc')
        captcha_sno=request.POST.get('captcha_id')
        captcha_sum=request.POST.get('captcha_sum')
        captcha_file=verify_bot.objects.filter(sno=captcha_sno)
        if captcha_file[0].value==int(captcha_sum):
            date=datetime.now()
            comm_querry=Commentq.objects.filter(comm_desc=desc)
            if(len(comm_querry)==0):
                comment=Commentq(comm_name=name,comm_sub=sub,comm_desc=desc,comm_date=date)
                comment.save()
                allComt=Commentq.objects.all().values()
                allComt=list(allComt)
                file_bot=verify_bot.objects.all().values()
                random_file=random.choice(file_bot)
                return JsonResponse({'data':200,'msg':'Your querry has been posted','random_bot_file':random_file,'allComt':allComt})
            else:
                allComt=Commentq.objects.all().values()
                allComt=list(allComt)
                file_bot=verify_bot.objects.all().values()
                random_file=random.choice(file_bot)
                return JsonResponse({'data':302,'msg':'Description Already Exist!','random_bot_file':random_file,'allComt':allComt})
            
        else:
            allComt=Commentq.objects.all().values()
            allComt=list(allComt)
            file_bot=verify_bot.objects.all().values()
            random_file=random.choice(file_bot)
            return JsonResponse({'data':302,'msg':'Captcha Not Verified!','random_bot_file':random_file,'allComt':allComt})

    file_bot=verify_bot.objects.all()
    random_file=random.choice(file_bot)
    bannerImg=frontImg.objects.all()
    gallaryImg=Gallary.objects.all()
    comm_querry=Commentq.objects.all()
    param={'bannerImg':bannerImg,'gallaryImg':gallaryImg,'comment':comm_querry,'random_bot_file':random_file}

    return render(request,'index.html',param)

def contact(request):
    massageVal='none'
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email',"Not Given")
        phone=request.POST.get('phone',0)
        desc=request.POST.get('desc')
        if(len(phone)==0):
            phone=00000
            if(name!="" and desc!=""):
                cont=Contact(cont_name=name,cont_email=email,cont_phone=phone,cont_desc=desc)
                cont.save()
                massageVal='success'
            else:
                massageVal='failed'
        else:
            if(name!="" and desc!=""):
                cont=Contact(cont_name=name,cont_email=email,cont_phone=phone,cont_desc=desc)
                cont.save()
                massageVal='success'
            else:
                massageVal='failed'
    param={'massageVal':massageVal}
    return render(request,'contact.html',param)

def about(request):
    return render(request,'about.html')


def gallary(request):
    gallaryPhoto=Gallary.objects.all()
    param={'gallaryPhoto':gallaryPhoto}
    return render(request,'gallary.html',param)

