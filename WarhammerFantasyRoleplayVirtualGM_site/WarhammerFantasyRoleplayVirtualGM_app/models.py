from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, verbose_name='Player', on_delete=models.CASCADE)

    def __str__(self):
        return u"{0} \"{1}\" {2}".format(self.user.first_name, self.user.username, self.user.last_name)

    def __unicode__(self):
        return u"{0} \"{1}\" {2}".format(self.user.first_name, self.user.username, self.user.last_name)

class Species(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class CharacterClass(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class CareerPath(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class Career(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class Status(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class Hair(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class Eyes(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Character(models.Model):
    player = models.OneToOneField(Player, verbose_name="Player", on_delete=models.CASCADE)
    name = models.CharField(max_length= 50)
    species = models.OneToOneField(Species, verbose_name="Species", on_delete=models.CASCADE)
    ch_class = models.OneToOneField(CharacterClass, verbose_name="Class", on_delete=models.CASCADE)
    career_level = models.IntegerField(default="1", verbose_name="Career  Level")
    career_path = models.OneToOneField(CareerPath, verbose_name="CareerPath", on_delete=models.CASCADE)
    status = models.OneToOneField(Status, verbose_name="Status", on_delete=models.CASCADE)
    age = models.IntegerField(default="1", verbose_name="Age")
    height = models.IntegerField(default="1", verbose_name="Age")
    hair = models.OneToOneField(Hair, verbose_name="Hair", on_delete=models.CASCADE)
    eyes = models.OneToOneField(Eyes, verbose_name="Eyes", on_delete=models.CASCADE)
    characteristics_ws_initial = models.IntegerField(default="0", verbose_name="ws_initial")
    characteristics_bs_initial = models.IntegerField(default="0", verbose_name="bs_initial")
    characteristics_s_initial = models.IntegerField(default="0", verbose_name="s_initial")
    characteristics_t_initial = models.IntegerField(default="0", verbose_name="t_initial")
    characteristics_i_initial = models.IntegerField(default="0", verbose_name="i_initial")
    characteristics_ag_initial = models.IntegerField(default="0", verbose_name="ag_initial")
    characteristics_dex_initial = models.IntegerField(default="0", verbose_name="dex_initial")
    characteristics_int_initial = models.IntegerField(default="0", verbose_name="int_initial")
    characteristics_wp_initial = models.IntegerField(default="0", verbose_name="wp_initial")
    characteristics_fel_initial = models.IntegerField(default="0", verbose_name="fel_initial")
    characteristics_ws_advances = models.IntegerField(default="0", verbose_name="ws_advances")
    characteristics_bs_advances = models.IntegerField(default="0", verbose_name="bs_advances")
    characteristics_s_advances = models.IntegerField(default="0", verbose_name="s_advances")
    characteristics_t_advances = models.IntegerField(default="0", verbose_name="t_advances")
    characteristics_i_advances = models.IntegerField(default="0", verbose_name="i_advances")
    characteristics_ag_advances = models.IntegerField(default="0", verbose_name="ag_advances")
    characteristics_dex_advances = models.IntegerField(default="0", verbose_name="dex_advances")
    characteristics_int_advances = models.IntegerField(default="0", verbose_name="int_advances")
    characteristics_wp_advances = models.IntegerField(default="0", verbose_name="wp_advances")
    characteristics_fel_advances = models.IntegerField(default="0", verbose_name="fel_advances")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Campaign(models.Model):
    name = models.CharField(max_length= 250)
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
