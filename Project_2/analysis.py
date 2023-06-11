import pandas as pd
import numpy as np
import ipaddress
import dns.resolver
import dns.reversename
import pygeoip
import matplotlib.pyplot as plt 




datadir='data/'
datafile=datadir+'dataset0/data0.parquet'
data=pd.read_parquet(datafile)
print(data.columns)

# Analyze ports used
print("=====PORTS=====")
print("\n - outgoing\n")
port=data.groupby(['src_ip'])['port'].value_counts()
proto=data.groupby(['src_ip'])['proto']

# Define a treshold for the number of times a port is used

# get number of times each port is used

print(port.to_string())

print(port.describe(percentiles=[.05, .25, .5, .75, .95])   )  
print(proto.describe(percentiles=[.05, .25, .5, .75, .95])   )


# Analyze protocols used
print("=====PROTOCOLS=====")

# Analyze volume of traffic per IP

print("=====TRAFFIC=====")
downS=data.groupby(['src_ip'])['down_bytes']
upS=data.groupby(['src_ip'])['up_bytes']

downD=data.groupby(['dst_ip'])['down_bytes']
upD=data.groupby(['dst_ip'])['up_bytes']

# Analyze relation between source and destination IPs


# get number of times each port is used
print(downS.describe(percentiles=[.05, .25, .5, .75, .95])   )
print(upS.describe(percentiles=[.05, .25, .5, .75, .95])   )