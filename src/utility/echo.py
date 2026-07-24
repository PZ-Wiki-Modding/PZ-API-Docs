"""
Console logging utilities with coloured output, warning control, and ~~tqdm~~ support (deactivated here).

@source: https://github.com/Vaileasys/pz-wiki_parser/blob/main/scripts/utils/echo.py
"""
# from tqdm import tqdm
from . import color
from datetime import datetime
from typing import Callable

_ignore_warnings = False # True=Ignore warnings
_warnings_level = 3 # 0=All, 1=Error, 2=Warnings, 3=Deprecated

def noise(*args):
    # if tqdm._instances:
    #     tqdm.write(" ".join(map(str, args)))
    # else:
    print(*args)

def _get_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def _message(message: str, prefix: str, style_func, *, emit_warning: bool = False, warnings_level: int = 3):
    """
    Print a coloured message with optional warning metadata.

    Args:
        message (str): The message text to display.
        prefix (str): Label prefix (e.g., "[Info]", "[Warning]").
        style_func (callable): A function that applies styling (e.g., color.info).
        emit_warning (bool, optional): Whether to append stack info for warnings.
        warnings_level (int, optional): Warning level threshold for display.
    """
    if emit_warning:
        if _ignore_warnings and warnings_level > _warnings_level:
            return
    
    # if emit_warning:
    #     stack = traceback.extract_stack()
    #     write("".join(traceback.format_list(stack)), color.red)

    output = f"{style_func(prefix)} {message}"

    # if tqdm._instances:
    #     tqdm.write(output)
    # else:
    print(output)

def ignore_warnings(warnings_level: int = 0, ignore: bool = True):
    """
    Enable or disable warning output filtering by level.

    Args:
        warnings_level (int): Minimum warning level to show.
        ignore (bool): Whether to suppress warnings below the level.
    """
    global _ignore_warnings, _warnings_level
    _ignore_warnings = ignore
    _warnings_level = warnings_level

def _no_style(message: str):
    """Return the message without any styling."""
    return message

def write(*args, prefix: str = "",style_func: Callable = _no_style, **kwargs):
    """
    Print a standard message safely, supporting tqdm progress bars.

    Args:
        message (str): The message text to print.
        style_func (callable, optional): A colour/style function (e.g. color.info).
    """
    text = " ".join(map(str, args))
    output = (prefix + " " + style_func(text)).strip()

    # if tqdm._instances:
    #     tqdm.write(f"{output}")
    # else:
    print(f"{output}")

def info(message: str, _prefix="Info"):
    """
    Print an informational message in cyan.

    Args:
        message (str): The message text to display.
    """
    _message(message, f"[{_prefix}]", color.info)

def warning(message: str, _prefix="Warning", emit_warning=True, warning_level=2):
    """
    Print a warning message in yellow with warning context.

    Args:
        message (str): The warning text to display.
    """
    _message(message, f"[{_prefix}]", color.warning, emit_warning=emit_warning, warnings_level=warning_level)

def error(message: str, _prefix="Error", emit_warning=True, warnings_level=1):
    """
    Print an error message in red with error context.

    Args:
        message (str): The error text to display.
    """
    _message(message, f"[{_prefix}]", color.error, emit_warning=emit_warning, warnings_level=warnings_level)

def success(message: str):
    """
    Print a success message in green.

    Args:
        message (str): The success message to display.
    """
    _message(message, "[Success]", color.success)

# def debug(message: str):
#     """
#     Print a debug message in magenta if debug mode is enabled.

#     Args:
#         message (str): The debug text to display.
#     """
#     from scripts.core import config_manager as config
#     debug_mode = config.get_debug_mode()

#     if debug_mode:
#         _message(message, "[Debug]", color.debug)

def deprecated(message: str):
    """
    Print a deprecation warning in magenta with warning context.

    Args:
        message (str): The deprecation message to display.
    """
    _message(message, "[Deprecated]", color.debug, emit_warning=True, warnings_level=3)


def time(message, color=color.debug):
    _message(message, f"[{_get_time()}]", color)

def notice(message, color=color.cyan):
    """
    Print a notice message in cyan.

    Args:
        message (str): The notice message to display.
    """
    write(message, color)

def path(*args, color=color.yellow, **kwargs):
    """
    Print a path message in yellow.

    Args:
        message (str): The path message to display.
    """
    write(*args, style_func=color, **kwargs)