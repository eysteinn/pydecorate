

#from DecoratorBase import DecoratorBase

#from pydecorate.decorator_agg import DecoratorAGG

from .decorator import Decorator
try:
    import aggdraw
    from .decorator_agg import DecoratorAGG
except ImportError:
    print('Failed to import aggdraw, falling back to PIL')
    DecoratorAGG = Decorator


