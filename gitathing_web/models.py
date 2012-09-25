from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from licenses.fields import LicenseField
import urllib, hashlib

class Profile(models.Model):
    """User profile"""
    user = models.ForeignKey(User)
    display_name = models.CharField(max_length = 100, blank = True)
    location = models.CharField(max_length = 100, blank = True)
    about = models.TextField("About me", blank = True)
    
    def mini_avatar(self):
        return self.avatar(size = 32, default = "http://gitathing.org/static/img/unknown-mini.png")

    def avatar(self, size = 120, default = "http://gitathing.org/static/img/unknown.png"):
        """Gravatar fetching as from http://gravatar.com/site/implement/images/python/"""
        email = self.user.email
        gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
        return gravatar_url

    def __unicode__(self):
        if self.display_name:
            return self.display_name
        else:
            return unicode(self.user)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user = instance)
post_save.connect(create_user_profile, sender = User)

class Media(models.Model):
    """Static content not handled in git repositories"""
    design = models.ForeignKey("Design", related_name = "media")
    file = models.FileField(upload_to = "%Y/%m/%d/")
    added = models.DateTimeField(auto_now_add = True)
    uploader = models.ForeignKey(User)

class Design(models.Model):
    """Database entry for a git-repository (possibly pointing to a specific git branch)"""
    user = models.ForeignKey(User)
    name = models.CharField("Design name", max_length = 150)
    short_name = models.SlugField("Short repository name")
    repo_path = models.CharField(max_length = 80, editable = False, blank = True)
    branch = models.CharField(max_length = 100, editable = False, blank = True, null = True, default = "master")
    parent = models.ForeignKey("Design", null = True, blank = True)
    derived_from = models.ManyToManyField("Design", related_name = "derivatives")
    license = LicenseField()
    description = models.TextField(blank = True)
    instructions = models.TextField(blank = True)
    public = models.BooleanField(default = False, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = (("user", "short_name", "branch"),)

class Release(models.Model):
    """Database entry for a git-tag"""
    design = models.ForeignKey(Design)
    name = models.CharField(max_length = 100)
    date = models.DateTimeField()

class Build(models.Model):
    """Report of a build of a design by someone"""
    builder = models.ForeignKey(User)
    design = models.ForeignKey(Design)
    date = models.DateTimeField(auto_now_add = True)
    comment = models.TextField()
    image = models.ForeignKey(Media)

