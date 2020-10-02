.. _building-isos:

*************
Building ISOs
*************

Since Cobbler uses the systemd hardening option "PrivateTmp" you can't write or read files from your ``/tmp`` when you
run Cobbler via systemd as a service.

Per default this builds an ISO for all available systems and profiles.

Additional dependencies
#######################

If you wish to generate grub2 bootloaders in the EFI format please install the dependencies according to the arches you
wish to boot with your Cobbler installation: ``grob2-ARCH-efi-modules``.

The script mkgrub.sh
####################

This script can create a bootable grub2 Bootloader in the EFI format.

The script can be manipulated in the following way:

* The env variable ``SYSLINUX_DIR``. If not set this defaults to ``/usr/share/syslinux``.
* The env variable ``GRUB2_MOD_DIR``. If not set this defaults to ``/usr/share/grub2``.

Current Workflow
################

#. Created a bootable grubx64.efi loader via ``/usr/share/cobbler/bin/mkgrub.sh``
#. copied that loader to tftp root folder
#. in ``/etc/cobbler/settings`` ``grubconfig_dir`` has to be set to ``/var/lib/cobbler/grub_config``
#. ``cobbler sync`` automatically populates the grub configuration directory now in tftp root folder
#. In your dhcp server, point option 67 (``filename``) to ``grubx64.efi`` (assuming you have configured the other
   options already)

When you want to use cloud init with the new subiquity installer in Ubuntu 20.04, please keep in mind that the nocloud
source has to be quoted in grub, otherwise it won't work. For syslinux however, the nocloud source mustn't be quoted!
That said, currently you can't use cloud init profiles for Ubuntu 20.04 simultaneously in both syslinux and grub.

Building Standalone ISOs
########################

You need to give the parameters:

* ``--standalone``
* ``--distro``
* ``--source``

Building Netinstaller ISOs
##########################

TODO
