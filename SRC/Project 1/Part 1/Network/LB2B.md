![[load_balancer.png]]

---

# Config
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