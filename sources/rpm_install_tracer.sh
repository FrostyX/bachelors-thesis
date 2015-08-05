# Přesun do adresáře `install` na přiloženém CD
cd /run/media/<user>/<drive>/install/

# Instalace pouze programu Tracer
sudo dnf install ./tracer-0.6.2-1.fc22.noarch

# Instalace včetně DNF pluginu
# Netřeba explicitně instalovat balík 'tracer'
sudo dnf install ./python-dnf-plugins-extras-tracer-0.0.9-1.fc22.noarch
