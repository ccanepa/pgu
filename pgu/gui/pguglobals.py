"""Contains the global reference to the PGU application."""

# pguglobals.py - A place to stick global variables that need to be accessed
#                 from other modules. To avoid problems with circular imports
#                 this module should not import any other PGU module.

# A global reference to the application instance (App class)
app = None

# default key to quit app loop (for debug / develop set to K_F12 by example)
key_app_quit = None

