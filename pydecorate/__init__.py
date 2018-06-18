

#from DecoratorBase import DecoratorBase

#from pydecorate.decorator_agg import DecoratorAGG

from .decorator import Decorator
try:
    from .decorator_agg import DecoratorAGG
except ImportError:
    DecoratorAGG = Decorator


