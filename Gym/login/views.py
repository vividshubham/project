from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,get_user_model
from .forms import LoginForm,AddUserForm,UserProfileForm,UserProfileForm1,UserProfileForm2,OffersForm,MachineForm,DumbellForm,PlatesAndBarForm,OtherAccessoryForm
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from .models import Machine,Dumbell,PlatesAndBar,OtherAccessory,Offers
from .models import table1,table2,table3,table4,table5,table6,table7,table8,table9,table10,table11,table12
from .models import table13,table14,table15,table16,table17,table18,table19,table20,table21,table22,table23,table24
from .forms import DietForm
from login.models import UserProfile,extras,members,w1_cardio,w1_fullbody,w2_cardio,w2_lowerbody,w3_legs,w2_upperbody,w3_back,w3_cardio,w3_chest
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from datetime import datetime,timedelta,tzinfo
from django.contrib import messages
#from pytz import timezone
# Create your views here.

@csrf_exempt
def home(request):
	form = LoginForm(request.POST or None)
	#form1 = SignUpForm(request.POST or None)
	c = {}
	c.update(csrf(request))
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		utc = UTC()
		today = datetime.now(utc)
		if user is not None and not user.is_staff:
			profile1 = UserProfile.objects.get(user=user)
			days_remaining = user.date_joined + timedelta(days=int(profile1.duration)) - today
			if days_remaining.total_seconds()<=0:
				user1 = User.objects.get(user=user)
				user1.is_active = False
				user1.save()
		if user is not None:
			if user.is_active:
				login(request,user)
				if user.is_staff:
					return render(request,"manager.html",{})
				try:
					profile = UserProfile.objects.get(user=request.user)
					status = profile.status
					print status
					if status=="Member":
						return render(request,"member.html")
					elif status=="Instructor":
						return render(request,"instructor.html",{})
				except:
					return render(request,"signup.html",{})
				#context1 = {
				#"username":username
				#"age":str(user.profile.objects.age)
				#"gender":user.profile.objects.gender
				#}
				return render(request,"member.html",{})
			else:
				raise forms.ValidationError("Invalid Login")
				return HttpResponseRedirect('/')
				message = "Your account has expired"
		else:
			return HttpResponseRedirect('/')
	context = {
	"form" : form
	}
	return render(request,"home.html",context)


ZERO = timedelta(0)

class UTC(tzinfo):
  def utcoffset(self, dt):
    return ZERO
  def tzname(self, dt):
    return "UTC"
  def dst(self, dt):
    return ZERO

@login_required
def profile(request):
	# if not request.user.is_authenticated():
	# 	return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	profile = UserProfile.objects.get(user = request.user)
	username = request.user.username
	gender = profile.gender
	bloodgrp = profile.bloodgrp
	name=profile.user.first_name+" "+profile.user.last_name
	context = {
	'username':username,
	'gender':gender,
	'bloodgrp':bloodgrp,
	'profile':profile,
	'name':name
	}

	return render(request,"profile.html",context)

@login_required
def logout1(request):
	logout(request)
	form = LoginForm(request.POST or None)
	#return render(request,"home.html",{"form":form})
	return HttpResponseRedirect('/')

@login_required
def members1(request):
	u1 = UserProfile.objects.get(user_id=request.user.username)
	mems = u1.instruct.all()
	return render(request,"members.html",{"member_list":mems})


@login_required
def sched_diet(request,user_name):
	return render(request,"choices.html",{"user_name":user_name})


@login_required
def adduser(request):
	form = AddUserForm(request.POST or None)
	if request.method == 'POST':
		if not form.is_valid():
			messages.add_message(request,messages.ERROR,'There was a problem while creating account.')
		else:
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			first_name =form.cleaned_data.get('first_name')
			last_name =form.cleaned_data.get('last_name')

			User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
			form1 = UserProfileForm(request.POST or None)
			return HttpResponseRedirect(username)
	return render(request,"adduser.html",{"form":form})
	# if request.method == 'POST':
	#	form = AddUserForm(request.POST)	
	# 	if not form.is_valid():
	# 		messages.add_message(request,messages.ERROR,'There was a problem while creating your account.')
	# 	else:
	# 		username = form.cleaned_data.get('username')
	# 		email = form.cleaned_data.get('email')
	# 		password = form.cleaned_data.get('password')
	# 		User.objects.create_user(username=username,password=password,email=email)
	# 		return render(request,"addprofile.html",{"form":form})
	# return render(request,"manager.html",{"form":form})


