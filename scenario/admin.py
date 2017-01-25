from django.contrib import admin

# Register your models here.
from .models import Representative, CompPlan, Tier

admin.site.register(Representative)
admin.site.register(CompPlan)
admin.site.register(Tier)
