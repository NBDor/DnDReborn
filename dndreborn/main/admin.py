from django.contrib import admin
from .models import Journal, Item, Character, Subject, Paragraph, Ability, Skill

# Register your models here.
admin.site.register(Journal)
admin.site.register(Item)
admin.site.register(Character)
admin.site.register(Ability)
admin.site.register(Skill)
admin.site.register(Subject)
admin.site.register(Paragraph)

