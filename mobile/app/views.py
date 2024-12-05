from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os
from django.contrib.auth.models import *
from django.contrib import messages

def mob_login(req):
    if 'mob' in req.session:
        return redirect(home_ad)
    if req.method=='POST':
        uname=req.POST['uname']
        password=req.POST['passwd']
        data=authenticate(username=uname,password=password)
        if data:
            #create session
            if data.is_superuser:
                login(req,data)
                req.session['mob']=uname   
                return redirect(home_ad)
            else:
                
                login(req,data)
                req.session['user']=uname   
                return redirect(user_home)
        else:
            messages.warning(req,'Invalid username or password.')
            return redirect(mob_login)
    else:
        return render(req,'login.html')
    
def home_ad(req):
    if 'mob' in req.session:
        data=Product.objects.all()
        return render(req,'admin/home.html',{'data':data})
    else:
        return redirect(mob_login)
 #delete session

def mob_logout(req):
    req.session.flush()          
    logout(req)
    return redirect(mob_login)

def add_prod(req):
    if 'mob' in req.session:
        if req.method=='POST':
            product_id=req.POST['mob_id']
            product_name=req.POST['mob_name']
            product_price=req.POST['mob_price']
            ofr_price=req.POST['ofr_price']
            img=req.FILES['img']
            
            data=Product.objects.create(pro_id=product_id,name=product_name,price=product_price,offer_price=ofr_price,img=img)
            data.save()
            return redirect(add_prod)
        else:
            return render(req,'admin/add_product.html')
    else:
        return redirect(mob_login)
    
def edit_product(req,pid):
    if 'mob' in req.session:
        if req.method=='POST':
            prd_id=req.POST['prd_id']
            prd_name=req.POST['prd_name']
            prd_price=req.POST['prd_price']
            ofr_price=req.POST['ofr_price']
            
            img=req.FILES.get('img')
            if img:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,offer_price=ofr_price)
                data=Product.objects.get(pk=pid)
                data.img=img
                data.save()
            else:
                Product.objects.filter(pk=pid).update(pro_id=prd_id,name=prd_name,price=prd_price,offer_price=ofr_price)
            return redirect(home_ad)
        else:
            data=Product.objects.get(pk=pid)
            return render(req,'admin/edit.html',{'product':data})
    else:
        return redirect(mob_login)

def delete_product(req,pid):
    data=Product.objects.get(pk=pid)
    url=data.img.url
    og_path=url.split('/')[-1]
    os.remove('static/images/'+og_path)
    data.delete()
    return redirect(home_ad)


    #user

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
       
        try:
           
            data=User.objects.create_user(first_name=name,email=email,password=password,username=email)
            data.save()
            return redirect(mob_login)
        except:
            messages.warning(req,'User already exists.')
            return redirect(register)
    else:
        return render(req,'user/registration.html')

def user_home(req):
    if 'user' in req.session:
        data=Product.objects.all()
        return render(req,'user/home.html',{'data':data})
    else:
        return redirect(mob_login)
    
def view_pro(req,pid):
        data=Product.objects.get(pk=pid)
        return render(req,'user/view_pro.html',{'data':data})
