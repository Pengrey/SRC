>[!NOTE]
>RESET:
>```
>sudo cp /opt/vyatta/etc/config.boot.default /config/config.boot
>```


PC1 (Computer)
```
ip 10.2.2.100/24 10.2.2.10
write
```

PC2 (Computer)
```
ip 200.2.2.100/24 200.2.2.10
write
```

PC3 (Computer DMZ)
```
ip 192.1.1.100/24 192.1.1.110
write
```

R1 (Router)
```
conf t
int f0/0
ip addr 10.1.1.10 255.255.255.0
no shut
int f0/1
ip addr 10.2.2.10 255.255.255.0
no shut

ip route 0.0.0.0 0.0.0.0 10.1.1.11
ip route 192.1.1.0 255.255.255.0 10.1.1.11

end
write
```

R2 (Router)
```
conf t
int f0/0
ip addr 200.1.1.10 255.255.255.0
no shut
int f0/1
ip addr 200.2.2.10 255.255.255.0
no shut

ip route 192.1.0.0 255.255.254.0 200.1.1.15
ip route 192.1.1.0 255.255.255.0 200.1.1.15

end
write
```

LB1A (Load Balancer)
```
configure
set system host-name LB1A
set interfaces ethernet eth0 address 10.1.1.11/24  
set interfaces ethernet eth1 address 10.1.0.11/24  
set interfaces ethernet eth2 address 10.1.2.11/24  
set interfaces ethernet eth3 address 10.1.3.11/24  

set protocols static route 0.0.0.0/0 next-hop 10.1.3.13
set protocols static route 0.0.0.0/0 next-hop 10.1.2.14
set protocols static route 10.2.2.0/24 next-hop 10.1.1.10
set protocols static route 192.1.1.0/24 next-hop 10.1.1.13
set protocols static route 192.1.1.0/24 next-hop 10.1.1.14


# vrrp

set high-availability vrrp group LB1Cluster vrid 10  
set high-availability vrrp group LB1Cluster interface eth1
set high-availability vrrp group LB1Cluster virtual-address 192.168.100.1/24 
set high-availability vrrp sync-group LB1Cluster member LB1Cluster  
set high-availability vrrp group LB1Cluster rfc3768-compatibility


# conntrack sync

set service conntrack-sync accept-protocol 'tcp,udp,icmp'  
set service conntrack-sync failover-mechanism vrrp sync-group LB1Cluster  
set service conntrack-sync interface eth1  
set service conntrack-sync mcast-group 225.0.0.50  
set service conntrack-sync disable-external-cache


# load balancing

set load-balancing wan interface-health eth3 nexthop 10.1.3.13 
set load-balancing wan interface-health eth2 nexthop 10.1.2.14 
set load-balancing wan rule 1 inbound-interface eth0  
set load-balancing wan rule 1 interface eth3 weight 1  
set load-balancing wan rule 1 interface eth2 weight 1 
set load-balancing wan sticky-connections inbound  
set load-balancing wan disable-source-nat
commit  
save
exit
```

LB1B (Load Balancer)
```
configure
set system host-name LB1B
set interfaces ethernet eth0 address 10.1.1.12/24  
set interfaces ethernet eth1 address 10.1.0.12/24  
set interfaces ethernet eth2 address 10.1.4.12/24  
set interfaces ethernet eth3 address 10.1.3.12/24  
set protocols static route 0.0.0.0/0 next-hop 10.1.4.13
set protocols static route 0.0.0.0/0 next-hop 10.1.3.14
set protocols static route 10.2.2.0/24 next-hop 10.1.1.10
set protocols static route 192.1.1.0/24 next-hop 10.1.4.13
set protocols static route 192.1.1.0/24 next-hop 10.1.3.14

# vrrp

set high-availability vrrp group LB1Cluster vrid 10  
set high-availability vrrp group LB1Cluster interface eth1
set high-availability vrrp group LB1Cluster virtual-address 192.168.100.1/24 
set high-availability vrrp sync-group LB1Cluster member LB1Cluster  
set high-availability vrrp group LB1Cluster rfc3768-compatibility


# conntrack sinc

set service conntrack-sync accept-protocol 'tcp,udp,icmp'  
set service conntrack-sync failover-mechanism vrrp sync-group LB1Cluster  
set service conntrack-sync interface eth1  
set service conntrack-sync mcast-group 225.0.0.50  
set service conntrack-sync disable-external-cache


# load balancing

set load-balancing wan interface-health eth3 nexthop 10.1.3.14
set load-balancing wan interface-health eth2 nexthop 10.1.4.13 
set load-balancing wan rule 1 inbound-interface eth0  
set load-balancing wan rule 1 interface eth3 weight 1  
set load-balancing wan rule 1 interface eth2 weight 1 
set load-balancing wan sticky-connections inbound  
set load-balancing wan disable-source-nat
commit  
save
exit
```

