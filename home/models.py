from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=254, unique=True, help_text='Enter your email address')
    password = models.CharField(max_length=128, help_text='Enter your password')
    check_me_out = models.BooleanField(default=False, help_text='Check this box if you want to be checked out')

    def __str__(self):
        return self.email
