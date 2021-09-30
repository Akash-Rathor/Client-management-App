from django.shortcuts import render,redirect
from clients.models import new_customer
# Create your views here.

def dashboard(request):
    return render(request,'company_dashboard.html')

def product(request):
    return render(request,'product_upload.html')

def my_menu(request):
    return render(request,'my_menu.html')

def add(request):

    if request.method=="POST":
        user_id = request.user
        phone=request.POST['phone']
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        age=request.POST['date']
        phone_al = new_customer.objects.filter(user_id=user_id,phone=phone)
        if len(phone_al)==0:
            cust = new_customer(user_id=user_id,name=name,email=email,phone=phone,Address=address,age=age)
            cust.save()
            return redirect('all customer')
        else:
            return redirect('all customer')
    return render(request, 'add_customer.html')

def all_customer(request):
    if request.user.is_authenticated:
        user_id = request.user
        customers = new_customer.objects.filter(user_id=user_id)
        return render(request,'all_customer.html',{'context':customers})
    else:
        return redirect('login-page')
    # return render(request, 'all_customers.html')

def delete_customer(request,key_id):
    if request.user.is_authenticated:
        user_id=request.user
        customer=new_customer.objects.filter(user_id=user_id,id=key_id)
        customer.delete()
        return redirect('all customer')
    else:
        return redirect('login-page')

def offers(request):
    return render(request,'offers.html')


def select_theme(request, theme_id):
    # if request.user.is_authenticated:
    #     try:
    #         theme = Themes.objects.get(id=theme_id)
    #         #To write for theme selection or change
    #         user_obj = User.objects.get(id=request.user.id)
    #         if not UserThemes.objects.filter(theme=theme, user=request.user):
    #             for record in UserThemes.objects.filter(user=request.user):
    #                 record.is_active = False
    #                 record.save()
    #             user_choice = UserThemes(user_name=user_obj.username, user=user_obj, theme=theme, is_active=True)
    #             user_choice.save()
    #         else:
    #             for record in UserThemes.objects.filter(user=request.user):
    #                 record.is_active = False
    #                 record.save()
    #             user_choice = UserThemes.objects.filter(user_name=user_obj.username, user=user_obj, theme=theme)[0]
    #             user_choice.is_active = True
    #             user_choice.save()

    #         return redirect('main_nav')
    #     except :
    #         return redirect('theme_select')
    return redirect('login-page')