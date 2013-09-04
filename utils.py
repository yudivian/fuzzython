__author__ = ''

#region Decorators

def norm(type_=None, name=None):
    """
    Function decorator for defining a norm
    :param type_: norm's type
    :param name: norm's name
    """
    def decorator(func):
        func.norm = type_
        func.name = name
        return func
    return decorator



def timer(label:str='', trace:bool=True):
    """
    Function decorator for measure method
    :param label: label to print
    :param trace: print info if it's value is True
    """
    label += ' ' if label else ''
    import time
    def on_decorator(func):
        def on_call(*args, **kwargs):
            start = time.clock()
            result = func(*args, **kwargs)
            elapsed = time.clock() - start
            #on_call.all_times += elapsed
            if trace:
                values = (label, func.__name__, elapsed)
                print('{0}{1}: {2:.5f}s'.format(*values))
            return result
        on_call.__annotations__ = func.__annotations__
        #on_call.all_times = 0
        return on_call
    return on_decorator

#endregion


