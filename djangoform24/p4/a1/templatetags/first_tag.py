from django import template
register = template.Library() 
from django.template.loader import get_template

def change_n(value,arg):
    if arg == "change":
        return 'rahim'
register.filter('chnage_name',change_n)




def show_cur():
    
    course =[
    {'id':101,'name':'c++'},
    {'id':102,'name':'py'},
    {'id':103,'name':'js'}
    ]
    return {'course' : course }

print('asik 1000')
cours_template = get_template('course.html')
print('asik 2000')
register.inclusion_tag(cours_template)(show_cur)
    














