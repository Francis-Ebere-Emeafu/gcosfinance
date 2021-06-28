from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from account.forms import StartForm, NameForm
from account.models import Account


def start(request):
    context = {}
    if request.POST:
        form = StartForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            email = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('phone')
            first_name = form.cleaned_data.get('first_name').lower()
            last_name = form.cleaned_data.get('last_name').lower()
            new_user = User.objects.create_user(username=email, email=email, password=password)
            print(new_user)
            new_account.user = new_user
            new_account.save()
            request.session['email'] = new_user.email
            return redirect("questions")
            # return redirect("register")

        else:
            context['form'] = form
    return render(request, 'account/start.html', context)


def register(request):
    context = {}
    # del form.fields["email"]
    # del form.fields["phone"]
    email = request.session.get('email')
    request.session['email'] = email
    user = User.objects.get(username=email)
    account = Account.objects.get(user=user)

    if request.POST:
        print('Reauest.POST Method')
        form = NameForm(request.POST or None, instance=account)
        print(form)
        if form.is_valid():
            updated_account = form.save(commit=False)
            first_name = form.cleaned_data.get('first_name').lower()
            last_name = form.cleaned_data.get('last_name').lower()
            updated_account.first_name = first_name
            updated_account.last_name = last_name
            updated_account.save()
            return redirect("questions")
        else:
            context['form'] = form

    return render(request, 'account/register.html', context)
