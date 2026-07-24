print("Loading documentation types...")
import pkgutil
import importlib

# automatically load all documentation types from the docs package
for importer, modname, ispkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f".{modname}", __name__)