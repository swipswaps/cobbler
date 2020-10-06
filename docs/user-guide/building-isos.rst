.. _building-isos:

*************
Building ISOs
*************

Since Cobbler uses the systemd hardening option "PrivateTmp" you can't write or read files from your ``/tmp`` when you
run Cobbler via systemd as a service.

Per default this builds an ISO for all available systems and profiles.

Building Standalone ISOs
########################

You need to give the parameters:

* ``--standalone``
* ``--distro``
* ``--source``

Building Netinstaller ISOs
##########################

TODO
