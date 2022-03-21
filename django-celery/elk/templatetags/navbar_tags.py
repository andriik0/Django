import re

from django import template

register = template.Library()


@register.simple_tag
def is_active(request, pattern):
    pattern = pattern.replace('__username__', request.user.username)
    if re.search(pattern, request.path):
        return 'active'
    return ''
