from django import forms
from django.forms import formset_factory
from django.forms.models import ModelForm

from assessment.models import Answer, Question, QuestionOption, Update, Project


class QuestionForm(forms.Form):
    class Meta:
        model = Question
        fields = []


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = []

    def __init__(self, *args, **kwargs):
        super(AnswerForm, self).__init__(*args, **kwargs)
        # self.fields['text'].required=False
        question = kwargs.get('instance')
        if question:
            print(question.type)
            qset = QuestionOption.objects.filter(question=question)
        else:
            qset = QuestionOption.objects.all()

        if question.type == 1:
            print(type(question.type))
            print('radio')

            self.fields['answer'] = forms.ModelChoiceField(
                queryset=qset,
                widget=forms.RadioSelect(attrs={"class": "answer-radio"}),
                empty_label=None
            )
        elif question.type == 2:
            print(type(question.type))
            print('text')
            self.fields['answer'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'answer-radio'}))


    def clean_answer(self):
        if 'answer' in self.cleaned_data:
            return self.cleaned_data['answer']




class CreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('notes',)


class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     question = kwargs.get('instance')

    # def clean_text(self):
    #     if 'text' in self.cleaned_data:
    #         return self.cleaned_data['text']
