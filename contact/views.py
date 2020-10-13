from django.shortcuts import redirect, render
from django.contrib import messages

from contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return redirect('thanks')
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, 'contact/contact.html', context)




def thanks(request):
    return render(request, 'contact/thanks.html')