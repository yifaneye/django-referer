
django-referer
==============

django-referer is a Django app for displaying different referer details based on query parameter.
It provides sales, partners and affiliates custom links to send out to the public.
It gives sales, partners and affiliates their opportunity to convert every contact detail on the website to their own.
It thus encourages sales, partners and affiliates to promote the website and the business.
Also, with the help of analytics scripts, there will be information about which sales gets most clicks.

Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`_ to install django-referer.

.. code-block:: bash

   pip install django-referer

Usage
-----

Step 1. Add referer middleware (in settings.py file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   MIDDLEWARE = [
       'referer.middleware.referer.RefererMiddleware',  # here 
       'django.middleware.security.SecurityMiddleware',
       '...'
   ]

Step 2. Add referer context processors (in settings.py file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   TEMPLATES = [
       {
           'OPTIONS': {
               'context_processors': [
                   '...',
                   'django.contrib.messages.context_processors.messages',
                   'referer.context_processors.referer',  # here
               ],
           },
       },
   ]

Step 3. Customize referer settings (in settings.py file) (optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The defaults are:

.. code-block:: python

   REFERER_LINK_PARAMETER = 'referer'
   REFERER_DEFAULT_ID = 1
   # ?referer=1

   REFERER_MODEL_FROM = 'django.contrib.auth.models'
   REFERER_MODEL_IMPORT = 'User'
   # from REFERER_MODEL_FROM import REFERER_MODEL_IMPORT

   REFERER_IGNORED_LINKS = []

Step 4. Display referer information (in .html file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: html

   <a href="mailto:{{ referer.email }}">Email</a>
   <p>{{ referer.first_name }} {{ referer.last_name }}</p>

Contributing
------------

Pull requests are welcome.

License
-------

`MIT <https://choosealicense.com/licenses/mit/>`_
