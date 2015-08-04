>>> import rpm
>>> ts = rpm.TransactionSet()
>>> mi = ts.dbMatch(rpm.RPMTAG_NAME, "vim-X11")
>>> fi = rpm.fi(mi.next())
>>> return [f[0] for f in fi]
