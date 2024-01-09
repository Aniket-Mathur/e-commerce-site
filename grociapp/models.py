from django.db import models

# Create your models here.
class item(models.Model):
	item_id=models.AutoField
	item_name=models.CharField(max_length=50)
	item_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



	def __str__(self):
		return self.item_name



class fruit(models.Model):
	fruit_id=models.AutoField
	fruit_name=models.CharField(max_length=50)
	fruit_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



class pulse(models.Model):
	pulse_id=models.AutoField
	pulse_name=models.CharField(max_length=50)
	pulse_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")


class staple(models.Model):
	staple_id=models.AutoField
	staple_name=models.CharField(max_length=50)
	staple_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



class utensil(models.Model):
	utensil_id=models.AutoField
	utensil_name=models.CharField(max_length=50)
	utensil_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



class disinfecent(models.Model):
	disinfecent_id=models.AutoField
	disinfecent_name=models.CharField(max_length=50)
	disinfecent_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



class milk(models.Model):
	milk_id=models.AutoField
	milk_name=models.CharField(max_length=50)
	milk_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



class biscuit(models.Model):
	biscuit_id=models.AutoField
	biscuit_name=models.CharField(max_length=50)
	biscuit_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")


class drink(models.Model):
	drink_id=models.AutoField
	drink_name=models.CharField(max_length=50)
	drink_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")



class noodle(models.Model):
	noodle_id=models.AutoField
	noodle_name=models.CharField(max_length=50)
	noodle_desc=models.CharField(max_length=50)
	price=models.IntegerField(default="0")
	image=models.ImageField(upload_to='images',default="0")