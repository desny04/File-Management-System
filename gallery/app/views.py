from django.shortcuts import render,redirect
import bcrypt
from .models import *
# Create your views here.
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        cnf_password=request.POST['cnf_password']
        
        if password==cnf_password:
            hashed_password=bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt())
            Users.objects.create(name=name,email=email,password=hashed_password.decode('utf-8'))
            return redirect(login)      
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
    
    
        try:
            user=Users.objects.get(email=email)
            print(user)

            if bcrypt.checkpw(
                password.encode('utf-8'),
                user.password.encode('utf-8')
            ):
                request.session['user']=user.id
                return redirect(file_upload)

            else:
                print('Password doesnot match')

        except:
            print('User doesnot Exists')
            return redirect(login)
    return render(request,'login.html')





# def home(request):
#     if 'user' in request.session:
#         return render(request,'file.html')
#     else:
#         return redirect(login)
 
 
 
    
def logout(request):
    request.session.flush()
    return redirect(login)




def file_upload(request):
    if 'user' in request.session:
        user = Users.objects.get(id = request.session['user'])
        files=Docs.objects.filter(fname=user)
        if request.method=='POST':
            title=request.POST['title']
            doc=request.FILES['file']
            Docs.objects.create(title=title,file=doc,fname=user)
        return render(request,'file.html',{'files':files,'user':user})
    else:
        return redirect(login)