@login_required
def addprofile(request,user_name):
	form = UserProfileForm(request.POST)
	if request.method == 'POST' and form.is_valid():
		user = User.objects.get(username=user_name)
		print user.username
		user1 = UserProfile.objects.get(user=user)
		#user1.name = form.cleaned_data['name']
		user1.age = form.cleaned_data['age']
		user1.status = form.cleaned_data['status']
		user1.gender = form.cleaned_data['gender']
		user1.phoneno = form.cleaned_data['phoneno']
		user1.address = form.cleaned_data['address']
		user1.bloodgrp = form.cleaned_data['bloodgrp']
		user1.duration = form.cleaned_data['duration']
		user1.needs_instructor = form.cleaned_data['needs_instructor']
		user1.save()
		user1 = UserProfile.objects.get(user_id=user_name)
		print user1.user.username
		members.objects.create(member=user1)
		mem = members.objects.get(member=user1)
		print mem
		if user1.needs_instructor is True:
			instructors1 = UserProfile.objects.filter(status="Instructor")
			extra_data0 = extras.objects.get(data='flag')
			extra_data1 = extras.objects.get(data='j')
			members1 = UserProfile.objects.filter(status="Member",needs_instructor=True)
			print instructors1
			if len(members1)<25:
				mem.instructor = instructors1[extra_data0.value]
				print mem.instructor
				mem.save()
				extra_data0.value+=1
				if extra_data0.value==5:
					extra_data0.value=0
				extra_data0.save()
			else:
				extra_data0.value = extra_data0.value+5
				if extra_data1.value<5:
					mem.instructor = instructors1[extra_data0.value]
					mem.save()
					extra_data1.value+=1
					if extra_data1.value==5:
						extra_data1.value=0
						extra_data0.value+=1
					extra_data0.save()
					extra_data1.save()
		return render(request,"manager.html",{})
	return render(request,"addprofile.html",{"form":form})

@login_required
def schedule(request,user_name):
	form = UserProfileForm1(request.POST or None)
	u = UserProfile.objects.get(user_id=user_name)
	utc = UTC()
	today = datetime.now(utc)
	days_completed = today - request.user.date_joined
	if days_completed.total_seconds() <= 7*24*60*60:
		if today.strftime("%A") == 'Monday' or 'Wednesday' or 'Friday':
			exercises = w1_cardio.objects.all()
		else:
			exercises = w1_fullbody.objects.all()
	elif days_completed.total_seconds() <= 14*24*60*60:
		if today.strftime("%A") == 'Monday' or today.strftime("%A") == 'Wednesday' or today.strftime("%A") == 'Friday':
			exercises = w2_cardio.objects.all()
		elif today.strftime("%A") == 'Tuesday' or today.strftime("%A") == 'Saturday':
			exercises = w2_lowerbody.objects.all()
		else:
			exercises = w2_upperbody.objects.all()
	else:
		if today.strftime("%A") == 'Monday' or today.strftime("%A") == 'Thursday':
			exercises = w3_cardio.objects.all()
		elif today.strftime("%A") == 'Tuesday' or today.strftime("%A") == 'Friday':
			exercises = w3_legs.objects.all()
		elif today.strftime("%A") == 'Wednesday' or today.strftime("%A") == 'Saturday':
			exercises = w3_chest.objects.all()
		else:
			exercises = w3_back.objects.all()
	return render(request,"schedule.html",{"exercises":exercises})


