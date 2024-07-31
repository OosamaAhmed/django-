from django import forms  
from djapp.models import Std ,Track
# ---------------->>> important <<<<<---------------
# self study : how to add bootstrap class to our modelform using widget
# how to add form validation (ref: cleand_data)
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

