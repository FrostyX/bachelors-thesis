>>> import rpm
>>> ts = rpm.TransactionSet()
>>> mi = ts.dbMatch("name", "vim-X11")
>>> package_hdr = mi.next()

>>> package_hdr[rpm.RPMTAG_SUMMARY]
# The VIM version of the vi editor for the X Window System

>>> package.category = package_hdr[rpm.RPMTAG_GROUP]
# Applications/Editors