LB2A (Load Balancer)
```
configure
set system host-name LB2A
set interfaces ethernet eth0 address 10.2.0.16/24  
set interfaces ethernet eth1 address 10.2.3.16/24  
set interfaces ethernet eth2 address 10.2.4.16/24  
set interfaces ethernet eth3 address 200.1.1.16/24
set protocols static route 10.2.2.0/24 next-hop 10.2.0.13
set protocols static route 10.2.2.0/24 next-hop 10.2.3.14
set protocols static route 0.0.0.0/0 next-hop 200.1.1.10  
set protocols static route 192.1.1.0/24 next-hop 10.2.0.13
set protocols static route 192.1.1.0/24 next-hop 10.2.3.14

#vrrp
set high-availability vrrp group LB2Cluster vrid 10  
set high-availability vrrp group LB2Cluster interface eth2
set high-availability vrrp group LB2Cluster virtual-address 192.168.100.1/24 
set high-availability vrrp sync-group LB2Cluster member LB2Cluster  
set high-availability vrrp group LB2Cluster rfc3768-compatibility

# conntrack sync
set service conntrack-sync accept-protocol 'tcp,udp,icmp'  
set service conntrack-sync failover-mechanism vrrp sync-group LB2Cluster  
set service conntrack-sync interface eth2  
set service conntrack-sync mcast-group 225.0.0.50  
set service conntrack-sync disable-external-cache

# load balancing


set load-balancing wan interface-health eth0 nexthop 10.2.0.13  
set load-balancing wan interface-health eth1 nexthop 10.2.3.14
set load-balancing wan rule 1 inbound-interface eth3  
set load-balancing wan rule 1 interface eth0 weight 1  
set load-balancing wan rule 1 interface eth1 weight 1 
set load-balancing wan sticky-connections inbound  
set load-balancing wan disable-source-nat

# Nat/pat

set nat source rule 10 outbound-interface eth3
set nat source rule 10 source address 10.0.0.0/8  
set nat source rule 10 translation address 192.1.0.1-192.1.0.10
commit  
save
exit
```

LB2B (Load Balancer)
```
configure
set system host-name LB2B
set interfaces ethernet eth0 address 10.2.4.15/24  
set interfaces ethernet eth1 address 10.2.1.15/24  
set interfaces ethernet eth2 address 10.2.4.15/24  
set interfaces ethernet eth3 address 200.1.1.15/24  

set protocols static route 0.0.0.0/0 next-hop 200.1.1.10
set protocols static route 10.2.2.0/24 next-hop 10.2.4.14
set protocols static route 10.2.2.0/24 next-hop 10.2.1.13

#vrrp

set high-availability vrrp group LB2Cluster vrid 10  
set high-availability vrrp group LB2Cluster interface eth2
set high-availability vrrp group LB2Cluster virtual-address 192.168.100.1/24 
set high-availability vrrp sync-group LB2Cluster member LB2Cluster  
set high-availability vrrp group LB2Cluster rfc3768-compatibility


# conntrack sync

set service conntrack-sync accept-protocol 'tcp,udp,icmp'  
set service conntrack-sync failover-mechanism vrrp sync-group LB2Cluster  
set service conntrack-sync interface eth2  
set service conntrack-sync mcast-group 225.0.0.50  
set service conntrack-sync disable-external-cache

# load balancing

set load-balancing wan interface-health eth0 nexthop 10.2.4.14
set load-balancing wan interface-health eth1 nexthop 10.2.1.13
set load-balancing wan rule 1 inbound-interface eth3  
set load-balancing wan rule 1 interface eth0 weight 1  
set load-balancing wan rule 1 interface eth1 weight 1 
set load-balancing wan sticky-connections inbound  
set load-balancing wan disable-source-nat


# Nat/pat
  
set nat source rule 10 outbound-interface eth3
set nat source rule 10 source address 10.0.0.0/8  
set nat source rule 10 translation address 100.64.0.10-100.64.0.20
commit  
save
exit
```

