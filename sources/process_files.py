import psutil
p = psutil.Process(pid)
for mmap in p.get_memory_maps():
    print mmap.path
