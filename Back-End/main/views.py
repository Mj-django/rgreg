import json

from django.shortcuts import render
from django.views import View
from .models import user, user_as, file
from django.http import Http404, JsonResponse
from django.core import serializers


# Create your views here.
class main_slug(View):

    def get(self, request, slug):
        # request.session['username'] = 'mjghaaaaa'
        # request.session['password'] = 'tisno'
        # request.session['pk'] = 52
        if slug == 'users':
            try:
                if f := user_as.objects.get(username=user.objects.get(username=request.session['username']),
                                            password=request.session['password'], is_active=True, is_admin=True):
                    return render(
                        request,
                        'main.html',
                        {
                            'ad_ac': True,
                            'user': f,
                            'filter': 'all',
                            'users': user_as.objects.all() if len(
                                user_as.objects.all()) < 50 else user_as.objects.all()[-1:-20:-1]
                        }
                    )
                else:
                    return Http404
            except:
                return Http404


class main(View):
    def post(self, request):
        if (name_form := request.POST['name_form']) == 'edit_user':
            if user_as.objects.get(
                    username=user.objects.get(username=request.session['username']),
                    password=request.session['password'],
                    is_active=True,
                    is_admin=True
            ):
                request.session['select_username'] = request.POST['wed']
                h = (user_as.objects.get(
                    username=user.objects.get(
                        pk=int(request.POST['wed'])
                    )
                )
                )
                j = {}
                s = 0
                for js in h.profile_image.all():
                    j[f'{s + 1}'] = js.the_file.url
                    s += 1
                if not j:
                    j = ''
                return JsonResponse(
                    {
                        'username': h.username.username,
                        'admin': h.is_admin,
                        'active': h.is_active,
                        'fn': h.first_name,
                        'ln': h.last_name,
                        'imgp': j,
                        'pn': h.phone_number,
                    }
                )

        elif name_form == 'edit_user_tk':
            if user_as.objects.get(
                    username=user.objects.get(username=request.session['username']),
                    password=request.session['password'],
                    is_active=True,
                    is_admin=True
            ):
                if request.POST['active'] and request.POST['admin'] and request.POST['username'] and not (j := not (
                        user.objects.get(pk=request.session['select_username']).username == request.POST[
                    'username'] or not user.objects.filter(username=request.POST['username']))):

                    the_user = user_as.objects.get(
                        username=user.objects.get(pk=int(request.session['select_username'])))
                    x = the_user.username
                    x.username = request.POST['username']
                    x.save()
                    the_user.is_admin = True if request.POST['admin'] == 'true' else False
                    the_user.is_active = True if request.POST['active'] == 'true' else False
                    if request.POST['is_image'] == 'true':
                        for image in the_user.profile_image.all():
                            the_user.profile_image.remove(image)
                        for image in request.FILES.getlist('image_profile'):
                            the_user.profile_image.add(file.objects.create(the_file=image))
                    if request.POST['phone_number']:
                        the_user.phone_number = request.POST['phone_number']
                    else:
                        the_user.phone_number = None
                    the_user.last_name = request.POST['last_name']
                    the_user.first_name = request.POST['first_name']
                    the_user.save()
                    if int(request.session['select_username']) == int(request.session['pk']):
                        request.session['username'] = request.POST['username']
                    request.session['select_username'] = user.objects.get(username=request.POST['username']).pk

                    is_success = True
                else:
                    is_success = False
                if is_success:
                    return JsonResponse(
                        {
                            'success': True,

                        }

                    )
                else:
                    return JsonResponse(
                        {
                            'success': False,
                            'username_found': not j,
                            'username_kh': True if not request.POST['username'] else False,
                            'active_kh': True if not request.POST['active'] else False,
                            'admin_kh': True if not request.POST['admin'] else False,

                        }
                    )
        elif name_form == 'del_user':
            if user_as.objects.get(
                    username=user.objects.get(username=request.session['username']),
                    password=request.session['password'],
                    is_active=True,
                    is_admin=True
            ):
                try:
                    the_user = user_as.objects.get(username=(u := user.objects.get(pk=int(request.POST['user']))))
                    the_user.delete()
                    u.delete()
                    s = True
                except:
                    s = False
                return JsonResponse(
                    {
                        'succes': s
                    }
                )
        elif name_form == 'create_user_tk':
            try:
                the_user = user_as.objects.create(
                    username=user.objects.create(username=request.POST['username']),
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    phone_number=request.POST['phone_number'] if request.POST['phone_number'] else None,
                    is_admin=True if request.POST['admin'] == 'true' else False,
                    is_active=True if request.POST['active'] == 'true' else False,
                    password=request.POST['password']
                )
                for image in request.FILES.getlist('image_profile'):
                    the_user.profile_image.add(file.objects.create(the_file=image))
                the_user.save()
                return JsonResponse(
                    {
                        'username': the_user.username.username,
                        'pk': the_user.pk,
                        'success': True
                    }
                )
            except:
                return JsonResponse(
                    {
                        'success': False
                    }
                )
