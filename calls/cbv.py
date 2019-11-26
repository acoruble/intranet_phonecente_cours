from django.views.generic import DeleteView
from django import http
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse

from .models import Call


class CallDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'utils/delete_view.html'
    model = Call

    def test_func(self):
        self.object = self.get_object()
        return self.request.user.user_type == 1 and self.object.teammember == self.request.user.teammember

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.teammember == self.request.user.teammember:
            success_url = self.get_success_url()
            self.object.delete()
            return http.HttpResponseRedirect(success_url)
        else:
            return http.HttpResponseForbidden("Cannot delete other's calls")

    def get_success_url(self):
        return reverse("calls:call_list") 
