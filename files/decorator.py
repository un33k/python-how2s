def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper

def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper



@p_decorate
@div_decorate
@strong_decorate
def get_text(name):
   return "{0}, you can do it".format(name)

# OR

get_text = p_decorate(div_decorate(strong_decorate(get_text)))


print get_text("Mike")

# Outputs
#<p><div><strong>Mike, you can do it.</strong></div></p>


