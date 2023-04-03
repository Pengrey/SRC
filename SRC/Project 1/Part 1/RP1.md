![[repeater.png]]

---

# Config
```
conf t
int f0/0
ip addr 10.1.1.10 255.255.255.0
int f0/1
ip addr 10.2.2.10 255.255.255.0
no shut

ip route 0.0.0.0 0.0.0.0 10.1.1.1

end
write
```