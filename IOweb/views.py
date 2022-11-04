from django.shortcuts import render
import os
import pandas as pd
from django.http import HttpResponse, Http404
import datetime
from django.template import Context, Template
from django.template.loader import get_template
from IOweb import models


# Create your views here.
file_path = os.path.abspath(os.path.join(os.getcwd()))
activity_record = [fr'images\activity_record\{i}' for i in os.listdir(fr'{file_path}\static\images\activity_record')]
member_images = [fr'images\member\{i}' for i in os.listdir(fr'{file_path}\static\images\member')]


#静态页面
def hello(request):
    return HttpResponse("Hello World")

#动态内容/DTL模板
def current_datatime(request):

    now = datetime.datetime.now()
    t = get_template('current_datetime.html')
    # t = Template("<html><body> It is now {{current_date}}. </body></html>")
    html = t.render({"current_date":now})
    return  HttpResponse(html)

#通配url
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse(f'In {offset} hour, it will be {dt}')


def IO_web(request):
    t = get_template('IO_web.html')
    activie_time = '周五'
    html = t.render({
        'current_data': activie_time,
        'title':'艾欧工作室',
        'member':models.user.objects.all(),
        'activity_images':activity_record,
    })
    return HttpResponse(html)

def IO_members(request, member_id):

    try:
        member_id = int(member_id)
    except ValueError:
        raise Http404()

    member = models.user.objects.get(id=member_id)

    t = get_template('IO_members.html')
    text = pd.read_table(fr'{file_path}\static\text\member{member_id}_selfintroduce')

    html = t.render(
        {
            'membername': member.username,
            'self_introduce': text.columns[0],
            'path':f'images/member/member{member_id}.png',
        }
    )
    return HttpResponse(html)


def test(request):
    member = models.user.objects.all()
    username = models.user.objects.get(id='1')
    picturelist = [fr'images\activity_record\{i}' for i in os.listdir(fr'{file_path}\static\images\activity_record')]
    return render(
        request, 
        'test.html',
        {
            'member': member,
            'username':username.username,
            'length':len(member),
            'picturelist':picturelist,
        }
    )
