from django.contrib import admin
from .models import *


# Register your models here.

class ResumeTitleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "about_me", "profile_pic")


class ResumeTitleScrollAdmin(admin.ModelAdmin):
    list_display = ("id", "designation")


class ResumeSkillAdmin(admin.ModelAdmin):
    list_display = ("id", "skill", "skill_level")


class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ("level", "college", "start_date", "end_date")


class ResumeExperienceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")


class ResumeServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "detail", "icon")


class ResumePortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name", "project_type", "project_img", "project_tag", "project_link")


class ResumeContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "mobile")


admin.site.register(ResumeTitle, ResumeTitleAdmin)
admin.site.register(ResumeTitleScroll, ResumeTitleScrollAdmin)
admin.site.register(ResumeSkill, ResumeSkillAdmin)
admin.site.register(ResumeEducation, ResumeEducationAdmin)
admin.site.register(ResumeExperience, ResumeExperienceAdmin)
admin.site.register(ResumeService, ResumeServiceAdmin)
admin.site.register(ResumePortfolio, ResumePortfolioAdmin)
admin.site.register(ResumeContact, ResumeContactAdmin)
