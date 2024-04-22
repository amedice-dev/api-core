from django.contrib import admin

from .models import OrgSocials


class OrgSocialsAdmin(admin.ModelAdmin):
    search_fields = ('whatsapp', 'viber', 'telegram', 'instagram', 'vkontakte', 'facebook',
                     'odnoklassniki', 'youtube', 'imo')

    list_display = ('id', 'whatsapp', 'viber', 'telegram', 'instagram', 'vkontakte', 'facebook',
                    'odnoklassniki', 'youtube', 'imo')


admin.site.register(OrgSocials, OrgSocialsAdmin)
