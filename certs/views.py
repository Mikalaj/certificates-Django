from django.shortcuts import render, redirect, get_object_or_404
from certs.models import Wedding, Baptism
from django.forms import ModelForm
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from .serializers import BaptismSerializer
from rest_framework.renderers import JSONRenderer


from django.contrib.auth.models import User, Group
from rest_framework import viewsets


class BaptismForm(ModelForm):
    class Meta:
        model = Baptism
        fields = ['date', 'number', 'priest', 'certificate',
                  'baptized_name', 'baptized_middle_name', 'baptized_surname',
                  'godfather', 'godmother', 'saint_name', 'saint_date']


class WeddingForm(ModelForm):
    class Meta:
        model = Wedding
        fields = ['date', 'number', 'priest', 'certificate',
                  'fiance_name', 'fiance_middle_name', 'fiance_surname',
                  'fiancee_name', 'fiancee_middle_name', 'fiancee_surname',
                  'witness1', 'witness2']

    # def __init__(self, *args, **kwargs):
    #     super(ModelForm, self).__init__(*args, **kwargs)
    # adding css classes to widgets without define the fields:
    # for field in self.fields:
    #     self.fields[field].widget.attrs['class'] = 'form-control-plaintext'

    # def as_div(self):
    #     return self._html_output(
    #         normal_row=u'<div%(html_class_attr)s>%(label)s %(field)s %(help_text)s %(errors)s</div>',
    #         error_row=u'<div class="error">%s</div>',
    #         row_ender='</div>',
    #         help_text_html=u'<div class="hefp-text">%s</div>',
    #         errors_on_separate_row=False)


class ReadOnlyBaptismForm(BaptismForm):
    def __init__(self, *args, **kwargs):
        super(BaptismForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['readonly'] = True


class ReadOnlyWeddingForm(WeddingForm):
    def __init__(self, *args, **kwargs):
        super(WeddingForm, self).__init__(*args, **kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs['readonly'] = True


# Methods fo Baptism
@login_required
def baptism_list(request, template_name='certs/baptism_list.html'):
    baptisms = Baptism.objects.all()
    data = dict()
    data['object_list'] = baptisms
    return render(request, template_name, data)


@login_required
def baptism_detail(request, pk, template_name='certs/baptism_detail.html'):
    baptism = get_object_or_404(Baptism, pk=pk)
    form = ReadOnlyBaptismForm(instance=baptism)
    return render(request, template_name,
                  {'form': form, 'baptism': baptism})


@login_required
def baptism_create(request, template_name='certs/baptism_form.html'):
    form = BaptismForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('baptism_list')
    return render(request, template_name, {'form': form})


@login_required
def baptism_update(request, pk, template_name='certs/baptism_form.html'):
    baptism = get_object_or_404(Baptism, pk=pk)
    form = BaptismForm(request.POST or None, request.FILES or None, instance=baptism)
    if form.is_valid():
        form.save()
        return redirect('baptism_list')
    return render(request, template_name, {'form': form})


@login_required
def baptism_delete(request, pk, template_name='certs/baptism_confirm_delete.html'):
    baptism = get_object_or_404(Baptism, pk=pk)
    if request.method == 'POST':
        default_storage.delete(baptism.certificate)
        baptism.delete()
        return redirect('baptism_list')
    return render(request, template_name, {'object': baptism})


# End of methods of Baptism


# Methods of Wedding
@login_required
def wedding_list(request, template_name='certs/wedding_list.html'):
    weddings = Wedding.objects.all()
    data = dict()
    data['object_list'] = weddings
    return render(request, template_name, data)


@login_required
def wedding_detail(request, pk, template_name='certs/wedding_detail.html'):
    wedding = get_object_or_404(Wedding, pk=pk)
    form = ReadOnlyWeddingForm(instance=wedding)
    return render(request, template_name, {'form': form, 'wedding': wedding})


@login_required
def wedding_create(request, template_name='certs/wedding_form.html'):
    form = WeddingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('wedding_list')
    return render(request, template_name, {'form': form})


@login_required
def wedding_update(request, pk, template_name='certs/wedding_form.html'):
    wedding = get_object_or_404(Wedding, pk=pk)
    form = WeddingForm(request.POST or None, request.FILES or None, instance=wedding)
    if form.is_valid():
        form.save()
        return redirect('wedding_list')
    return render(request, template_name, {'form': form, 'wedding': wedding})


@login_required
def wedding_delete(request, pk, template_name='certs/wedding_confirm_delete.html'):
    wedding = get_object_or_404(Wedding, pk=pk)
    if request.method == 'POST':
        default_storage.delete(wedding.certificate)
        wedding.delete()
        return redirect('wedding_list')
    return render(request, template_name, {'object': wedding})


def index(request):
    return render(request, "certs/index.html", {})