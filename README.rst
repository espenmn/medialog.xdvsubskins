
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


Install medialog.subskins
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Install medialog.subskins from the add-ons control panel



Select theme
~~~~~~~~~~~~
Select and enable the theme from the Diazo control panel. 


Configure layout
~~~~~~~~~~~~~~~~~~~~~~~~
Click the subskins control panel at top right (twice if your site is not in debug mode) and select your layout.
You can also click the "manage-viewlets" link an hide / show / move viewlets (there are a few hidden by default)



Help
----

Obviously there is more work to be done. If you want to help, pull requests accepted! 




Authors
-------

This product was developed by Espen Moe-Nilssen.


