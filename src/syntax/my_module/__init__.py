# This signifies a module, and is loaded on module import

from my_module.script import my_module_func

# This special array exposes things for import, like `from my_module import my_module_func`
__all__ = ["my_module_func"]
