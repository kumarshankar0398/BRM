from django.shortcuts import render
from BRMApp.forms import NewBookForm,SearchForm
from django.http import HttpResponse,HttpResponseRedirect
from BRMApp import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username'];
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/BRMApp/view-books/')
        else:
            data['error']="Username or Password is incorrect!!!!"
            res=render(request,'BRMApp_Template/user_login.html',data)
            return res
    else:
        return render(request,'BRMApp_Template/user_login.html',data)

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRMApp/login/')

@login_required(login_url="/BRMApp/login/")
def searchBooks(request):
    form=SearchForm()
    username=request.session['username']
    res=render(request,'BRMApp_Template/search_book.html',{'form':form})
    return res

@login_required(login_url="/BRMApp/login/")
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'BRMApp_Template/search_book.html',{'form':form,'books':books})
    return res

@login_required(login_url="/BRMApp/login/")
def deleteBooks(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMApp/view-books')

@login_required(login_url="/BRMApp/login/")
def editBooks(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMApp_Template/edit_book.html',{'form':form,'book':book})
    return res

@login_required(login_url="/BRMApp/login/")
def edit(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMApp/view-books')

@login_required(login_url="/BRMApp/login/")
def viewBooks(request):
    books=models.Book.objects.all()
    username=request.session['username']
    res=render(request,'BRMApp_Template/view_book.html',{'books':books,'username':username})
    return res

@login_required(login_url="/BRMApp/login/")
def newBooks(request):
    form=NewBookForm()
    username=request.session['username']
    res=render(request,'BRMApp_Template/new_book.html',{'form':form})
    return res

@login_required(login_url="/BRMApp/login/")
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    return HttpResponseRedirect('BRMApp/view-books')
