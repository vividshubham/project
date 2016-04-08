from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import signals
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,primary_key=True,to_field='username')
	age = models.IntegerField(blank=True,null = True)
	MEMBER = 'Member'
	INSTRUCTOR = 'Instructor'
	Status = ((MEMBER,'Member'),(INSTRUCTOR,'Instructor'))
	MALE = 'Male'
	FEMALE = 'Female'
	Gender = ((MALE,'Male'),(FEMALE,'Female'))
	gender = models.CharField(max_length = 9,choices = Gender,blank=False,null=False)
	phoneno = models.CharField(max_length=10,blank = True,null=True)
	address = models.CharField(max_length = 200,blank = True,null=True)
	status = models.CharField(max_length = 15,choices = Status,blank=False,null=False)
	Ap = 'A+'
	An = 'A-'
	Bp = 'B+'
	Bn = 'B-'
	ABp = 'AB+'
	ABn = 'AB-'
	Op = 'O+'
	On = 'O-'
	Bloodgrp = ((Ap,'A+'),(An,'A-'),(Bp,'B+'),(Bn,'B-'),(ABp,'AB+'),(ABn,'AB-'),(Op,'O+'),(On,'O-'))
	bloodgrp = models.CharField(max_length = 4,choices = Bloodgrp,blank=True,null=True)
	one_month = '30'
	two_month = '60'
	three_month = '90'
	six_month = '180'
	one_year = '365'
	Duration = ((one_month,'30'),(two_month,'60'),(three_month,'90'),(six_month,'180'),(one_year,'365'))
	duration = models.CharField(max_length = 3,choices = Duration)

	needs_instructor = models.BooleanField(default=False)
	#instructor = models.ForeignKey("self",default = "",blank = True,null = True,limit_choices_to={'status':'Instructor'},related_name="instruct")
	#members = models.ForeignKey("self",default="",blank=True,null = True,limit_choices_to={'status':'Member','needs_instructor':True},related_name = "membs")
	exercises = models.TextField(default="",blank=True,null=True,editable=False)
	diet = models.TextField(default="",blank=True,null=True,editable=False)
	#instructor = models.ForeignKey("self",limit_choices_to={'status':'Instructor'},blank=True,null=True)

	def __unicode__(self):
		return u"%s" % self.user.username
	def save1(self):
		if self.needs_instructor is True:
			instructors = UserProfile.objects.filter(status="Instructor")
			extra_data = extras.objects.all()
			print instructors
			print "here"
			if not self.instructor:
				if len(members)<25:
					self.instructor = instructors[extra_data[0].value].user.username
					extra_data[0].value+=1
					if extra_data[0].value==5:
						extra_data[0].value=0
					extra_data.save()
				else:
					extra_data[0].value = extra_data[0].value+5
					if extra_data[1].value<5:
						self.instructor = instructors[extra_data[0].value].user.username
						extra_data[1].value+=1
						if extra_data[1].value==5:
							extra_data[1].value=0
							extra_data[0].value+=1
						extra_data.save()
		super(UserProfile, self).save1()


# def AssignInstructor(self):
# 	instructors = UserProfile.objects.filter(status='Intructor')
# 	members = UserProfile.objects.filter(status='Member',needs_instructor=True)
# 	extra_data = extras.objects.all()

# 	if profile.needs_instructor is True:
# 		if len(members)<25:
# 			instructor1 = instructors[extra_data[0].value].user.username
# 			extra_data[0].value+=1
# 			if extra_data[0].value==5:
# 				extra_data[0].value=0
# 			extra_data.save()
# 			return instructor1
# 		else:
# 			extra_data[0].value = extra_data[0].value+5
# 			if extra_data[1].value<5:
# 				instructor1 = instructors[extra_data[0].value].user.username
# 				extra_data[1].value+=1
# 				if extra_data[1].value==5:
# 					extra_data[1].value=0
# 					extra_data[0].value+=1
# 				extra_data.save()
# 			return instructor1


def create_profile(sender,instance,created,**kwargs):
	if created:
		print "here1"
		profile = UserProfile.objects.create(user=instance)
		


post_save.connect(create_profile, sender=User)

class instructors(models.Model):
	instructor = models.ForeignKey(UserProfile,limit_choices_to={'status':'Instructor'})
