from django.contrib import admin

# Register your models here.


from .models import Input
from .models import Auth
from .models import Clients
from .models import Downloads
from .models import Sessions
from .models import Sensors


class AuthAdmin(admin.ModelAdmin):
	model = Auth
	list_display  = ('session' , 'success' , 'username' , 'password' , 'timestamp')

class InputAdmin(admin.ModelAdmin):
	model = Input
	list_display = ('session', 'timestamp' , 'realm' , 'success' , 'input')

class ClientAdmin(admin.ModelAdmin):
	model = Clients
	list_display = ['version']

class DownloadsAdmin(admin.ModelAdmin):
	model = Downloads
	list_display = ('session', 'timestamp' , 'url' , 'outfile')

class SessionsAdmin(admin.ModelAdmin):
	model = Sessions
	list_display = ('id' , 'starttime' , 'endtime' , 'sensor' , 'ip' , 'termsize' , 'client')

class SensorAdmin(admin.ModelAdmin):
	model = Sensors
	list_display = ['ip']

admin.site.register(Input, InputAdmin)
admin.site.register(Auth , AuthAdmin)
admin.site.register(Clients, ClientAdmin)
admin.site.register(Downloads, DownloadsAdmin)
admin.site.register(Sessions, SessionsAdmin)
admin.site.register(Sensors, SensorAdmin)