@login_required
def diet(request,user_name):
	form = UserProfileForm2(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		u = UserProfile.objects.get(user_id=user_name)
		u.diet = form.cleaned_data['diet']
		u.save()
		return HttpResponseRedirect('/members/'+user_name+'/diet/')
	return render(request,"diet.html",{"form":form})

@login_required
def todaysschedule(request):
	u = UserProfile.objects.get(user_id=request.user.username)
	# if u.needs_instructor is True:
	# 	exercise = u.exercises
	# 	return render(request,"todaysschedule.html",{"exercise":exercise})
	utc = UTC()
	today = datetime.now(utc)
	days_completed = today - request.user.date_joined
	print today.strftime("%A")
	print "dfsfsd"
	if days_completed.total_seconds() <= 7*24*60*60:
		if today.strftime("%A") == "Monday" or "Wednesday" or "Friday":
			exercises = w1_cardio.objects.all()
		else:
			exercises = w1_fullbody.objects.all()
	elif days_completed.total_seconds() <= 14*24*60*60:
		if today.strftime("%A") == "Monday" or "Wednesday" or "Friday":
			exercises = w2_cardio.objects.all()
		elif today.strftime("%A") == "Tuesday" or "Saturday":
			exercises = w2_lowerbody.objects.all()
		else:
			exercises = w2_upperbody.objects.all()
	else:
		if today.strftime("%A") == "Thursday":
			exercises = w3_cardio.objects.all()
		elif today.strftime("%A") == "Tuesday" or today.strftime("%A") == "Friday":
			exercises = w3_legs.objects.all()
		elif today.strftime("%A") == "Wednesday" or today.strftime("%A") == "Saturday":
			exercises = w3_chest.objects.all()
		else:
			exercises = w3_back.objects.all()
	return render(request,"todaysschedule.html",{"exercises":exercises})



@login_required
def todaysdiet(request):
	form = DietForm(request.POST or None)
	
	if request.method == "POST" and form.is_valid():
		profile = UserProfile.objects.get(user=request.user)
		f = request.POST['fat']
		p = request.POST['protein']
		c = request.POST['carbohydrate']
		f = int(f)
		p = int(p)
		c = int(c)
		#print f+"\t"+p+"\t"+c+"\t"
		if profile.gender=="Male":
			if profile.age>=18 and profile.age<=20:
				if f<6:
					fa="f1"
				elif f>=6 and f<=8:
					fa="f2"
				elif f>8 and f<=10:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=21 and profile.age<=25:
				if f<7:
					fa="f1"
				elif f>=7 and f<=9:
					fa="f2"
				elif f>9 and f<=11:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=26 and profile.age<=35:
				if f<9:
					fa="f1"
				elif f>=9 and f<=11:
					fa="f2"
				elif f>11 and f<=13:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=36 and profile.age<=45:
				if f<12:
					fa="f1"
				elif f>=12 and f<=14:
					fa="f2"
				elif f>14 and f<=16:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=46 and profile.age<=55:
				if f<15:
					fa="f1"
				elif f>=15 and f<=17:
					fa="f2"
				elif f>17 and f<=19:
					fa="f3"
				else:
					fa="f4"
			if profile.age>56:
				if f<18:
					fa="f1"
				elif f>=18 and f<=20:
					fa="f2"
				elif f>20 and f<=22:
					fa="f3"
				else:
					fa="f4"		

		if profile.gender=="Female":
			if profile.age>=18 and profile.age<=20:
				if f<12:
					fa="f1"
				elif f>=12 and f<=14:
					fa="f2"
				elif f>14and f<=16:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=21 and profile.age<=25:
				if f<13:
					fa="f1"
				elif f>=13 and f<=15:
					fa="f2"
				elif f>17 and f<=19:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=26 and profile.age<=35:
				if f<15:
					fa="f1"
				elif f>=15 and f<=17:
					fa="f2"
				elif f>17 and f<=19:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=36 and profile.age<=45:
				if f<18:
					fa="f1"
				elif f>=18 and f<=20:
					fa="f2"
				elif f>20 and f<=26:
					fa="f3"
				else:
					fa="f4"
			if profile.age>=46 and profile.age<=55:
				if f<21:
					fa="f1"
				elif f>=21 and f<=23:
					fa="f2"
				elif f>23 and f<=25:
					fa="f3"
				else:
					fa="f4"
			if profile.age>56:
				if f<24:
					fa="f1"
				elif f>=24 and f<=26:
					fa="f2"
				elif f>26 and f<=28:
					fa="f3"
				else:
					fa="f4"
		print fa
		if p<10:
			pa = "p1"
		elif p>=10 and p<15:
			pa = "p2"
		elif p>=15 and p<=20:
			pa = "p3"
		if c<6:
			ca = "c1"
		else:
			ca = "c2"

		if fa=="f1" and pa=="p1" and ca=="c1":
			table=table1.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f1" and pa=="p1" and ca=="c2":
			table=table2.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f1" and pa=="p2" and ca=="c1":
			table=table3.objects.all()
			return render(request,"todaysdiet.html",{"table":table})

		if fa=="f1" and pa=="p2" and ca=="c2":
			table=table4.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f1" and pa=="p3" and ca=="c1":
			table=table5.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f1" and pa=="p3" and ca=="c2":
			table=table6.objects.all()
			return render(request,"todaysdiet.html",{"table":table})

		if fa=="f2" and pa=="p1" and ca=="c1":
			table=table7.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f2" and pa=="p1" and ca=="c2":
			table=table8.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f2" and pa=="p2" and ca=="c1":
			table=table9.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f2" and pa=="p2" and ca=="c2":
			table=table10.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f2" and pa=="p3" and ca=="c1":
			table=table11.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f2" and pa=="p3" and ca=="c2":
			table=table12.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f3" and pa=="p1" and ca=="c1":
			table=table13.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f3" and pa=="p1" and ca=="c2":
			table=table14.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f3" and pa=="p2" and ca=="c1":
			table=table15.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f3" and pa=="p2" and ca=="c2":
			table=table16.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f3" and pa=="p3" and ca=="c1":
			table=table17.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f3" and pa=="p3" and ca=="c2":
			table=table18.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f4" and pa=="p1" and ca=="c1":
			table=table19.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f4" and pa=="p1" and ca=="c2":
			table=table20.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f4" and pa=="p2" and ca=="c1":
			table=table21.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f4" and pa=="p2" and ca=="c2":
			table=table22.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f4" and pa=="p3" and ca=="c1":
			table=table23.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
		if fa=="f4" and pa=="p3" and ca=="c2":
			table=table24.objects.all()
			return render(request,"todaysdiet.html",{"table":table})
	




	return render(request,"todaysdiet.html",{"form":form})

	# u = UserProfile.objects.get(user_id=request.user.username)
	# if u.needs_instructor is True:
	# 	diet = u.diet
	# 	return render(request,"todaysdiet.html",{"diet":diet})
	# utc = UTC()
	# today = datetime.now(utc)
	# #today = today1.astimezone(timezone('Asia/Kolkata'))
	# if today.strftime("%A") == "Monday":
	# 	diet_list = Diet.objects.filter(day='Monday')
	# elif today.strftime("%A") == "Tuesday":
	# 	diet_list = Diet.objects.filter(day="Tuesday")
	# elif today.strftime("%A") == "Wednesday":
	# 	diet_list = Diet.objects.filter(day="Wednesday")
	# elif today.strftime("%A") == "Thursday":
	# 	diet_list = Diet.objects.filter(day="Thursday")
	# elif today.strftime("%A") == "Friday":
	# 	diet_list = Diet.objects.filter(day="Friday")
	# elif today.strftime("%A") == "Saturday":
	# 	diet_list = Diet.objects.filter(day="Saturday")
	# elif today.strftime("%A") == "Sunday":
	# 	diet_list = Diet.objects.filter(day="Sunday")
	# return render(request,"todaysdiet.html",{"diet_list":diet_list})

@login_required
def addoffer(request):
	form = OffersForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		of = form.cleaned_data['offer']
		o = Offers(offer=of)
		o.save()
		return render(request,"manager.html",{})
	return render(request,"addoffer.html",{"form":form})

@login_required
def allmembers(request):
	members = UserProfile.objects.filter(status='Member')
	return render(request,"allmembers.html",{"members":members})

@login_required
def memberprofile(request,user_name):
	user = User.objects.get(username=user_name)
	profile = UserProfile.objects.get(user_id=user_name)
	context={
	"user":user,
	"profile":profile
	}
	return render(request,"memberprofile.html",context)

@login_required
def allinstructors(request):
	instructors = UserProfile.objects.filter(status='Instructor')
	return render(request,"allinstructors.html",{"instructors":instructors})

@login_required
def instructorprofile(request,user_name):
	user = User.objects.get(username=user_name)
	profile = UserProfile.objects.get(user_id=user_name)
	context={
	"user":user,
	"profile":profile
	}
	return render(request,"instructorprofile.html",context)

@login_required
def persinst(request):
	user1 = UserProfile.objects.get(user=request.user)
	u = members.objects.get(member=user1)
	return render(request,"persinst.html",{"u":u})

@login_required
def ldate(request):
	profile = UserProfile.objects.get(user=request.user)
	utc = UTC()
	today = datetime.now(utc)
	days_remaining = request.user.date_joined + timedelta(days=int(profile.duration)) - today
	ldate = today + days_remaining
	return render(request,"ldate.html",{"ldate":ldate.date,"days_remaining":days_remaining.days})

@login_required
def offers(request):
	of = Offers.objects.all()
	return render(request,"offers.html",{"of":of})

@login_required
def iprofile(request):
	profile = UserProfile.objects.get(user = request.user)
	name=profile.user.first_name+" "+profile.user.last_name
	return render(request,"iprofile.html",{"profile":profile,"name":name})

@login_required
def inventory(request):
	return render(request,"inventory.html",{})

@login_required
def addinventory(request):
	return render(request,"addinventory.html",{})

@login_required
def showinventory(request):
	return render(request,"showinventory.html",{})

@login_required
def showMachines(request):
	mac = Machine.objects.all()
	return render(request,"showMachines.html",{"mac":mac})

@login_required
def showDumbells(request):
	dum = Dumbell.objects.all()
	return render(request,"showDumbells.html",{"dum":dum})

@login_required
def showPlatesAndBars(request):
	pnb = PlatesAndBar.objects.all()
	return render(request,"showPlatesAndBars.html",{"pnb":pnb})
	
@login_required
def showOtherAccessories(request):
	ota = OtherAccessory.objects.all()
	return render(request,"showOtherAccessories.html",{"ota":ota})

@login_required
def addMachine(request):
	form = MachineForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		name = form.cleaned_data['name']
		qty = form.cleaned_data['qty']
		obj = Machine(name=name,qty=qty)
		obj.save()
		return HttpResponseRedirect('/inventory/addinventory/addMachine')
	return render(request,"addMachine.html",{"form":form})

@login_required
def addDumbell(request):
	form = DumbellForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		name = form.cleaned_data['name']
		qty = form.cleaned_data['qty']
		obj = Dumbell(name=name,qty=qty)
		obj.save()
		return HttpResponseRedirect('/inventory/addinventory/addDumbell')
	return render(request,"addDumbell.html",{"form":form})

@login_required
def addPlatesAndBar(request):
	form = PlatesAndBarForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		name = form.cleaned_data['name']
		qty = form.cleaned_data['qty']
		obj = PlatesAndBar(name=name,qty=qty)
		obj.save()
		return HttpResponseRedirect('/inventory/addinventory/addPlatesAndBar')
	return render(request,"addPlatesAndBar.html",{"form":form})

@login_required
def addOtherAccessory(request):
	form = OtherAccessoryForm(request.POST or None)
	if request.method == "POST" and form.is_valid():
		name = form.cleaned_data['name']
		qty = form.cleaned_data['qty']
		obj = OtherAccessory(name=name,qty=qty)
		obj.save()
		return HttpResponseRedirect('/inventory/addinventory/addOtherAccessory')
	return render(request,"addOtherAccessory.html",{"form":form})


@login_required
def removeinventory(request):
	return render(request,"removeinventory.html",{})

@login_required
def removeMachine(request):
	mac = Machine.objects.all()
	if request.method == "POST":
		machi = request.POST.getlist('checks[]')
		for machine in machi:
			obj = Machine.objects.get(name=machine)
			obj.delete()
		return HttpResponseRedirect('/inventory/removeinventory/')
	return render(request,"removeMachine.html",{"mac":mac})

@login_required
def removeDumbell(request):
	dum = Dumbell.objects.all()
	if request.method == "POST":
		machi = request.POST.getlist('checks')
		for machine in machi:
			obj = Dumbell.objects.get(name=machine)
			obj.delete()
		return HttpResponseRedirect('inventory/removeinventory/')
	return render(request,"removeDumbell.html",{"dum":dum})

@login_required
def removePlatesAndBar(request):
	pnb = PlatesAndBar.objects.all()
	if request.method == "POST":
		machi = request.POST.getlist('checks')
		for machine in machi:
			obj = PlatesAndBar.objects.get(name=machine)
			obj.delete()
		return HttpResponseRedirect('inventory/removeinventory/')
	return render(request,"removePlatesAndBar.html",{"pnb":pnb})
	
@login_required
def removeOtherAccessory(request):
	ota = OtherAccessory.objects.all()
	if request.method == "POST":
		machi = request.POST.getlist('checks')
		for machine in machi:
			obj = OtherAccessory.objects.get(name=machine)
			obj.delete()
		return HttpResponseRedirect('inventory/removeinventory/')
	return render(request,"removeOtherAccessory.html",{"ota":ota})
