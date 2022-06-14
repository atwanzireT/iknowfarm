from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Farmer)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(Recomender)
admin.site.register(FarmerGroup)
admin.site.register(FarmerFile)
admin.site.register(ExGroups)
admin.site.register(ExGroupWorkers)
admin.site.register(Search)

