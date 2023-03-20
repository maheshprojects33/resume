from django.db import models


# Create your models here.
class ResumeTitle(models.Model):
    name = models.CharField(max_length=30)
    about_me = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="thumbnail_profile", default="", blank=True)


class ResumeTitleScroll(models.Model):
    designation = models.CharField(max_length=100)


class ResumeSkill(models.Model):
    skill = models.CharField(max_length=500)
    skill_level = models.CharField(max_length=3)


class ResumeEducation(models.Model):
    level = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    college = models.CharField(max_length=200)


class ResumeExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()


class ResumeService(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    icon = models.ImageField(upload_to="service_icon", default="")


class ResumePortfolio(models.Model):
    project_name = models.CharField(max_length=100)
    project_type = models.CharField(max_length=100)
    project_img = models.ImageField(upload_to="project_img", default="")
    project_link = models.CharField(max_length=100, default="", blank=True)
    PROJECT_CHOICE = (
        ('code', 'code'),
        ('graphics', 'graphics'),
        ('3d', '3d'),
    )
    project_tag = models.CharField(max_length=10, choices=PROJECT_CHOICE, blank=True, default="")


class ResumeContact(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
