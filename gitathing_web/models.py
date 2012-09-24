from django.db import models
from django.contrib.auth.models import User
from licenses.fields import LicenseField

class Profile(models.Model):
    """User profile"""
    user = models.ForeignKey(User)
    display_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 200)
    location = models.CharField(max_length = 100)
    about = models.TextField("About me")

class Media(models.Model):
    """Static content not handled in git repositories"""
    design = models.ForeignKey("Design", related_name = "media")
    file = models.FileField(upload_to = "%Y/%m/%d/")
    added = models.DateTimeField(auto_now_add = True)
    uploader = models.ForeignKey(User)

class Design(models.Model):
    """Database entry for a git-repository (possibly pointing to a specific git branch)"""
    designer = models.ForeignKey(User)
    name = models.CharField(max_length = 150)
    short_name = models.SlugField()
    repo_path = models.CharField(max_length = 80, editable = False, blank = True)
    branch = models.CharField(max_length = 100, editable = False, blank = True, null = True)
    parent = models.ForeignKey("Design", null = True, blank = True)
    derived_from = models.ManyToManyField("Design", related_name = "derivatives")
    license = LicenseField()
    description = models.TextField(blank = True)
    instructions = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)

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

