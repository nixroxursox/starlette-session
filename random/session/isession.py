from zope.interface import Attribute, Interface


class IDict(Interface):
    # Documentation-only interface

    def __contains__(k):
        """Return ``True`` if key ``k`` exists in the dictionary."""

    def __setitem__(k, value):
        """Set a key/value pair into the dictionary"""

    def __delitem__(k):
        """Delete an item from the dictionary which is passed to the
        renderer as the renderer globals dictionary."""

    def __getitem__(k):
        """Return the value for key ``k`` from the dictionary or raise a
        KeyError if the key doesn't exist"""

    def __iter__():
        """Return an iterator over the keys of this dictionary"""

    def get(k, default=None):
        """Return the value for key ``k`` from the renderer dictionary, or
        the default if no such value exists."""

    def items():
        """Return a list of [(k,v)] pairs from the dictionary"""

    def keys():
        """Return a list of keys from the dictionary"""

    def values():
        """Return a list of values from the dictionary"""

    def pop(k, default=None):
        """Pop the key k from the dictionary and return its value.  If k
        doesn't exist, and default is provided, return the default.  If k
        doesn't exist and default is not provided, raise a KeyError."""

    def popitem():
        """Pop the item with key k from the dictionary and return it as a
        two-tuple (k, v).  If k doesn't exist, raise a KeyError."""

    def setdefault(k, default=None):
        """Return the existing value for key ``k`` in the dictionary.  If no
        value with ``k`` exists in the dictionary, set the ``default``
        value into the dictionary under the k name passed.  If a value already
        existed in the dictionary, return it.  If a value did not exist in
        the dictionary, return the default"""

    def update(d):
        """Update the renderer dictionary with another dictionary ``d``."""

    def clear():
        """Clear all values from the dictionary"""





class ISession(IDict):
    """An interface representing a session (a web session object,
    usually accessed via ``request.session``.

    Keys and values of a session must be JSON-serializable.

    .. warning::

        In :app:`Pyramid` 2.0 the session was changed to only be required to
        support types that can be serialized using JSON. It's recommended to
        switch any session implementations to support only JSON and to only
        store primitive types in sessions. See
        :ref:`upgrading_session_20` for more information about why this
        change was made.

    .. versionchanged:: 1.9

        Sessions are no longer required to implement ``get_csrf_token`` and
        ``new_csrf_token``. CSRF token support was moved to the pluggable
        :class:`pyramid.interfaces.ICSRFStoragePolicy` configuration hook.

    .. versionchanged:: 2.0

        Sessions now need to be JSON-serializable. This is more strict than
        the previous requirement of pickleable objects.

    """

    # attributes

    created = Attribute('Integer representing Epoch time when created.')
    new = Attribute('Boolean attribute.  If ``True``, the session is new.')

    # special methods

    def invalidate():
        """Invalidate the session.  The action caused by
        ``invalidate`` is implementation-dependent, but it should have
        the effect of completely dissociating any data stored in the
        session with the current request.  It might set response
        values (such as one which clears a cookie), or it might not.

        An invalidated session may be used after the call to ``invalidate``
        with the effect that a new session is created to store the data. This
        enables workflows requiring an entirely new session, such as in the
        case of changing privilege levels or preventing fixation attacks.
        """

    def changed():
        """Mark the session as changed. A user of a session should
        call this method after he or she mutates a mutable object that
        is *a value of the session* (it should not be required after
        mutating the session itself).  For example, if the user has
        stored a dictionary in the session under the key ``foo``, and
        he or she does ``session['foo'] = {}``, ``changed()`` needn't
        be called.  However, if subsequently he or she does
        ``session['foo']['a'] = 1``, ``changed()`` must be called for
        the sessioning machinery to notice the mutation of the
        internal dictionary."""

    def flash(msg, queue='', allow_duplicate=True):
        """Push a flash message onto the end of the flash queue represented
        by ``queue``.  An alternate flash message queue can used by passing
        an optional ``queue``, which must be a string.  If
        ``allow_duplicate`` is false, if the ``msg`` already exists in the
        queue, it will not be re-added."""

    def pop_flash(queue=''):
        """Pop a queue from the flash storage.  The queue is removed from
        flash storage after this message is called.  The queue is returned;
        it is a list of flash messages added by
        :meth:`pyramid.interfaces.ISession.flash`"""

    def peek_flash(queue=''):
        """Peek at a queue in the flash storage.  The queue remains in
        flash storage after this message is called.  The queue is returned;
        it is a list of flash messages added by
        :meth:`pyramid.interfaces.ISession.flash`
        """




