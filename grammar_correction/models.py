from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    user_type = models.IntegerField()

    def __str__(self):
        return "%s: %s" % (self.user_name, self.user_type)

class FeedbackResult(models.Model):
    user_name = models.CharField(max_length=64)
    original_text = models.TextField(blank=True, null=True)
    system_correction_result = models.TextField(blank=True, null=True)
    user_correction_suggestion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user_name