# Přesun do adresáře `install` na přiloženém CD
cd /run/media/<user>/<drive>/install/

# Instalace pouze programu Tracer
sudo rpm -i ./tracer-0.6.2-1.fc22.noarch

# Instalace včetně DNF pluginu
# Netřeba explicitně instalovat balík 'tracer'
sudo rpm -i ./python-dnf-plugins-extras-tracer-0.0.9-1.fc22.noarch
