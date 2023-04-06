![[firewall.png]]

---

# Config
```
configure
set system host-name FW1  
set interfaces ethernet eth0 address 10.2.0.13/24  
set interfaces ethernet eth1 address 10.2.1.13/24  
set interfaces ethernet eth2 address 10.1.4.13/24  
set interfaces ethernet eth3 address 10.1.3.13/24
set protocols static route 0.0.0.0/0 next-hop 10.2.0.16
set protocols static route 10.2.2.0/24 next-hop 10.1.3.11  
commit  
save
exit
```