from django.shortcuts import redirect
from datetime import datetime
from django.urls import reverse_lazy

class ValidatePermissionRequiredMixin(object):
    permission_required = ''
    url_redirect = None

    def get_perms(self):
        if isinstance(self.permission_required,str):
            perms = (self.permission_required,)
        else:
            perms = self.permission_required
        return perms

    def get_url_redirect(self):
        if self.url_redirect is None:
            return reverse_lazy('home')
        return self._url_redirect

    def dispatch(self,request,*args,**kwargs):
        if request.user.has_perms(self.get_perms()):
            return super().dispatch(request,*args,**kwargs)
        return redirect(self.get_url_redirect())