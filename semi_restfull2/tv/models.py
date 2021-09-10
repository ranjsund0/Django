from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        error = {}
        if len(postData['name']) < 2:
            errors["name"] = "Name must be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network must be at least 3 characters"
        if len(postData['description']) < 2:
            errors["description"] = "Name must be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()



