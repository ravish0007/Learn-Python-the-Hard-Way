age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

"""
1.)
pydoc raw_input

Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.

2.)
pydoc open

Help on built-in function open in module __builtin__:

open(...)
    open(name[, mode[, buffering]]) -> file object

    Open a file using the file() type, returns a file object.  This is the
    preferred way to open a file.  See file.__doc__ for further information.

3.)
pydoc file

Help on class file in module __builtin__:

class file(object)
 |  file(name[, mode[, buffering]]) -> file object
 |
 |  Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
 |  writing or appending.  The file will be created if it doesn't exist
 |  when opened for writing or appending; it will be truncated when
 |  opened for writing.  Add a 'b' to the mode for binary files.
 |  Add a '+' to the mode to allow simultaneous reading and writing.
 |  If the buffering argument is given, 0 means unbuffered, 1 means line
 |  buffered, and larger numbers specify the buffer size.  The preferred way
 |  to open a file is with the builtin open() function.
 |  Add a 'U' to mode to open the file for input with universal newline
 |  support.  Any line ending in the input file will be seen as a '\n'
 |  in Python.  Also, a file so opened gains the attribute 'newlines';
 |  the value for this attribute is one of None (no newline read yet),
 |  '\r', '\n', '\r\n' or a tuple containing all the newline types seen.
 |
 |  'U' cannot be combined with 'w' or '+' mode.

4.)
pydoc os

Help on module os:

NAME
    os - OS routines for Mac, NT, or Posix depending on what system we're on.

FILE
    /usr/lib/python2.7/os.py

MODULE DOCS
    http://docs.python.org/library/os

DESCRIPTION
    This exports:
      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
      - os.path is one of the modules posixpath, or ntpath
      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
      - os.curdir is a string representing the current directory ('.' or ':')
      - os.pardir is a string representing the parent directory ('..' or '::')
      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
      - os.extsep is the extension separator ('.' or '/')
      - os.altsep is the alternate pathname separator (None or '/')
      - os.pathsep is the component separator used in $PATH etc
      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
      - os.defpath is the default search path for executables
      - os.devnull is the file path of the null device ('/dev/null', etc.)

    Programs that import and use 'os' stand a better chance of being
    portable between different platforms.  Of course, they must then
    only use functions that are defined by all platforms (e.g., unlink
    and opendir), and leave all pathname manipulation to os.path
    (e.g., split and join).

5.)
pydoc sys
Help on built-in module sys:

NAME
    sys

FILE
    (built-in)

MODULE DOCS
    http://docs.python.org/library/sys

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.

    Dynamic objects:

    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules

    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.

    exitfunc -- if sys.exitfunc exists, this routine is called when Python exits
      Assigning to sys.exitfunc is deprecated; use the atexit module instead.

    stdin -- standard input file object; used by raw_input() and input()
    stdout -- standard output file object; used by the print statement
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.

    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.

    exc_type -- type of exception currently being handled
    exc_value -- value of exception currently being handled
    exc_traceback -- traceback of exception currently being handled
      The function exc_info() should be used instead of these three,
      because it is thread-safe.
"""
