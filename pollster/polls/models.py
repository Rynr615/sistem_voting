from django.db import models

class Polling(models.Model):
    polling_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.polling_text

class Choice(models.Model):
    polling = models.ForeignKey(Polling, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
