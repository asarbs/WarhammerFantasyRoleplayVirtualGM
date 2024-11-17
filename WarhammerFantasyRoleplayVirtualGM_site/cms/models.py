from django.db import models
from django.contrib.auth.models import User

import hashlib
from datetime import datetime

# Create your models here.

import logging
logger = logging.getLogger(__name__)

class Tag(models.Model):
    name = models.CharField(max_length= 250)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class News(models.Model):
    title = models.CharField(max_length= 250)
    lead = models.TextField(verbose_name="lead", default="")
    contents = models.TextField(verbose_name="content", default="", blank=True, null=True)
    datetime_create = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Create Time")
    datetime_update = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Update Time")
    author = models.ForeignKey(User, verbose_name='User', blank=True, null=True, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)
    tagss = models.ManyToManyField(Tag, through="News2Tag", blank=True)
    is_yt = models.BooleanField(max_length= 50, default=False, blank=True, null=True)
    internal_id = models.CharField(max_length= 50, blank=True, null=True)
    
    def autor_formmated(self):
        if self.author is None:
            return "-"
        return u"{0} \"{1}\" {2}".format(self.author.first_name, self.author.username, self.author.last_name)

    
    def __str__(self):
        return u"{0}".format(self.title)

    def __unicode__(self):
        return u"{0}".format(self.title)
    
    def save(self, *args, **kwargs):
        self.datetime_create = datetime.now()
        # if not self.is_yt:
        #     txt = self.lead.encode('utf-8') + str(self.datetime_create).encode('utf-8')
        #     self.internal_id = hashlib.md5(txt).hexdigest()
        super().save(*args, **kwargs)

        
        
    
class News2Tag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    

    class Meta:
        ordering = ['news']

    def __str__(self):
        return f"Tag: {self.tag} -> {self.news}"

    def __unicode__(self):
        return f"Tag: {self.tag} -> {self.news}"
