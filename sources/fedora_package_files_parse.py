>>> process = subprocess.Popen(['rpm', '-ql', 'vim-X11'], stdout=subprocess.PIPE)
>>> files = process.communicate()[0]
>>> files = files.split('\n')[:-1]
