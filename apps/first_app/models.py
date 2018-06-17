from __future__ import unicode_literals
from django.db import models

class Users(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __repr__(self):
        return "<user: {}, {}, {}, {}>".format(self.id, self.first_name, self.last_name, self.email)

class Books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    uploader = models.ForeignKey(Users, related_name="uploaded_books")
    likes = models.ManyToManyField(Users, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __repr__(self):
        return "<book: {}, {}, {}>".format(self.id, self.name, self.desc)
