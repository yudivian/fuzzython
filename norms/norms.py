from utils import norm

__author__ = ''


@norm(type_='TNORM', name='MIN')
def minimum(*args:float) -> float:
    return min(args)

@norm(type_='SNORM', name='MAX')
def maximum(*args:float) -> float:
    return max(args)


@norm(type_='TNORM', name='PROD')
def algebraic_product(x:float, y:float) -> float:
    return x*y

@norm(type_='SNORM', name='ASUM')
def algebraic_sum(x:float, y:float) -> float:
    return x+y-x*y


@norm(type_='TNORM', name='BDIF')
def bounded_difference(x:float, y:float) -> float:
    return max(0.0, x+y-1.0)

@norm(type_='SNORM', name='BSUM')
def bounded_sum(x:float, y:float) -> float:
    return min(1.0, x+y)


@norm(type_='TNORM', name='DPROD')
def drastic_product(x:float, y:float) -> float:
    if x==1: return y
    if y==1: return x
    return 0.0

@norm(type_='SNORM', name='DSUM')
def drastic_sum(x:float, y:float) -> float:
    if x==0: return y
    if y==0: return x
    return 1.0


@norm(type_='TNORM', name='EPROD')
def einstein_product(x:float, y:float) -> float:
    return (x*y)/(1.+(1.-x)*(1.-y))

@norm(type_='SNORM', name='ESUM')
def einstein_sum(x:float, y:float) -> float:
    return (x+y)/(1.+x*y)


@norm(type_='TNORM', name='FAND')
def fuzzy_and(x:float, y:float, p:float=0.5) -> float:
    return (1.-p)*min(x,y) + p*(x+y)/2.

@norm(type_='SNORM', name='FOR')
def fuzzy_or(x:float, y:float, p:float=0.5) -> float:
    return p*max(x,y) + (1.-p)*(x+y)/2.


@norm(type_='SNORM', name='NSUM')
def normalised_sum(x:float, y:float) -> float:
    num = x + y
    return num / max(1, num)

# def arithmetic_mean(*args):
#     return sum(args)/len(args)


@norm(type_='CNORM', name='ZADEH')
def zadeh_complement(x:float) -> float:
    return 1 - x

@norm(type_='CNORM', name='SUGENO')
def sugeno_complement(x, lambda_=0):
    return (1 - x) / (1+ lambda_*x)

@norm(type_='CNORM', name='YAGER')
def yager_complement(x, w=1):
    return pow((1 - pow(x, w)), 1/w)


# add more norms below or...
# add each norm in a new .py file with the name of the norm
# for both cases above we need to use the norm decorator from utils

def get_norm(name):
    """
    Search for a norm with a given name inside norms package
    :param name: norm's name specified in @norm decorator
    :return: a norm function if exists
    """
    for name_, func_ in globals().items():
        if callable(func_) and hasattr(func_, 'name'):
            if func_.name == name or name_ == name:
                return func_
    try:
        name_ = name.lower()
        module = __import__('norms.'+name_, fromlist=(name,))
        for n, f in module.__dict__.items():
            if callable(f) and hasattr(f, 'name'):
                if f.name == name: # or n == name:
                    return f
    except Exception as e:
        print('unsupported norm {}'.format(name))
        pass
