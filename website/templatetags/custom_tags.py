from django import template

register = template.Library()

def replace_img(value):
    return str(value).replace('website', '..')


register.filter('replace_img', replace_img)