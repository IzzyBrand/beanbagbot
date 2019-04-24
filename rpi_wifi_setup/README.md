# Overview

I got fed up with using the Pi's built-in WiFi as an access point. Raspbian Stretch changed up a lot of networking stuff, and it appears that most of the tutorials on the internet right now are broken in one way or another. Instead I'm using [an external Realtek WiFi dongle](https://www.amazon.com/BrosTrend-1200Mbps-Adapter-Wireless-Antennas/dp/B01IEU7UZ0/ref=sr_1_fkmrnull_5?keywords=brostrend+wifi+dongle&qid=1556078946&s=gateway&sr=8-5-fkmrnull) that will give me better range and I found a bit easier to configure.

## Install the Realtek driver

I used some tools mentioned on [this forum post](https://www.raspberrypi.org/forums/viewtopic.php?t=178405#p1136676) to automatically install the appropriate driver for my wifi dongle.

With the dongle plugged in, those instructions were to:

```
sudo wget http://www.fars-robotics.net/install-wifi -O /usr/bin/install-wifi
sudo chmod +x /usr/bin/install-wifi
sudo install-wifi
```

Then `sudo reboot` and try `ifconfig` and `iwconfig` to see if the interface shows up.

## Set predictable interface names

Use `sudo raspi-config` to enable predicatble interface names. We need to ensure that USB WiFi dongle comes up as the same interface every time.

Again `sudo reboot` and try `ifconfig` and `iwconfig` to see what the interface is called.

## Install hostapd and dnsmasq

My understanding is that hostapd actually runs the accesspoint, while dnsmasq runs a little DNS server (assigning domain names to IP addresses) on the PI. We'll need them both.

```
sudo apt install hostapd dnsmasq
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
```

## Configure a bunch of files

I've included my configuration for each of the files in this folder. They correspond to:

 * `/etc/dhcpcd.conf` set the static IP address for the AP
 * `/etc/hostapd/hostapd.conf` this is where the AP is configured
 * `/etc/default/hostapd` tells the hostapd service to use our configuration file
 * `/etc/dnsmasq.conf` specify the range of IP addresses to be used in dhcp