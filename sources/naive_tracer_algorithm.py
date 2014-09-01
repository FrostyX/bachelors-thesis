packages = seznam balíčků modifikovaných od spuštění systému
processes = seznam všech spuštěných procesů
for package in packages:
    for process in processes:
        if množinový_průnik(package_files, process_files) != prázdná množina
            print process
