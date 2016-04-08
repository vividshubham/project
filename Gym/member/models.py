from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import signals
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	age = models.IntegerField(null = True)
	MEMBER = 'Member'
	INSTRUCTOR = 'Instructor'
	Status = ((MEMBER,'Member'),(INSTRUCTOR,'Instructor'))
	MALE = 'Male'
	FEMALE = 'Female'
	Gender = ((MALE,'Male'),(FEMALE,'Female'))
	gender = models.CharField(max_length = 9,choices = Gender,blank=False,null=True)
	phoneno = models.BigIntegerField(blank = True,null=True)
	address = models.CharField(max_length = 200,blank = True)
	status = models.CharField(max_length = 15,choices = Status,blank=False,null=True)
	Ap = 'A+'
	An = 'A-'
	Bp = 'B+'
	Bn = 'B-'
	ABp = 'AB+'
	ABn = 'AB-'
	Op = 'O+'
	On = 'O-'
	Bloodgrp = ((Ap,'A+'),(An,'A-'),(Bp,'B+'),(Bn,'B-'),(ABp,'AB+'),(ABn,'AB-'),(Op,'O+'),(On,'O-'))
	one_month = '30'
	two_month = '60'
	three_month = '90'
	six_month = '180'
	one_year = '365'
	Duration = ((one_month,'30'),(two_month,'60'),(three_month,'90'),(six_month,'180'),(one_year,'365'))
	duration = models.CharField(max_length = 3,choices = Duration)

	def create_profile(sender,instance,created,**kwargs):
		if created:
			profile,new = UserProfile.objects.get_or_create(user=instance)


class MemberDetails(models.Model):
	user = models.OneToOneField(User)
	height = models.IntegerField()
	weight = models.IntegerField()
	def AssignInstructor(User):
		instructors = []
		instructors = UserProfile


	