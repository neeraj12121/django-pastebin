from django.contrib import admin

class PasteAdmin(admin.ModelAdmin):
    list_display = ('__str__','title', 'poster', 'syntax', 'timestamp')
    list_filter = ('timestamp', 'syntax')

admin.site.register(Pastebin,PasteAdmin)
