from django import forms
from .models import *


class Stationregform(forms.ModelForm):
    class Meta:
        model=Station
        fields=['stationid','addressline1','addressline2','district','city','contactno']
class Loginregform(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email','password']
        widget={
            'password':forms.PasswordInput()
        }
class Hospitalregform(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=['hospitalname','hospitaladdress','city','district','state']
class LoginCheck(forms.Form):
    email=forms.CharField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput)  
class Userregform(forms.ModelForm):
     class Meta:
        model=User
        fields=['name','address','gender','age','contactno','city','district','state']
class UserEditform(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','address','gender','age','contactno','city','district','state']
class HospitalEditform(forms.ModelForm):
    class Meta:
        model=Hospital
        fields=['hospitalname','hospitaladdress','city','district','state']
class StationEditform(forms.ModelForm):
    class Meta:
        model=Station
        fields=['stationid','addressline1','addressline2','district','city','contactno']        
class missingpersonregform(forms.ModelForm):
    stationid=forms.ModelChoiceField(queryset=Station.objects.all(),widget=forms.Select())
    class Meta:
        model=Missingperson
        fields=['name','missingpersonpic','gender','age','address','missingdate','missingplace','height','weight','identificationmark','bloodgroup']        
        
class complaint(forms.ModelForm):      
    class Meta:
        model=UserComp
        fields=['subject','complaint']      

class ComplaintReplyForm(forms.ModelForm):
    class Meta:
        model=UserComp
        fields=['replay']    

class acciedentregform(forms.ModelForm):
    class Meta:
        model=Acciedent
        fields=['city','district','location','accidentdetails','media']

class StationEnquiryForm(forms.ModelForm):
    class Meta:
        model = StationEnquiry
        fields = ['name', 'email', 'message']
class StationEnquiryReplyForm(forms.ModelForm):
    class Meta:
        model = StationEnquiry
        fields = ['reply']
        widgets = {
            'reply': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your reply here...'}),
        }