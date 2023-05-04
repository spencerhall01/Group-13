from django import template
from re import IGNORECASE, compile, escape as rescape
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='highlight')
def highlight(text, search):
    rgx = compile(rescape(search), IGNORECASE)
    return mark_safe(
        rgx.sub(
            lambda m: '<b style="background-color: #fe0; padding: 3px 8px; border-radius: 8px; color:#000">{}</b>'.format(m.group()),
            text
        )
    )