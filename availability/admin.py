from django.contrib import admin
from .models import Doctor, RecurringAvailability, DateOverride

admin.site.register(Doctor)
admin.site.register(RecurringAvailability)
admin.site.register(DateOverride)