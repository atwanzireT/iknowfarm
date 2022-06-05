from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *

# Register your models here.
admin.site.register(
    FarmerGroup,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(SingleFarmer)
admin.site.register(Country)
admin.site.register(District)
admin.site.register(Village)
