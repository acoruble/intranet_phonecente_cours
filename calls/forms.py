from django import forms

from users.forms import ModelFormWithSubmit
from .models import Call, CallTag


class NewCallForm(ModelFormWithSubmit):

    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=CallTag.objects.all(),
        )

    class Meta:
        model = Call
        fields = ('title', 'customer', 'tags', 'content', 'solved', )
