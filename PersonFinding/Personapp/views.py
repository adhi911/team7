from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib import messages
from django.db.models import Q
from .models import *
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'loginindex.html')
def adminhome(request):
    return render(request,'adminindex.html')
def Stationregister(request):
    if request.method=='POST':
        form=Stationregform(request.POST)
        logform=Loginregform(request.POST)
        if form.is_valid() and logform.is_valid():
            a=logform.save(commit=False)
            a.usertype='station'
            a.save()
            b=form.save(commit=False)
            b.loginid=a
            b.save()
            messages.success(request,'User data saved successfully!')
            return redirect('logins')
    else:
         form = Stationregform()
         logform=Loginregform()
    return render(request, 'user_form.html',{'form': form,'logform':logform})
def Hospitalregister(request):
    if request.method=='POST':
        form=Hospitalregform(request.POST)
        logform=Loginregform(request.POST)
        if form.is_valid() and logform.is_valid():
            a=logform.save(commit=False)
            a.usertype='hospital'
            a.save()
            b=form.save(commit=False)
            b.loginid=a
            b.save()
            messages.success(request,'User data saved successfully!')
            return redirect('logins')
    else:
         form = Hospitalregform()
         logform=Loginregform()
    return render(request, 'hospital_form.html',{'form': form,'logform':logform})
def Userregister(request):
    if request.method=='POST':
        form=Userregform(request.POST)
        logform=Loginregform(request.POST)
        if form.is_valid() and logform.is_valid():
            a=logform.save(commit=False)
            a.usertype='user'
            a.save()
            b=form.save(commit=False)
            b.loginid=a
            b.save()
            messages.success(request,'User data saved successfully!')
            return redirect('logins')
    else:
         form = Userregform()
         logform=Loginregform()
    return render(request, 'userloginform.html',{'form': form,'logform':logform})
def Station_list_view(request):
    users=Station.objects.all()
    return render(request,'stationtable.html',{'users':users})
def Hospital_list_view(request):
    users=Hospital.objects.all()
    return render(request,'hospitaltable.html',{'users':users})
def User_list_view(request):
    users=User.objects.all()
    return render(request,'usertable.html',{'users':users})
def user_edit(request,id):
    users=get_object_or_404(User,id=id)
    if request.method=='POST':
        form=Userregform(request.POST,instance=users)
        if form.is_valid():
            form.save()
            return redirect('usertable')
    else:
         form = Userregform(instance=users)
    return render(request,'edit.html',{'form': form})
def custom_login_view(request):
    if request.method=='POST':
        form=LoginCheck(request.POST)
        if form.is_valid():
            username=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                user=Login.objects.get(email=username)
                if user.password==password:
                    if user.usertype=='user':
                        request.session['user_id']=user.id
                        return redirect('userhome')
                    elif user.usertype=='station':
                        request.session['station_id']=user.id
                        return redirect('stationhome')
                    elif user.usertype=='hospital':
                        request.session['hospital_id']=user.id
                        return redirect('hospitalhome')
                else:
                    messages.error(request,'invalid password') 
            except User.DoesNotExist:
                messages.error(request,'user does not exist')
    else:
        form=LoginCheck()
    return render(request,'loginindex.html',{'form':form})
def userhome(request):
    return render(request,'userhome.html')
def stationhome(request):
    return render(request,'stationhome.html')
def hospitalhome(request):
    return render(request,'hospitalhome.html')
def userhomeprofile(request):
    userid=request.session.get('user_id')
    login_detail=get_object_or_404(Login,id=userid)
    data=get_object_or_404(User,loginid=login_detail)
    if request.method=='POST':
        form=UserEditform(request.POST,instance=data)
        form1=Loginregform(request.POST,instance=login_detail)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('userhome')
    else:
        form=UserEditform(instance=data)
        form1=Loginregform(instance=login_detail)
    return render(request,'userprofile.html',{'form':form,'form1':form1})

