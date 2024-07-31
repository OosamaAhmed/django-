from rest_framework import serializers  

from .models import Std,Track
# ---------------->>> important <<<<<---------------
# self study : how to add bootstrap class to our modelform using widget
# how to add form validation (ref: cleand_data)
class StdSerializers(serializers.ModelSerializer):
    class Meta:
        model = Std
        fields = ('id','fname', 'lname','age', 'std_track')