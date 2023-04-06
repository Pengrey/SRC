![[firewall.png]]

---

# Config
```
configure
set system host-name FW2  
set interfaces ethernet eth0 address 10.2.4.14/24  
set interfaces ethernet eth1 address 10.2.3.14/24  
set interfaces ethernet eth2 address 10.1.2.14/24  
set interfaces ethernet eth3 address 10.1.3.14/24  
set protocols static route 0.0.0.0/0 next-hop 10.2.4.15
set protocols static route 10.2.2.0/24 next-hop 10.1.3.12  
commit  
save
exit
```