from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def welcome(request):
    year = request.GET['year']
    year = int(year)
    month=request.GET['month']
    # month=int(month)
    day=request.GET['day']
    # day=int(day)
    name=request.GET['name']
    thisYear=2025
    age=thisYear-year+1
    return render(request, 'welcome.html',{'name':name, 'month':month, 'year':year, 'day':day,'age':age})

#가상환경생성>장고설치>프로젝트>앱>서버 명령어순서
#(views.py)딕셔너리,name="",GET메서드
#(settings) 앱등록
#(html) form시맨틱태그,name=""
#(url.py)from welcome_app import views