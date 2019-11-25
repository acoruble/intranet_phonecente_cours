from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import UserPassesTestMixin

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile, TeamMember, Customer

class TeamMemberCreate(UserPassesTestMixin, CreateView):
    template_name = 'utils/form.html'
    model = TeamMember
    fields = ['support_level', ]

    def test_func(self):
        return self.request.user.is_superuser

    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       form.helper = FormHelper()
       form.helper.add_input(Submit('submit', 'Attribuer', css_class='btn-primary'))
       return form

    def get_form_kwargs(self):
        kwargs = super(TeamMemberCreate, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = TeamMember()
        user = UserProfile.objects.get(pk = self.kwargs['user_id'])
        kwargs['instance'].teammember = user
        user.user_type = 1
        user.save()
        return kwargs

    def get_success_url(self):
        return reverse("users:role_attribution")

class CustomerCreate(UserPassesTestMixin, CreateView):
    template_name = 'utils/form.html'
    model = Customer
    fields = ['credits', ]

    def test_func(self):
        return self.request.user.is_superuser

    def get_form(self, form_class=None):
       form = super().get_form(form_class)
       form.helper = FormHelper()
       form.helper.add_input(Submit('submit', 'Attribuer', css_class='btn-primary'))
       return form

    def get_form_kwargs(self):
        kwargs = super(CustomerCreate, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Customer()
        user = UserProfile.objects.get(pk = self.kwargs['user_id'])
        kwargs['instance'].customer = user
        user.user_type = 2
        user.save()
        return kwargs

    def get_success_url(self):
        return reverse("users:role_attribution")
