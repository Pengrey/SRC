![[firewall.png]]

---

# Config
```
configure
set system host-name FW2
# Set interfaces
set interfaces ethernet eth0 address 250.4.4.40/24
set interfaces ethernet eth1 address 250.3.3.30/24  
set interfaces ethernet eth2 address 250.2.2.30/24
set interfaces ethernet eth3 address 250.1.1.40/24

# Static Routes
set protocols static route 10.2.2.0/24 next-hop 10.3.3.30
set protocols static route 10.2.2.0/24 next-hop 10.4.4.40
set protocols static route 0.0.0.0/24 next-hop 200.4.4.40
set protocols static route 0.0.0.0/24 next-hop 200.3.3.30

# nat/pat
set nat source rule 10 outbound-interface eth0
set nat source rule 10 source address 10.0.0.0/8  
set nat source rule 10 translation address 192.1.0.1-192.1.0.10
set nat source rule 11 outbound-interface eth1
set nat source rule 11 source address 10.0.0.0/8  
set nat source rule 11 translation address 192.1.0.1-192.1.0.10

commit  
save
exit
```