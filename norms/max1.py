from utils import norm

__author__ = ''

@norm(type_='SNORM', name='MAX1')
def maximum(*args:float) -> float:
    """
    This function is only to show a norm definition
    """
    print('--- max1 ---')
    return max(args)
