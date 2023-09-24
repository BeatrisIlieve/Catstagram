from django.shortcuts import redirect


def is_owner(request, obj):
    return request.user == obj.user

# class OwnerRequiredMixin(BaseUpdateView):
#     def get(self, request, *args, **kwargs):
#         result = super().get(request, *args, **kwargs)
#
#         if request.user == self.object.user:
#             return result
#         else:
#             redirect('index')
