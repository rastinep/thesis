#!/usr/bin/env python

 

from mininet.net  import Mininet

from mininet.node import RemoteController

from mininet.link import TCLink

from mininet.cli  import CLI


net = Mininet(link=TCLink);

 

# Add hosts and switches

Host1  = net.addHost('h1')
Host2  = net.addHost('h2')
Host3  = net.addHost('h3')

Switch1 = net.addSwitch('s1')
Switch2 = net.addSwitch('s2')
Switch3 = net.addSwitch('s3')
Switch4 = net.addSwitch('s4')
Switch5 = net.addSwitch('s5')
Switch6 = net.addSwitch('s6')
Switch7 = net.addSwitch('s7')
Switch8 = net.addSwitch('s8')
Switch9 = net.addSwitch('s9')
 

# Add links

# set link speeds to 10Mbit/s

linkopts = dict(bw=10)

net.addLink(Host1,   Switch1,    **linkopts )
net.addLink(Switch1,  Switch2,    **linkopts )
net.addLink(Switch1,  Switch4,    **linkopts )
net.addLink(Switch1,  Switch5,    **linkopts )

net.addLink(Switch2,  Switch3,    **linkopts )
net.addLink(Switch2,  Switch4,    **linkopts )
net.addLink(Switch2,  Switch5,    **linkopts )
net.addLink(Switch2,  Switch6,    **linkopts )

net.addLink(Switch3,  Switch5,    **linkopts )
net.addLink(Switch3,  Switch6,    **linkopts )

net.addLink(Switch4,  Switch5,    **linkopts )
net.addLink(Switch4,  Switch7,    **linkopts )
net.addLink(Switch4,  Switch8,    **linkopts )

net.addLink(Switch5,  Switch6,    **linkopts )
net.addLink(Switch5,  Switch7,    **linkopts )
net.addLink(Switch5,  Switch8,    **linkopts )
net.addLink(Switch5,  Switch9,    **linkopts )

net.addLink(Switch6,  Switch8,    **linkopts )
net.addLink(Switch6,  Switch9,    **linkopts )

net.addLink(Switch7,  Switch8,    **linkopts )

net.addLink(Switch8,  Switch9,    **linkopts )
net.addLink(Host2,   Switch9,    **linkopts )
net.addLink(Host3,   Switch7,    **linkopts )

 

# Start

net.addController('c', controller=RemoteController,ip='127.0.0.1')

net.build()

net.start()

 

# CLI

CLI( net )