from django.db import models

# Create your models here.
class Login(models.Model):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=20,default=0)

class Station(models.Model):
    stationid=models.CharField(max_length=50,unique=True)
    addressline1=models.CharField(max_length=250)
    addressline2=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    city=models.CharField(max_length=200)
    contactno=models.CharField(max_length=200)
    loginid=models.ForeignKey('Login',on_delete=models.CASCADE)
    def __str__(self):
        return self.addressline1
class Hospital(models.Model):
    hospitalname=models.CharField(max_length=50,unique=True)
    hospitaladdress=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    district=models.CharField(max_length=250)
    state=models.CharField(max_length=200)
    loginid=models.ForeignKey('Login',on_delete=models.CASCADE)
class User(models.Model):
    name=models.CharField(max_length=50,unique=True)
    address=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    age=models.CharField(max_length=250)
    contactno=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    loginid=models.ForeignKey('Login',on_delete=models.CASCADE)
class Missingperson(models.Model):
    name=models.CharField(max_length=50,unique=True)
    missingpersonpic=models.ImageField(upload_to='image')
    gender=models.CharField(max_length=250)
    age=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    missingdate=models.CharField(max_length=200)
    missingplace=models.CharField(max_length=200)
    height=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)
    identificationmark=models.CharField(max_length=200)
    bloodgroup=models.CharField(max_length=200)
    stationid=models.ForeignKey('Station',on_delete=models.CASCADE)
    userid=models.ForeignKey('Login',on_delete=models.CASCADE,related_name='userid')
    currentdate=models.DateField(auto_now_add=True)
class UserComp(models.Model):
    userid=models.ForeignKey('Login',on_delete=models.CASCADE)
    complaint=models.TextField(max_length=300)
    subject=models.CharField(max_length=200)
    currentdate=models.DateField(auto_now_add=True)
    replay=models.TextField(max_length=500,null=True,blank=True)
class Acciedent(models.Model):
    userid=models.ForeignKey('Login',on_delete=models.CASCADE,related_name='accidentid')
    city=models.CharField(max_length=200)
    district=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    currentdate=models.DateField(auto_now_add=True)
    accidentdetails=models.CharField(max_length=200)
    media=models.ImageField(upload_to='image',blank=True)
class StationEnquiry(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    user = models.ForeignKey(Login, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)  # New field for station reply
    current_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry by {self.name} for {self.station.stationid}"
class HospitalEnquiry(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    current_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enquiry from {self.station.stationid} to {self.hospital.hospitalname}"
    
class CaseSheet(models.Model):
    hospital = models.ForeignKey('Login', on_delete=models.CASCADE) 
    patient_name = models.CharField(max_length=100)
    address = models.TextField()
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    contact_no = models.CharField(max_length=15)
    other_details = models.TextField(blank=True, null=True)
    current_date = models.DateField(auto_now_add=True)
    file = models.ImageField(upload_to='image',blank=True)
    postmortem_report = models.FileField(upload_to='postmortem_reports/', blank=True, null=True)
    def __str__(self):
        return f"Case Sheet for {self.patient_name} - {self.hospital.email}"  
   


        