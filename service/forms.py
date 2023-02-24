from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class quoteForm(forms.Form):
    deliver_city = forms.CharField(max_length=50)
    departure_city = forms.CharField(max_length=50)
    total_wight = forms.DecimalField(max_digits=6)
    dimension = forms.DecimalField(max_digits=6)
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    phone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
