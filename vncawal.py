import os

cmd = 'sudo apt update'
os.system(cmd)
cmd = 'wget https://gitlab.com/firsakamala/firsa/-/raw/main/CRP10_ShortVPN-Fox.ascr'
os.system(cmd)
cmd = 'wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes xfce4 desktop-base dbus-x11'
os.system(cmd)
cmd = 'sudo apt install xfce4-terminal -y'
os.system(cmd)
cmd = 'sudo apt install firefox-esr -y'
os.system(cmd)
cmd = 'sudo apt install actionaz -y'
os.system(cmd)
cmd = 'sudo apt-get install geany -y'
os.system(cmd)
cmd = 'sudo apt install iputils-ping -y'
os.sytem(cmd)
print("vnc up")
