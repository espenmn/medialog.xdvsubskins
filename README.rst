
Introduction
============

The ``medialog.xdvsubskins`` package uses the **theming** and **packaging** features
available in `plone.app.theming`_ to make medialog.subskins 
available in for plona.app.theming in `Plone 4.1`_.

.. image:: http://products.medialog/xdvsubskins.png

Installation
------------

Add Plone site
~~~~~~~~~~~~~~

Install Plone 4.1 with `plone.app.theming`_ and create a Plone site (if you have not already)
with Diazo theming configured.



Buildout
~~~~~~~~

If you are a developer, you might enjoy installation via buildout.

Add ``medialog.xdvsubskins`` to your ``plone.recipe.zope2instance`` section's *eggs* parameter e.g.::

    [instance]
    eggs =
        Plone
        …
        medialog.xdvsubskins

Select theme
~~~~~~~~~~~~

Select and enable the theme from the Diazo control panel. That's it!

Help
----

Obviously there is more work to be done. If you want to help, pull requests accepted! Some ideas:

* Add a diazo rule to import Plone editing styles
* Configure styles to use portal_css
* Add quick installer support
* Improve styles 

Authors
-------

This product was developed by espen Moe-Nilssen.


License
-------

The author is not a "license guy", but the earthlingtwo theme is distributed via CC 3.0 license [1]_ and this package is GPL version 2 (assuming that makes sense).

.. _`earthlingtwo`: http://www.freecsstemplates.org/preview/earthlingtwo/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
.. _`CSS Templates`: http://www.freecsstemplates.org/

.. [1] http://www.freecsstemplates.org/license/