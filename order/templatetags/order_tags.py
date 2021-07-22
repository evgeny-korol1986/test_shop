from django import template

register = template.Library()

@register.inclusion_tag('order/pagination.html', takes_context=True)
def show_pagination(context):
    request = context['request']

    # GET parameters without page
    parameters = [f'{key}={val}' for key, val in request.GET.items() if not key == 'page']

    url = request.path + '?' + '&'.join(parameters)
    url += '&page=' if parameters else 'page='
    context['current_url'] = url
    return context
