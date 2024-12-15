from django.contrib import admin
from Admin.models import User,OfficeStaff,LibraryHistory,Librarian

# Register your models here.

admin.site.register(User),
admin.site.register(OfficeStaff),
admin.site.register(Librarian)