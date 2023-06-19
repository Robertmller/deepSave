from django.contrib import admin
from pf_person.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "rg", "expedition_time", "expedition_org", "cpf", "email", "born_date", "city", "cep",
                    "reference", "street", "street_number", "mother_name", "dad_name", "partiner_name", "isPj", "hasGovAccount"]

    @admin.display(ordering="name")
    def name(self, obj):
        return obj.name.name


admin.site.register(Person, PersonAdmin)
