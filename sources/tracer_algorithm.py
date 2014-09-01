packages = seznam balíčků modifikovaných od spuštění systému
processes_files = BTree(...)
for package in packages:
    for package_file in package_files:
	processes = processes_files[package_file]
	if processes != prázdná množina:
	    print processes
