from django import template

register = template.Library()

@register.filter
def hide_forbidden(value):
    words = value.split()
    result = []
    for word in words:
        if word in hide_forbidden:
            result.append(word[0] + "*"*(len(word)-2) + word[-1])
        else:
            result.append(word)

    return " ".join(result)
