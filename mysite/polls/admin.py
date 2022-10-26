from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice


# admin.site.register(Question)
# admin.site.register(Choice)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_data', 'question_text']
    list_filter = ['pub_data']
    list_display = ('question_text','pub_data','was_published_recently')
    search_fields = ['question_text']
    fieldsets = [(None, {'fields': ['question_text']}), ('Date infomation', {'fields': ['pub_data']}), ]
    # fieldsets = [ (None, {'fields': ['question_text']}), ('Date information', {'fields': ['pub_date']}),]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
