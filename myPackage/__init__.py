"""
Awesome description of the package here!

`pdoc` only extracts _public API_ documentation.[^public]
All objects (modules, functions, classes, variables) are only
considered public if their _identifiers don't begin with an
underscore_ ( \\_ ).[^private]

[^public]:
    Here, public API refers to the API that is made available
    to your project end-users, not the public API e.g. of a
    private class that can be reasonably extended elsewhere
    by your project developers.

[^private]:
    Prefixing private, implementation-specific objects with
    an underscore is [a common convention].

[a common convention]: https://docs.python.org/3/tutorial/classes.html#private-variables

In addition, if a module defines [`__all__`][__all__], then only
the identifiers contained in this list will be considered public.
Otherwise, a module's global identifiers are considered public
only if they don't begin with an underscore and are defined
in this exact module (i.e. not imported from somewhere else).

[__all__]: https://docs.python.org/3/tutorial/modules.html#importing-from-a-package

By transitivity, sub-objects of non-public objects
(e.g. submodules of non-public modules, methods of non-public classes etc.)
are not public and thus not documented.


Where does `pdoc` get documentation from?
-----------------------------------------
In Python, objects like modules, functions, classes, and methods
have a special attribute `__doc__` which contains that object's
documentation string ([docstring][docstrings]).
For example, the following code defines a function with a docstring
and shows how to access its contents:

    >>> def test():
    ...     ""This is a docstring.""
    ...     pass
    ...
    >>> test.__doc__
    'This is a docstring.'

It's pretty much the same with classes and modules.
See [PEP-257] for Python docstring conventions.

[PEP-257]: https://www.python.org/dev/peps/pep-0257/

These docstrings are set as descriptions for each module, class,
function, and method listed in the documentation produced by `pdoc`.

`pdoc` extends the standard use of docstrings in Python in two
important ways: by allowing methods to inherit docstrings, and
by introducing syntax for docstrings for variables.


### Docstrings inheritance

`pdoc` considers methods' docstrings inherited from superclass methods',
following the normal class inheritance patterns.
Consider the following code example:

    >>> class A:
    ...     def test(self):
    ...         ""Docstring for A.""
    ...         pass
    ...
    >>> class B(A):
    ...     def test(self):
    ...         pass
    ...
    >>> A.test.__doc__
    'Docstring for A.'
    >>> B.test.__doc__
    None

In Python, the docstring for `B.test` doesn't exist, even though a
docstring was defined for `A.test`.
When `pdoc` generates documentation for the code such as above,
it will automatically attach the docstring for `A.test` to
`B.test` if `B.test` does not define its own docstring.
In the default HTML template, such inherited docstrings are greyed out.
"""
