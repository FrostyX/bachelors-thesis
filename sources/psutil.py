>>> import psutil
>>> p = psutil.Process(pid)

>>> p.pid
13005

>>> p.name()
'gvim'

>>> p.username()
'frostyx'

>>> p.create_time()
1408897172.2

>>> p
<psutil.Process(pid=13005, name='gvim') at 3071122124>
