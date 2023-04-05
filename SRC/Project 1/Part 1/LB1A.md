![[load_balancer.png]]

---

# Config
```
configure
set system host-name LB1A
# Set interfaces
set interfaces ethernet eth0 address 10.3.3.10/24  
set interfaces ethernet eth1 address 10.3.3.20/24  
set interfaces ethernet eth2 address 10.3.3.30/24
set interfaces ethernet eth3 address 10.3.3.40/24

# Static Routes
set protocols static route 10.2.2.0/24 next-hop 10.1.1.10
set protocols static route 0.0.0.0/24 next-hop 100.1.1.40
set protocols static route 0.0.0.0/24 next-hop 250.2.2.30

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
set load-balancing wan interface-health eth2 nexthop 10.3.3.30 
set load-balancing wan interface-health eth3 nexthop 100.1.1.40
set load-balancing wan rule 1 inbound-interface eth0
set load-balancing wan rule 1 interface eth2 weight 1
set load-balancing wan rule 1 interface eth3 weight 1
set load-balancing wan rule 2 inbound-interface eth1
set load-balancing wan rule 2 interface eth2 weight 1
set load-balancing wan rule 2 interface eth3 weight 1
set load-balancing wan sticky-connections inbound  
set load-balancing wan disable-source-nat

commit
save
exit
```