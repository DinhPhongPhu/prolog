from facts import Facts

def varible(x):
    return isinstance(x,str) and x[0].isupper()

def compound(x):
    return isinstance(x,Facts)

def is_list(x):
    return isinstance(x,list)