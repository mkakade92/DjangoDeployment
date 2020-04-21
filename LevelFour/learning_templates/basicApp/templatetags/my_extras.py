from django import template

register=template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "args" from th string
    """
    print("sl;ds;aldj;sa")
    print(value.replace(arg,'Maitraya'))
    return value.replace(arg,'Maitraya')

# register.filter('cut',cut)
