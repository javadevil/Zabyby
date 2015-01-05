from django.db import models

# Create your models here.
#Contact vCard4.0 spec implementation
class Contact(models.Model):
	GENDERS = (
		('M','Male'),
		('F','Female'),
		('O','Other'),
		('N','None'),
		('U','Unknow')
	)
	n 			= models.CharField(max_length=1024)
	nickname 	= models.CharField(max_length=128)
	bday		= models.DateField()
	gender		= models.CharField(max_length=1,choices=GENDERS)
	 
	def __str__():
		return "Contact"

class Address(models.Model):
	contact 	= models.ForeignKey(Contact)
	pobox		= models.CharField(max_length=256)
	ext			= models.CharField(max_length=256)
	street		= models.CharField(max_length=256)
	locality	= models.CharField(max_length=256)
	region		= models.CharField(max_length=256)
	code		= models.CharField(max_length=20)
	country		= models.CharField(max_length=256)
	geo			= models.CharField(max_length=64)

class Tel(models.Model):
	TEL_TYPE = (
		('home','Home'),
		('work','Work'),
		('mobile','Mobile'),
		('main','main'),
		('home fax','Home Fax'),
		('work fax','Work Fax'),
		('pager','Pager'),
		('other','other'),
	)
	contact 	= models.ForeignKey(Contact)
	tel_type 	= models.CharField(max_length=10,choices=TEL_TYPE)
	uri			= models.CharField(max_length=255)

class Email(models.Model):
	MAIL_TYPE = (
		('home','Home'),
		('work','Work'),
		('other','Other'),
	)
	contact 	= models.ForeignKey(Contact)
	mail_type	= models.CharField(max_length=10,choices=MAIL_TYPE)
	uri			= models.CharField(max_length=255)

class Url(models.Model):
	URL_TYPE = (
		('homepage','Homepage'),
		('home','Home'),
		('work','work'),
		('other','Other'),
	)
	contact 	= models.ForeignKey(Contact)
	url_type	= models.CharField(max_length=10,choices=URL_TYPE)
	uri			= models.CharField(max_length=255)
