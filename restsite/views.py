from django.shortcuts import render

from restsite.models import ItemModel


def index(requests):
    menu_brk = ItemModel.objects.filter(type__exact='BRK').order_by('?')[:6]
    menu_lun = ItemModel.objects.filter(type__exact='LUN').order_by('?')[:6]
    menu_din = ItemModel.objects.filter(type__exact='DIN').order_by('?')[:6]
    context = {'menu_brk': menu_brk, 'menu_lun': menu_lun, 'menu_din': menu_din}
    return render(requests,
                  'index.html',
                  context=context
                  )

