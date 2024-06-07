from django.contrib import admin

from djapp.models import Std, Track



# customization
class Stdadmin(admin.ModelAdmin):
    fieldsets = (
        ['student info',{'fields':['fname','lname','age']}],
        ['track or scholer ship info',{'fields':['std_track']}]
        
    )
    list_display =('fname','lname','is_graduated','age','std_track')
    list_filter = ['fname','age']
    search_fields = ['fname','age']

class InlineStudent(admin.StackedInline):
    model = Std
    extra = 1  # default 3 
     
    
class TrackAdmin (admin.ModelAdmin):
    inlines = [InlineStudent]
    
admin.site.register(Std ,Stdadmin)
admin.site.register(Track ,TrackAdmin)