def hospitalhomeprofile(request):
    userid=request.session.get('hospital_id')
    login_detail=get_object_or_404(Login,id=userid)
    data=get_object_or_404(Hospital,loginid=login_detail)
    if request.method=='POST':
        form=HospitalEditform(request.POST,instance=data)
        form1=Loginregform(request.POST,instance=login_detail)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('hospitalhome')
    else:
        form=HospitalEditform(instance=data)
        form1=Loginregform(instance=login_detail)
    return render(request,'hospitalprofile.html',{'form':form,'form1':form1})

def stationhomeprofile(request):
    userid=request.session.get('station_id')
    login_detail=get_object_or_404(Login,id=userid)
    data=get_object_or_404(Station,loginid=login_detail)
    print("userid..",data)
    if request.method=='POST':
        form=StationEditform(request.POST,instance=data)
        form1=Loginregform(request.POST,instance=login_detail)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect('stationhome')
    else:
        form=StationEditform(instance=data) 
        form1=Loginregform(instance=login_detail)
    return render(request,'stationprofile.html',{'form':form,'form1':form1})
            
def stationsearch(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        stations = Station.objects.filter(
            Q(stationid__icontains=query) |
            Q(addressline1__icontains=query) |
            Q(addressline2__icontains=query) |
            Q(district__icontains=query) |
            Q(city__icontains=query) |
            Q(contactno__icontains=query)
        )
        
        # Check if no results were found
        if not stations:
            messages.error(request, 'No results found.')
        
        return render(request, 'stationsearch.html', {'stations': stations})
    else:
        return render(request, 'stationsearch.html')        
    
def hospitalsearch(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        stations = Hospital.objects.filter(
            Q(hospitalname__icontains=query) |
            Q(hospitaladdress__icontains=query) |
            Q(city__icontains=query) |
            Q(district__icontains=query) |
            Q(state__icontains=query)
        )
        
        # Check if no results were found
        if not stations:
            messages.error(request, 'No results found.')
        
        return render(request, 'hospitalsearch.html', {'stations': stations})
    else:
        return render(request, 'hospitalsearch.html')            
def missform(request):
    logid = request.session.get('user_id')
    loddata = get_object_or_404(Login,id=logid)
    if request.method == 'POST':
        miss=missingpersonregform(request.POST,request.FILES)
        if miss.is_valid():
            var=miss.cleaned_data['stationid']
            print(var)
            missdata=miss.save(commit=False)
            missdata.userid = loddata
            missdata.stationid=var
            missdata.save()
            return redirect('userhome')
    else:
        miss=missingpersonregform()
    return render(request,'missingperson.html',{'miss':miss})

def user_list_view(request):
    users=Missingperson.objects.all()
    return render(request,'Editpersonform.html',{'users':users})
def user_delete(request,id):
    user=get_object_or_404(Missingperson,id=id)
    user.delete()
    return redirect('table')   
def user_edit(request,id):
    users=get_object_or_404(Missingperson,id=id)
    if request.method=='POST':
        form=missingpersonregform(request.POST,request.FILES,instance=users)
        if form.is_valid():
            form.save()
            return redirect('table')
    else:
         form = missingpersonregform(instance=users)
    return render(request,'edit.html',{'form': form})

def station_missing_details(request):
    session_id = request.session.get('station_id')
    loddata = get_object_or_404(Station,loginid=session_id)  
    missing_persons = Missingperson.objects.filter(stationid=loddata)
    return render(request, 'registerview.html', {'missing_persons': missing_persons})

def missing_list_view(request):
    session_id = request.session.get('station_id')
    loddata = get_object_or_404(Station,loginid=session_id)  
    missing_persons = Missingperson.objects.all()
    return render(request, 'registerview.html', {'missing_persons': missing_persons})

def create_complaint(request): 
    if request.method=='POST':
        form=complaint(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            user=get_object_or_404(Login,id=request.session['user_id'])
            a.userid=user
            a.save()
            return redirect('userhome')
    else:
            form = complaint()
    return render(request,'user_complaint.html',{'form': form})
def ViewComplaints (request):
    complaints=UserComp.objects.all()
    return render(request, 'complaintview.html', {'form': complaints})

def ListComplaints (request):
    user=get_object_or_404(Login,id=request.session['user_id'])
    complaints=UserComp.objects.filter(userid=user)
    return render(request, 'listcomplaints.html', {'form':complaints})

def EditComplaint(request, id):
    complaints=get_object_or_404(UserComp, id=id)
    if request.method=="POST":
        form =complaint(request.POST, instance=complaints)
        if form.is_valid():
            form.save()
            messages.success (request, 'Complaint edited successfully')
            return redirect('ListComplaints')
    else:
        form=complaint(instance=complaints)
    return render(request, 'public_complaint.html', {'form': form})

def DeleteComplaint (request,id):
    complaint=get_object_or_404(UserComp, id=id)
    complaint.delete()
    messages.success (request, 'Complaint deleted successfully')
    return redirect('ListComplaints')
def ComplaintReply (request,id):
    complaint=get_object_or_404(UserComp,id=id)
    if request.method=="POST":
        form=ComplaintReplyForm (request.POST,instance=complaint)
        if form.is_valid():
            form.save()
            messages.success (request, 'Complaint edited successfully')
            return redirect('ViewComplaints')
    else:
        form=ComplaintReplyForm(instance=complaint)
    return render(request, 'reply.html', {'form': form,'complaint':complaint})

def ShowReply (request,id):
    complaint=get_object_or_404(UserComp, id=id)
    return render(request, 'view_reply.html', {'complaint':complaint})

def accidentregform(request):
    id=request.session['user_id']
    a=get_object_or_404(Login,id=id)
    if request.method == 'POST':
        form = acciedentregform(request.POST, request.FILES)
        if form.is_valid():
            accident = form.save(commit=False)
            accident.userid = a
            accident.save()
            return redirect('userhome') 
    else:
        form = acciedentregform()
    return render(request, 'register_accident.html', {'form': form})

def ListAccident (request):
    user=get_object_or_404(Login,id=request.session['user_id'])
    complaints=Acciedent.objects.filter(userid=user)
    return render(request, 'listaccident.html', {'form':complaints})

def accident_edit(request, id):
    complaints=get_object_or_404(Acciedent, id=id)
    if request.method=="POST":
        form =acciedentregform(request.POST,request.FILES, instance=complaints)
        if form.is_valid():
            form.save()
            messages.success (request, 'Complaint edited successfully')
            return redirect('ListAccident')
    else:
        form=acciedentregform(instance=complaints)
    return render(request, 'accident_edit.html', {'form': form})

def accident_delete (request,id):
    complaint=get_object_or_404(Acciedent, id=id)
    complaint.delete()
    messages.success (request, 'Complaint deleted successfully')
    return redirect('ListAccident')

def station_accidents(request):
    station_id = request.session.get('station_id')
    if not station_id:
        messages.error(request, "Session expired. Please login again.")
        return redirect('login')
    station = get_object_or_404(Station, loginid=station_id)
    accidents = Acciedent.objects.filter(city=station.city)
    return render(request, 'station_accidents.html', {'station': station, 'accidents': accidents})
def station_enquiry(request, station_id):
    station = get_object_or_404(Station, id=station_id)
    if request.method == 'POST':
        form = StationEnquiryForm(request.POST)
        if form.is_valid():
            enquiry = form.save(commit=False)
            enquiry.station = station 
            if 'user_id' in request.session:
                enquiry.user = get_object_or_404(Login, id=request.session['user_id'])
            else:
                enquiry.user = None 
            enquiry.save()
            messages.success(request, "Your enquiry has been submitted successfully!")
            return redirect('stationsearch')
    else:
        form = StationEnquiryForm()
    return render(request, 'station_enquiry_form.html', {'form': form, 'station': station})
def station_enquiries_list(request):
    station_id = request.session.get('station_id')
    if not station_id:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('login')
    station = get_object_or_404(Station, loginid=station_id)
    enquiries = StationEnquiry.objects.filter(station=station)
    return render(request, 'station_enquiries_list.html', {'station': station, 'enquiries': enquiries})
def station_enquiry_reply(request, enquiry_id):
    enquiry = get_object_or_404(StationEnquiry, id=enquiry_id)
    if request.method == 'POST':
        form = StationEnquiryReplyForm(request.POST, instance=enquiry)
        if form.is_valid():
            form.save()
            messages.success(request, "Reply sent successfully!")
            return redirect('station_enquiries_list')
    else:
        form = StationEnquiryReplyForm(instance=enquiry)
    return render(request, 'station_enquiry_reply.html', {'form': form, 'enquiry': enquiry})
def user_enquiries_list(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, "Session expired. Please log in again.")
        return redirect('login')
    enquiries = StationEnquiry.objects.filter(user_id=user_id).order_by('-current_date')
    return render(request, 'user_enquiries_list.html', {'enquiries': enquiries})
def user_enquiry_edit(request, enquiry_id):
    enquiry = get_object_or_404(StationEnquiry, id=enquiry_id)
    if enquiry.reply:
        messages.error(request, "You cannot edit this enquiry because the station has already replied.")
        return redirect('user_enquiries_list')
    if request.method == 'POST':
        form = StationEnquiryForm(request.POST, instance=enquiry)
        if form.is_valid():
            form.save()
            messages.success(request, "Enquiry updated successfully!")
            return redirect('user_enquiries_list')
    else:
        form = StationEnquiryForm(instance=enquiry)
    return render(request, 'user_enquiry_edit.html', {'form': form, 'enquiry': enquiry})
def user_enquiry_delete(request, enquiry_id):
    enquiry = get_object_or_404(StationEnquiry, id=enquiry_id)
    if enquiry.reply:
        messages.error(request, "You cannot delete this enquiry because the station has already replied.")
        return redirect('user_enquiries_list')
    enquiry.delete()
    messages.success(request, "Enquiry deleted successfully!")
    return redirect('user_enquiries_list')
def custom_logout_view(request):
    request.session.flush()
    return redirect('index')

def case_sheet_add(request):
    id = request.session.get('hospital_id')
    h = get_object_or_404(Login, id = id)
    if request.method == 'POST':
        form = CaseSheetForm(request.POST)
        if form.is_valid():
            case_sheet = form.save(commit=False)
            case_sheet.hospital = h
            case_sheet.save()
            return redirect('hospitalhome')
    else:
        form = CaseSheetForm()
    return render(request, 'case_sheet_form.html', {'form': form})   
 
def case_sheet_list(request):
    id = request.session.get('hospital_id')
    h = get_object_or_404(Login, id = id)
    case_sheets = CaseSheet.objects.filter(hospital = h)
    return render(request, 'case_sheet_list.html', {'case_sheets': case_sheets})

def case_sheet_edit(request, id):
    case_sheet = get_object_or_404(CaseSheet, id=id)
    if request.method == 'POST':
        form = CaseSheetForm(request.POST, instance=case_sheet)
        if form.is_valid():
            form.save()
            return redirect('case_sheet_list')
    else:
        form = CaseSheetForm(instance=case_sheet)
    return render(request, 'case_sheet_form.html', {'form': form})

def case_sheet_delete(request, id):
    case_sheet = get_object_or_404(CaseSheet, id=id)
    case_sheet.delete()
    return redirect('case_sheet_list')

def case_search(request):
    id = request.session.get('hospital_id')
    h = get_object_or_404(Login, id = id)
    if request.method == 'POST':
        query = request.POST.get('search')
        stations = CaseSheet.objects.filter(
            Q(hospital_id=h) &
            Q(patient_name__icontains=query) |
            Q(contact_no__icontains=query) |
            Q(current_date__icontains=query) 
        )
        if not stations:
            messages.error(request, 'No results found.')
        
        return render(request, 'casesearch.html', {'stations': stations})
    else:
        return render(request, 'casesearch.html')        
    
