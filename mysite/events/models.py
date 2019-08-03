from django.db import models

class Venue(models.Model):
       name = models.CharField('Venue Name', max_length=120)
       address = models.CharField(max_length=300)
       zip_code = models.CharField('Zip/Post Code', max_length=12)
       phone = models.CharField('Contact Phone', max_length=20)
       web = models.URLField('Web Address')
       email_address = models.EmailField('Email Address')

       def __str__(self):
            
            return self.name

class Event(models.Model):
     name = models.CharField('Event Name', max_length=120)
     event_date = models.DateTimeField('Event Date')
     venue = models.ForeignKey(Venue,default=1, on_delete=models.SET_DEFAULT)
     manager = models.CharField(max_length = 60)
     description = models.TextField(blank=True)

     def __str__(self):
            
            return self.name

