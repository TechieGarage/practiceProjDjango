from django import template

register = template.Library()

# Method-1
# Create custom filter
#def cut(value, arg):
#    """
#    This cuts out all values of "arg" from the string.
#    """
#    return value.replace(arg, "")
#
#register.filter('cutFilter', cut) # Now register the custom filter. 'cutFilter' is name of filter
#                                  # and 'cut' is the actual custom filter.



# Method-2
# We can also use decorator to register filter
@register.filter(name='cutFilter1')
def cut(value, arg):
    """
    This cuts out all values of "arg" from the string.
    """
    return value.replace(arg, "")
