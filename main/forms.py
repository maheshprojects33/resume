from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(label='Your Name', max_length=100)
    contact_email = forms.EmailField(label='Your Email', max_length=100)
    contact_subject = forms.CharField(label='Subject', max_length=100)
    contact_message = forms.CharField(label='Message', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('contact_name'):
            self.add_error('contact_name', 'Please enter your name')
        if not cleaned_data.get('contact_email'):
            self.add_error('contact_email', 'Please enter your email')
        if not cleaned_data.get('contact_subject'):
            self.add_error('contact_subject', 'Please enter a subject')
        if not cleaned_data.get('contact_message'):
            self.add_error('contact_message', 'Please enter a message')
