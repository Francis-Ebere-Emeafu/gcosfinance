from django.contrib import admin
from assessment.models import Category,  Question, QuestionOption, Answer, Project, Update


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', ]



class QuestionOptionInline(admin.TabularInline):
    model = QuestionOption


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'added_at', ]

    inlines = [QuestionOptionInline]


@admin.register(QuestionOption)
class QuestionOptionAdmin(admin.ModelAdmin):
    list_display = ['question', 'text', 'weight', ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['description', 'status',]

@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ['project', 'notes', 'added_by', 'update_date']
