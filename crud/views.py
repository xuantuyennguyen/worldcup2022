from django.shortcuts import render, redirect
from .models import CauThu, DoiTuyen, LichThiDau, Member

# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'crud/index.html', context)

def create(request):
    member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'])
    member.save()
    return redirect('/')

def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'crud/edit.html', context)

def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.save()
    return redirect('/crud/')

def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return redirect('/crud/')

# Đội tuyển
def doituyen(request, bang):
    doituyens = DoiTuyen.objects.filter(bang=bang)
    context = {'doituyens': doituyens}
    context['bang'] = bang 
    context['active'] = bang
    return render(request, 'doituyen/index.html', context)

def doituyen_create(request):
    data = DoiTuyen(name=request.POST['name'], bang=request.POST['bang'])
    data.save()
    bang = request.POST['bang']
    return redirect('/bang/'+bang)

def doituyen_edit(request, id):
    doituyens = DoiTuyen.objects.get(id=id)
    context = {'doituyens': doituyens}
    return render(request, 'doituyen/edit.html', context)

def doituyen_update(request, id):
    data = DoiTuyen.objects.get(id=id)
    data.name = request.POST['name']
    data.bang = request.POST['bang']
    data.save()
    return redirect('/bang/'+ data.bang)

def doituyen_delete(request, bang, id):
    data = DoiTuyen.objects.get(id=id)
    data.delete()
    return redirect('/bang/'+bang)

# Cập nhật cầu thủ
def cauthu(request, doituyen):
    cauthus = CauThu.objects.filter(doituyen=doituyen)
    context = {'cauthus': cauthus}
    context['doituyen'] = doituyen 
    return render(request, 'cauthu/index.html', context)

def cauthu_create(request):
    data = CauThu(
                    doituyen=request.POST['doituyen'], 
                    ten=request.POST['ten'],
                    namsinh=request.POST['namsinh'],
                    vitri=request.POST['vitri'],
                    chieucao=request.POST['chieucao'],
                    cannang=request.POST['cannang'],
                )
    data.save()
    doituyen = request.POST['doituyen']
    return redirect('/cauthu/'+doituyen)

def cauthu_delete(request,doituyen, id):
    data = CauThu.objects.get(id=id)
    data.delete()
    return redirect('/cauthu/'+doituyen)

def cauthu_edit(request, doituyen, id):
    cauthu = CauThu.objects.get(id=id)
    context = {}
    context['cauthu'] = cauthu
    context['doituyen'] = doituyen
    return render(request, 'cauthu/edit.html', context)

def cauthu_update(request, doituyen, id):
    data = CauThu.objects.get(id=id)
    data.ten = request.POST['ten']
    data.vitri = request.POST['vitri']
    data.namsinh = request.POST['namsinh']
    data.chieucao = request.POST['chieucao']
    data.cannang = request.POST['cannang']
    data.save()
    return redirect('/cauthu/'+ doituyen)

# Lịch thi đấu
def lichthidau(request):
    
    doituyenAs = DoiTuyen.objects.filter(bang='a')
    doituyenBs = DoiTuyen.objects.filter(bang='b')
    context = {}
    context['active'] = 'lichthidau'
    context['doituyenAs'] = doituyenAs
    context['doituyenBs'] = doituyenBs

    LichThiDauAs = LichThiDau.objects.filter(bang='a')
    LichThiDauBs = LichThiDau.objects.filter(bang='b')

    context['LichThiDauAs'] = LichThiDauAs
    context['LichThiDauBs'] = LichThiDauBs

    return render(request, 'lichthidau/index.html', context)

def lichthidau_create(request):
    data = LichThiDau(
                        bang=request.POST['bang'],
                        doi1=request.POST['doi1'],
                        kq1='-1',
                        doi2=request.POST['doi2'],
                        kq2='-1',
                        ngay=request.POST['ngay'],
                        gio=request.POST['gio'],
                        san=request.POST['san'],
                    )
    data.save()
    return redirect('/lich-thi-dau')

def lichthidau_edit(request, id):
    ketqua = LichThiDau.objects.get(id=id)
    context = {'ketqua': ketqua}
    return render(request, 'lichthidau/edit.html', context)

def lichthidau_update(request, id):
    data = LichThiDau.objects.get(id=id)
    data.kq1 = request.POST['kq1']
    data.kq2 = request.POST['kq2']
    data.save()
    return redirect('/lich-thi-dau/')

def lichthidau_delete(request, id):
    data = LichThiDau.objects.get(id=id)
    data.delete()
    return redirect('/lich-thi-dau/')

def tuoitrungbinh(request):
    thongke = CauThu.objects.raw('SELECT doituyen as id, doituyen,  ROUND(avg(2021 - namsinh), 1) as tuoi FROM crud_cauthu GROUP BY doituyen')

    doituyen = []
    tuoi = []

    for item in thongke: 
        doituyen.append(item.doituyen)
        tuoi.append(item.tuoi)

    data = {}
    data['active'] = 'tuoitrungbinh'
    data['thongke'] = thongke
    data['doituyen'] = doituyen
    data['tuoi'] = tuoi

    return render(request, 'phantich/tuoitrungbinh.html', data)

def chieucaotrungbinh(request):
    thongke = CauThu.objects.raw('SELECT doituyen as id, doituyen, ROUND(avg(chieucao), 1) as chieucao FROM crud_cauthu GROUP BY doituyen')

    doituyen = []
    chieucao = []

    for item in thongke: 
        doituyen.append(item.doituyen)
        chieucao.append(item.chieucao)

    data = {}
    data['active'] = 'chieucaotrungbinh'
    data['thongke'] = thongke
    data['doituyen'] = doituyen
    data['chieucao'] = chieucao
    
    return render(request, 'phantich/chieucaotrungbinh.html', data)