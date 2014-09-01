>>> import subprocess
>>> process = subprocess.Popen(['rpm', '-qi', 'vim-X11'], stdout=subprocess.PIPE)
>>> out = process.communicate()[0]
>>> out = out.split('\n')
