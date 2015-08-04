>>> import subprocess
>>> cmd = ['rpm', '-qi', 'vim-X11']
>>> process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
>>> out = process.communicate()[0]
>>> out = out.split('\n')
