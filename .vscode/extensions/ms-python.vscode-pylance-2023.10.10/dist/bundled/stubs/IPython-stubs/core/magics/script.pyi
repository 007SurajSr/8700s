"""
This type stub file was generated by pyright.
"""

from IPython.core import magic_arguments
from IPython.core.magic import Magics, cell_magic, line_magic, magics_class

"""Magic functions for running cells in various scripts."""
def script_args(f):
    """single decorator for adding script args"""
    ...

@magics_class
class ScriptMagics(Magics):
    """Magics for talking to scripts
    
    This defines a base `%%script` cell magic for running a cell
    with a program in a subprocess, and registers a few top-level
    magics that call %%script with common interpreters.
    """
    event_loop = ...
    script_magics = ...
    script_paths = ...
    def __init__(self, shell=...) -> None:
        ...
    
    def __del__(self): # -> None:
        ...
    
    @magic_arguments.magic_arguments()
    @script_args
    @cell_magic("script")
    def shebang(self, line, cell):
        """Run a cell via a shell command

        The `%%script` line is like the #! line of script,
        specifying a program (bash, perl, ruby, etc.) with which to run.

        The rest of the cell is run by that program.

        Examples
        --------
        ::

            In [1]: %%script bash
               ...: for i in 1 2 3; do
               ...:   echo $i
               ...: done
            1
            2
            3
        """
        ...
    
    @line_magic("killbgscripts")
    def killbgscripts(self, _nouse_=...): # -> None:
        """Kill all BG processes started by %%script and its family."""
        ...
    
    def kill_bg_processes(self): # -> None:
        """Kill all BG processes which are still running."""
        ...
    


