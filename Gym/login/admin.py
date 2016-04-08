from django.contrib import admin
from login.models import UserProfile,members,w1_cardio,w1_fullbody,w2_cardio,w2_lowerbody,w3_legs,w2_upperbody,w3_back,w3_cardio,w3_chest
from .models import table1,table2,table3,table4,table5,table6,table7,table8,table9,table10,table11,table12,table13
from .models import table14,table15,table16,table17,table18,table18,table19,table20,table21,table22,table23,table24
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# class UserProfileInline(admin.StackedInline):
# 	model = UserProfile
# 	can_delete = False
# 	can_update = True
# 	verbose_name_plural = 'user'
# class UserAdmin(UserAdmin):
# 	inlines = (UserProfileInline,)
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(members)
admin.site.register(w1_cardio)
admin.site.register(w1_fullbody)
admin.site.register(w2_cardio)
admin.site.register(w2_lowerbody)
admin.site.register(w3_legs)
admin.site.register(w2_upperbody)
admin.site.register(w3_back)
admin.site.register(w3_chest)
admin.site.register(w3_cardio)
admin.site.register(table1)
admin.site.register(table2)
admin.site.register(table3)
admin.site.register(table4)
admin.site.register(table5)
admin.site.register(table6)
admin.site.register(table7)
admin.site.register(table8)
admin.site.register(table9)
admin.site.register(table10)
admin.site.register(table11)
admin.site.register(table12)
admin.site.register(table13)
admin.site.register(table14)
admin.site.register(table15)
admin.site.register(table16)
admin.site.register(table17)
admin.site.register(table18)
admin.site.register(table19)
admin.site.register(table20)
admin.site.register(table21)
admin.site.register(table22)
admin.site.register(table23)
admin.site.register(table24)