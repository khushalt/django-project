from django.db import models

# Create your models here.

class Users(models.Model):
	user_name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 30, unique = True)
	full_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.email

class ForumData(models.Model):
	user_name = models.ForeignKey(Users, on_delete = models.DO_NOTHING)
	creation_at = models.DateTimeField()
	topic_id = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	title = models.CharField(max_length = 50)