class members(models.Model):
	member = models.ForeignKey(UserProfile,limit_choices_to={'status':'Member','needs_instructor':True},related_name='membs')
	instructor = models.ForeignKey(UserProfile,limit_choices_to={'status':'Instructor'},related_name='instruct',blank=True,null=True)
	def __unicode__(self):
		return u"%s" % self.member.user.username
def create_profile1(sender,instance,created,**kwargs):
	if created:
		profile1 = instructor.objects.create(member=instance)
'''
class MemberInfo(models.Model):
	member = models.ForeignKey(User)
	height = models.IntegerField()
	weight = models.IntegerField()
	def AssignInstructor(User):
		mems = UserProfile.objects.filter(status='Member')
		ins = UserProfile.objects.filter(status='Instructor')
		lenm = len(mems)-1
		leni = len(ins)-1
'''

class extras(models.Model):
	data = models.CharField(max_length=10)
	value = models.IntegerField(default=0)

class Offers(models.Model):
	offer = models.TextField(blank=True)


class Machine(models.Model):
	name = models.CharField(max_length=20,blank = False,null = False)
	qty = models.IntegerField()
	def __unicode__(self):
		return u"%s" % self.name

class Dumbell(models.Model):
	name = models.CharField(max_length=20,blank=False,null=False)
	qty = models.IntegerField()
	def __unicode__(self):
		return u"%s" % self.name

class PlatesAndBar(models.Model):
	name = models.CharField(max_length=20,blank=False,null=False)
	qty = models.IntegerField()
	def __unicode__(self):
		return u"%s" % self.name

class OtherAccessory(models.Model):
	name = models.CharField(max_length=20,blank=False,null=False)
	qty = models.IntegerField()
	def __unicode__(self):
		return u"%s" % self.name

class w1_cardio(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

class w1_fullbody(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise


class w2_cardio(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise


class w2_lowerbody(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

class w3_legs(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

class w2_upperbody(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

class w3_back(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

class w3_cardio(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

class w3_chest(models.Model):
	exercise = models.CharField(max_length=30)
	sets = models.CharField(max_length=10)
	def __unicode__(self):
		return u"%s" % self.exercise

# class Diet(models.Model):
	
# 	MONDAY = "Monday"
# 	TUESDAY = "Tuesday"
# 	WEDNESDAY = "Wednesday"
# 	THURSDAY = "Thursday"
# 	FRIDAY = "Friday"
# 	SATURDAY = "Saturday"
# 	SUNDAY = "Sunday"
# 	Day = ((MONDAY,'Monday'),(TUESDAY,'Tuesday'),(WEDNESDAY,'Wednesday'),(THURSDAY,'Thursday'),(FRIDAY,'Friday'),(SATURDAY,'Saturday'),(SUNDAY,'Sunday'))	
# 	day = models.CharField(max_length=15,choices=Day)
# 	EARLY_MORNING = "Early Morning"
# 	BREAKFAST = "Breakfast"
# 	MID_MORNING = "Mid-Morning"
# 	LUNCH = "Lunch"
# 	TEA_SNACKS = "Tea and Snacks"
# 	DINNER = "Dinner"
# 	BEDTIME = "Bedtime"
# 	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(MID_MORNING,'Mid-Morning'),(LUNCH,'Lunch'),(TEA_SNACKS,'Tea and Snacks'),(DINNER,'Dinner'),(BEDTIME,'Bedtime'))
# 	meal = models.CharField(max_length=50,choices=Meal)
# 	food_type = models.CharField(max_length=100)
# 	diet = models.TextField()

# 	def __unicode__(self):
# 		return u"%s" % self.meal

class table1(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table2(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table3(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table4(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table5(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table6(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table7(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table8(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table9(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table10(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table11(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table12(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table13(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table14(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table15(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table16(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table17(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table18(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table19(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table20(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table21(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table22(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table23(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)

class table24(models.Model):
	EARLY_MORNING = "Early Morning"
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	EVENING_SNACKS = "Evening Snacks"
	DINNER = "Dinner"
	Meal = ((EARLY_MORNING,'Early Morning'),(BREAKFAST,'Breakfast'),(LUNCH,'Lunch'),(EVENING_SNACKS,'Evening Snacks'),(DINNER,'Dinner'))
	meal = models.CharField(max_length=50,choices=Meal)
	food_type = models.CharField(max_length=100)
	diet = models.CharField(max_length=255)


class Fat(models.Model):
	age = models.IntegerField()


	
	
