#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HW1 EC 552 
PARTNER1: DELANEY DOW 
PARTNER2: JAMES MAHER 
"""
import os 
import csv 

fileName = open('gates.csv', 'r') 
file = csv.DictReader(fileName) 

#create empty lists 
yMax = []
yMin = [] 
k = [] 
n = [] 

#iterate through and send values to empty list 
for col in file: 
    yMax.append(col['ymax']) 
    yMin.append(col['ymin']) 
    k.append(col['K']) 
    n.append(col['n'])
    
#printing lists    
print('yMax:', yMax) 

#set directory variables 

""" 2. APPLY FUNCTIONS TO LIBRARY """
""" a. STRETCH OPERATION: INCREASE YMAX, DECREASE YMIN VALUES """
    
#increase slope; iterate through yMax list 
for i in yMax: 
    print('original value')
    print(i) 
    print('stretched value') 
    print (2*float(i)) 

#decrease slope
for i in yMin: 
    print('original value') 
    print(i) 
    print('stretched value') 
    print (0.3*float(i))
    
"""b. INCREASE SLOPE BY INCREASING VALUE OF N """
for i in n: 
    print ('original value') 
    print (i) 
    print ('increase slope value') 
    print (2*float(i)) 
    
""" c. DECREASE SLOPE BY DECREASING VALUE OF N"""
for i in n: 
    print ('original value') 
    print (i) 
    print ('decreased slope value') 
    print (0.3 * float(i))   
    
"""d. STRONGER PROMOTER: INCREASE BOTH Y MIN AND Y MAX BY SAME FACTOR"""
for i in yMax: 
    print (i) #original value 
    print (2*float(i)) #scaled valued 

for i in yMin: 
    print (i) #original value 
    print (2*float(i)) #scaled value     

""" E. WEAKER PROMOTER: DECREASE BY SAME FACTOR""" 
for i in yMax: 
    print (i) #original value
    print (0.3* float(i)) #scaled value 

for i in yMin: 
    print(i) 
    print(0.3*float(i)) #scaled value     

"""F. STRONGER RBS: INCREASED K BY A FACTOR"""

"""G. WEAKER RBS: DECREASED K BY A FACTOR"""

"""3. SPECIFY COLLECTION OF GATES, PERFORM SCORING, AND 
DETERMINE HIGH/LOW VALUES"""
 
#3. SPECIFY COLLECTION OF GATES 





#4. 
