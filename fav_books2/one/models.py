
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['regex'] = ("Invalid email address!")
            
        email_check= self.filter(email= postData['email'])
        if email_check:
            errors['email'] = "Email already in use"  
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match'
        return errors
    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())
    

    def register(self, postData):
        pw = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = pw
        )

class BookManager(models.Manager):
    def book_validate(self, postData):
        errors = {}


        if len(postData['title']) < 1:
                errors["title"] = "There must be a title"
        if len(postData['description']) < 5:
                errors["description"] = "Description should be 5 characters"
    
        return errors




class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=355)
    creator = models.ForeignKey(User, related_name="has_created_books",
    on_delete=models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name="favorited_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()








