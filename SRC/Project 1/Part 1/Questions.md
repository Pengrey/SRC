>[!NOTE] Explain why the synchronization of the load-balancers allows the nonexistence of firewall synchronization.
>In this scenario, the firewalls are not directly involved in load balancing or VRRP failover. The load balancing and failover is managed by the two load balancers LB1A and LB1B, which are configured to synchronize the connection state information between them using the conntrack-sync mechanism.
>
>Since both LB1A and LB1B are in the same VRRP group and are members of the same sync-group, they are aware of the state of connections handled by each other. When a failover occurs, the new active load balancer can continue handling the existing connections without dropping them.
>
>The firewalls, on the other hand, are not involved in connection tracking or load balancing, and they do not need to synchronize their state with the load balancers. They simply need to have their default gateway set to the IP address of the active load balancer in the VRRP cluster so that they can forward traffic to the load balancer.

>[!NOTE] Which load balancing algorithm may also allow the nonexistence of load-balancers synchronization
>
>The load balancing algorithm that may also allow the nonexistence of load-balancers synchronization is "consistent hashing".
>
>In consistent hashing, a hash function is used to map a resource or request to a server. Each server is assigned a range of hash values, and when a request is received, the hash function is used to determine which server the request should be sent to.
>
>Since each server is responsible for a specific range of hash values, adding or removing a server from the system only affects the requests that are mapped to that server's range, and not the entire system. This means that consistent hashing allows for the non-existence of load-balancer synchronization, as each server can independently determine which requests it should handle.

>[!NOTE] Explain why device/connection states synchronization may be detrimental during a DDoS attack.
>
>During a Distributed Denial of Service (DDoS) attack, the attacker aims to overwhelm a target network or device with a flood of traffic, making it unreachable or unusable. In response, network administrators may employ various mitigation techniques to filter out the malicious traffic and keep the network functioning.
>
>One such technique is to distribute the traffic across multiple servers or devices using load balancing, so that no single device becomes overwhelmed. However, if the load balancers are synchronizing their device/connection states, this can create a problem during a DDoS attack.
>
>If the load balancers are synchronized, then when one load balancer detects a flood of traffic, it will direct traffic away from the affected device to another device. However, since all the load balancers are synchronized, they will all direct traffic away from the affected device, leaving only a single device to handle all the traffic. This can cause the overwhelmed device to crash or become unusable, defeating the purpose of load balancing.
>
>Therefore, it is often better to have independent load balancers that do not synchronize their device/connection states during a DDoS attack. This allows each load balancer to make its own decisions about where to direct traffic, based on its own view of the network and the devices that it is managing. This approach helps to ensure that the network remains available and functional during a DDoS attack.