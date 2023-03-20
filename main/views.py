from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def main(request):
    # Resume Title
    latest_value = len(ResumeTitle.objects.all())
    name = ResumeTitle.objects.all()[latest_value - 1]
    about_me = ResumeTitle.objects.all()[latest_value - 1]
    profile_pic = ResumeTitle.objects.all()[latest_value - 1].profile_pic
    

    # scroll Text Designation
    designation = ResumeTitleScroll.objects.all()

    # Skill and Slider bar
    skill = ResumeSkill.objects.all()
    skill_level = ResumeSkill.objects.all()
    two_loops = zip(skill, skill_level)

    # Education
    level = ResumeEducation.objects.all()
    start_date = ResumeEducation.objects.all()
    end_date = ResumeEducation.objects.all()
    college = ResumeEducation.objects.all()
    edu_loops = zip(level, start_date, end_date, college)

    # Experience
    title = ResumeExperience.objects.all()
    company = ResumeExperience.objects.all()
    address = ResumeExperience.objects.all()
    start_date = ResumeExperience.objects.all()
    end_date = ResumeExperience.objects.all()
    description = ResumeExperience.objects.all()
    exp_loops = zip(title, company, address, start_date, end_date, description)

    # Services
    title = ResumeService.objects.all()
    detail = ResumeService.objects.all()
    icon = ResumeService.objects.all()
    serv_loops = zip(title, detail, icon)

    # Portfolio
    project_name = ResumePortfolio.objects.all()
    project_type = ResumePortfolio.objects.all()
    project_img = ResumePortfolio.objects.all()
    project_tag = ResumePortfolio.objects.all()
    project_link = ResumePortfolio.objects.all()
    port_loops = zip(project_name, project_type, project_img, project_tag, project_link)

    # Contacts
    total_contacts = len(ResumeContact.objects.all())
    name_cont = ResumeContact.objects.all()[total_contacts - 1]
    designation_cont = ResumeContact.objects.all()[total_contacts - 1]
    email = ResumeContact.objects.all()[total_contacts - 1]
    mobile = ResumeContact.objects.all()[total_contacts - 1]
    address = ResumeContact.objects.all()[total_contacts - 1]

    return render(request, "resume.html", {
        "name": name,
        "about_me": about_me,
        "profile_pic": profile_pic,
        "designation": designation,
        "skill_list": two_loops,
        "education": edu_loops,
        "experience": exp_loops,
        "service": serv_loops,
        "portfolio": port_loops,
        "name_cont": name_cont,
        "designation_cont": designation_cont,
        "email": email,
        "mobile": mobile,
        "address": address
    })


    

def contact_me(request):
    latest_value = len(ResumeTitle.objects.all())
    profile_pic = ResumeTitle.objects.all()[latest_value - 1].profile_pic
    if request.method == "POST":
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_subject = request.POST['contact_subject']
        contact_message = request.POST['contact_message']

        message = f"""
        You got a message from: {contact_name}

        Email: {contact_email}

        Subject: {contact_subject}

        Message: {contact_message}
        """

        if contact_name and contact_email and contact_subject and contact_message:
            
            
            try:
                send_mail(
                    'Message from Contact_Me',
                    message,
                    'mahesh.projects33@gmail.com',
                    ['mahesh.projects33@gmail.com'],
                    fail_silently= False
                )
                messages.info(request, "'Thanks for contacting me! I've received your message and will reply soon. I appreciate your interest and look forward to connecting with you!'")
                return redirect('contact')
            except Exception as e:
                return HttpResponse('An error occurred while sending the email: {}'.format(str(e)), status=500)
        else:
            messages.info(request, "I apologize for the inconvenience, but there seems to be an issue with the email transmission. Kindly try submitting your message again. I appreciate your patience and look forward to receiving your message.")
            return redirect('contact')
            
    return render(request, 'contact.html', {"profile_pic": profile_pic})