FW1 (Firewall)
```
configure
set system host-name FW1  
set interfaces ethernet eth0 address 10.2.0.13/24  
set interfaces ethernet eth1 address 10.2.1.13/24  
set interfaces ethernet eth2 address 10.1.4.13/24  
set interfaces ethernet eth3 address 10.1.3.13/24
set interfaces ethernet eth4 address 10.3.3.13/24
set protocols static route 0.0.0.0/0 next-hop 10.2.0.16
set protocols static route 10.2.2.0/24 next-hop 10.1.3.11

# Access Control Lists 
set firewall name InternalToDMZ default-action drop 
set firewall name InternalToDMZ rule 10 action accept 
set firewall name InternalToDMZ rule 10 protocol tcp 
set firewall name InternalToDMZ rule 10 destination address 192.1.1.0/24 
set firewall name InternalToDMZ rule 10 destination port 80,443 

set firewall name ExternalToDMZ default-action drop 
set firewall name ExternalToDMZ rule 20 action accept 
set firewall name ExternalToDMZ rule 20 protocol tcp 
set firewall name ExternalToDMZ rule 20 destination address 192.1.1.0/24 
set firewall name ExternalToDMZ rule 20 destination port 80,443

# Rate limiting 
set traffic-policy shaper RATE-LIMIT-10Mbps bandwidth 10mbit 
set traffic-policy shaper RATE-LIMIT-10Mbps default bandwidth 100% 

set interfaces ethernet eth4 traffic-policy out RATE-LIMIT-10Mbps
commit  
save
exit
```

FW2 (Firewall)
```
configure
set system host-name FW2  
set interfaces ethernet eth0 address 10.2.4.14/24  
set interfaces ethernet eth1 address 10.2.3.14/24  
set interfaces ethernet eth2 address 10.1.2.14/24  
set interfaces ethernet eth3 address 10.1.3.14/24  
set interfaces ethernet eth4 address 10.3.3.14/24
set protocols static route 0.0.0.0/0 next-hop 10.2.4.15
set protocols static route 10.2.2.0/24 next-hop 10.1.3.12 

# Access Control Lists 
set firewall name InternalToDMZ default-action drop 
set firewall name InternalToDMZ rule 10 action accept 
set firewall name InternalToDMZ rule 10 protocol tcp 
set firewall name InternalToDMZ rule 10 destination address 192.1.1.0/24 
set firewall name InternalToDMZ rule 10 destination port 80,443 
set firewall name ExternalToDMZ default-action drop 
set firewall name ExternalToDMZ rule 20 action accept 
set firewall name ExternalToDMZ rule 20 protocol tcp 
set firewall name ExternalToDMZ rule 20 destination

# Rate limiting 
set traffic-policy shaper RATE-LIMIT-10Mbps bandwidth 10mbit 
set traffic-policy shaper RATE-LIMIT-10Mbps default bandwidth 100% 

set interfaces ethernet eth4 traffic-policy out RATE-LIMIT-10Mbps
commit  
save
exit
```

## Possible fix para 10.2:
```bash
#!/bin/bash

# Define the path to the blocklist file and the firewall group name
BLOCKLIST_FILE="/path/to/blocklist.txt"
FIREWALL_GROUP_NAME="ddos_blocklist"

# Configure VyOS to apply the updated rules
sudo vtysh -c "configure terminal"

# Remove the existing firewall group, if it exists
sudo vtysh -c "delete firewall group address-group $FIREWALL_GROUP_NAME"

# Create a new firewall group and add the IP addresses from the blocklist file
while read -r ip; do
  sudo vtysh -c "set firewall group address-group $FIREWALL_GROUP_NAME address $ip"
done < "$BLOCKLIST_FILE"

# Commit and save the changes
sudo vtysh -c "commit"
sudo vtysh -c "save"
sudo vtysh -c "exit"
```

FW1:
```bash
configure
set firewall name outside-in rule 30 action drop
set firewall name outside-in rule 30 source group address-group ddos_blocklist
set interfaces ethernet eth4 firewall in name outside-in
commit
save
exit
```

FW2:
```bash
configure
set firewall name outside-in rule 10 action drop
set firewall name outside-in rule 10 source group address-group ddos_blocklist
set interfaces ethernet eth4 firewall in name outside-in
commit
save
exit
```