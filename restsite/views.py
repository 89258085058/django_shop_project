from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from restsite.forms import ContactForm
from restsite.models import ItemModel, TestModel


def index(requests):
    menu_brk = TestModel.objects.filter().order_by('?')[:6]
    # menu_brk = ItemModel.objects.filter(type__exact='BRK').order_by('?')[:6]
    menu_lun = ItemModel.objects.filter(type__exact='LUN').order_by('?')[:6]
    menu_din = ItemModel.objects.filter(type__exact='DIN').order_by('?')[:6]
    context = {'menu_brk': menu_brk, 'menu_lun': menu_lun, 'menu_din': menu_din}
    return render(requests,
                  'index.html',
                  context=context
                  )

def about(requests):
    return render(requests, 'about.html')

def contact(requests):
    context = {}
    if requests.method == 'POST':
        form = ContactForm(requests.POST)
        if form.is_valid():
            send_messege(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['messege'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        requests,
        'contact.html',
    context=context
    )


def send_messege(name, email, messege):
    text = get_template('messege.html')
    html = get_template('messege.html')
    context = {'name': name, 'email': email, 'messege': messege}
    subject = 'Сообщение от пользователя'
    from_email = 'from@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['gorelov2895@yandex.ru'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

