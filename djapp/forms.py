from django import forms  
from djapp.models import Std ,Track

class StdForms(forms.ModelForm):
    class Meta:
        model = Std
        # fields =('fname', 'lname', 'age', 'std_track',)
        fields = ('__all__')

class TrackForms(forms.ModelForm):
    class Meta:
        model = Track
        # fields =('tname',)
        fields = ('__all__')

