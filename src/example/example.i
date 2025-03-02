%module example
%{
#include "example.h"
%}

/* Parse the header file to generate wrappers */
%include "example.h"

%pythoncode %{
class Handler:
    """Opaque type representing the C Handler structure."""
    def __init__(self):
        raise RuntimeError("Cannot instantiate Handler directly. Use alloc_something() instead.")
%}
