from django.shortcuts import render,redirect

# Create your views here.
from students.models import student
from students.form import PostForm
def listone(request): 
    try: 
        unit = student.objects.get(stdName="NL") #讀取一筆資料
    except:
        errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):  
    allStudents = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())

def post(request):
    if request.method == "POST":
        mess = request.POST['stdName'] + " " + request.POST['stdID'] + " " + request.POST['stdSex'] + " " + request.POST['stdBirth']
    else:
        mess = "表單資料尚未送出!"
    return render(request,"addstudent.html",locals())

def post1(request):
    if request.method == "POST":
        stdName = request.POST['stdName']
        stdID = request.POST['stdID']
        stdSex = request.POST['stdSex']
        stdBirth = request.POST['stdBirth']
        stdEmail = request.POST['stdEmail']
        stdPhone = request.POST['stdPhone']
        stdAddress = request.POST['stdAddress']

        unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdEmail=stdEmail, stdPhone=stdPhone, stdAddress=stdAddress)
        unit.save()#寫入資料庫
        return redirect('/listall')
    else:
        message = '請輸入資料(資料不作驗證)'
    return render(request, "addstudent.html",locals())

def postform(request):
    #新增PostForm表單物件
    stdform = PostForm()
    # stdName = request.POST['stdName']
    # stdID = request.POST['stdID']
    # stdSex = request.POST['stdSex']
    # stdBirth = request.POST['stdBirth']
    # stdEmail = request.POST['stdEmail']
    # stdPhone = request.POST['stdPhone']
    # stdAddress = request.POST['stdAddress']
    # unit = student.objects.create(stdName=stdName, stdID=stdID, stdSex=stdSex, stdBirth=stdBirth, stdEmail=stdEmail, stdPhone=stdPhone, stdAddress=stdAddress) 
    # unit.save()  #寫入資料庫
    return render(request,"stdform.html",locals())

def delete(request, stdID=None):
    if stdID != None:
        if request.method == "POST":
            stdID = request.POST["stdID"]
        #嘗試抓取此id學生資料
        try:
            unit = student.objects.get(stdID=stdID)
            #刪除該資料
            unit.delete()
            return redirect('/listall')
        except:
            mess = "查無該學號"
    return render(request, "delete.html", locals())


def edit(request, stdID=None, mode=None):
    if mode == "edit":
        unit = student.objects.get(stdID=stdID)
        unit.stdName = request.GET["stdName"]
        unit.stdID = request.GET["stdID"]
        unit.stdSex = request.GET["stdSex"]
        unit.stdBirth = request.GET["stdBirth"]
        unit.stdEmail = request.GET["stdEmail"]
        unit.stdPhone = request.GET["stdPhone"]
        unit.stdAddress = request.GET["stdAddress"]
        unit.save()
        mess = "已修改完成"
        return redirect('/listall')
    else:
        try:
            unit = student.objects.get(stdID=stdID)
            strDate = str(unit.stdBirth)
            strDate2 = strDate.replace(" 年 ", "-")
            strDate2 = strDate.replace(" 月 ", "-")
            strDate2 = strDate.replace(" 日 ", "-")
            unit.stdBirth = strDate2
        except:
            mess = "此學號不存在"
        return render(request, "edit.html", locals())