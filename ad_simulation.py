#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 18:47:16 2019

@author: firashofa
"""

import simpy
import random 

#print ('ad1 had %s audience, ad2 had %s audience, ad3 had %s audience' % (num_audience_ad1,num_audience_ad2,num_audience_ad3))

def ad_simulation(env, ad_picked):
    global num_audience_ad1
    global num_audience_ad2
    global num_audience_ad3
    global times_watched_ad1
    global times_watched_ad2
    global times_watched_ad3
    if ad_picked == ad1:
        with ad1.request() as req:
            yield req
            times_watched_ad1.append(env.now)
            num_audience_ad1 += 1
            yield env.timeout(10)
    elif ad_picked == ad2:
        with ad2.request() as req:
            yield req
            times_watched_ad2.append(env.now)
            num_audience_ad2 += 1
            yield env.timeout(15)
    elif ad_picked == ad3:
        with ad3.request() as req:
            yield req
            times_watched_ad3.append(env.now)
            num_audience_ad3 += 1
            yield env.timeout(20)
         
def pick_ad(env, ad):
    ad_picked = random.choice(ad)
    return ad_picked
    
def audience_arrival(env):
    while True:
        yield env.timeout(random.expovariate(1/3))
        env.process(ad_simulation(env, pick_ad(env, ad)))
    
env = simpy.Environment()
ad1 = simpy.Resource(env, 1)
ad2 = simpy.Resource(env, 1)
ad3 = simpy.Resource(env, 1)
ad = [ad1, ad2, ad3]
num_audience_ad1 = 0
num_audience_ad2 = 0
num_audience_ad3 = 0
times_watched_ad1 =[]
times_watched_ad2 =[]
times_watched_ad3 =[]
#<Process(car) object at 0x...>
env.process(audience_arrival(env))
env.run(until=120)

avg_ad1=0
total_distance_ad1 = 0
for i in range(len(times_watched_ad1)):
    if(i+1 < len(times_watched_ad1)):
        total_distance_ad1 += (times_watched_ad1[i+1]-times_watched_ad1[i])
        #avg=sum(avg_ad1)/len(avg(ad1))
    avg_ad1 = total_distance_ad1/(len(times_watched_ad1)-1)
avg_ad2=0
total_distance_ad2 = 0
for i in range(len(times_watched_ad2)):
    if(i+1 < len(times_watched_ad2)):
        total_distance_ad2 += (times_watched_ad2[i+1]-times_watched_ad2[i])
        #avg=sum(avg_ad1)/len(avg(ad1))
    avg_ad2 = total_distance_ad2/(len(times_watched_ad2)-1)
avg_ad3=0
total_distance_ad3 = 0
for i in range(len(times_watched_ad3)):
    if(i+1 < len(times_watched_ad3)):
        total_distance_ad3 += (times_watched_ad3[i+1]-times_watched_ad3[i])
        #avg=sum(avg_ad1)/len(avg(ad1))
    avg_ad3 = total_distance_ad3/(len(times_watched_ad3)-1)

print('ad1 has length 10s and average time interval between each audience member is:', avg_ad1)
print('ad2 has length 15s and average time interval between each audience member is:', avg_ad2)
print('ad3 has length 20s and average time interval between each audience member is:', avg_ad3)
print('Total audience for ad 1:', num_audience_ad1)
print('Times watched for ad 1:', times_watched_ad1)
print('Total audience for ad 2:', num_audience_ad2)
print('Times watched for ad 2:', times_watched_ad2)
print('Total audience for ad 3:', num_audience_ad3)
print('Times watched for ad 3:', times_watched_ad3)
