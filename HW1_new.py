#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HW1 EC 552 
PARTNER1: DELANEY DOW 
PARTNER2: JAMES MAHER 
"""
import os 
import csv 

#iterate through and send values to empty list 
def fileParse(yMax, yMin, k, n, file): 
    for col in file: 
        yMax.append(col['ymax']) 
        yMin.append(col['ymin']) 
        k.append(col['K']) 
        n.append(col['n'])
    
#printing lists    
#print('yMax:', yMax) 

#set directory variables 

# 2. APPLY FUNCTIONS TO LIBRARY 
# a. STRETCH OPERATION: INCREASE YMAX, DECREASE YMIN VALUES 

def stretch(yMax, yMin): 
    
#increase slope; iterate through yMax list 
    for i in yMax: 
        print('original value')
        print(i) 
        print('stretched value') 
        print (2*float(i)) 
        #save new value

#decrease slope in yMin
    for i in yMin: 
        print('original value') 
        print(i) 
        print('stretched value') 
        print (0.3*float(i))
        #save new value 
        
def increaseSlope(n):     
#b. INCREASE SLOPE BY INCREASING VALUE OF N 
    for i in n: 
        print ('original value') 
        print (i) 
        print ('increase slope value') 
        print (2*float(i)) 
        #save new value

def decreaseSlope(n):     
# c. DECREASE SLOPE BY DECREASING VALUE OF N
    for i in n: 
        print ('original value') 
        print (i) 
        print ('decreased slope value') 
        print (0.3 * float(i))  
        #save new value 
        
def strongPromoter(yMax, yMin):     
#d. STRONGER PROMOTER: INCREASE BOTH Y MIN AND Y MAX BY SAME FACTOR
    for i in yMax: 
        print (i) #original value 
        print (2*float(i)) #scaled valued 
        #save new value 

    for i in yMin: 
        print (i) #original value 
        print (2*float(i)) #scaled value  
        #save new value 

def weakPromoter(yMax, yMin): 
#E. WEAKER PROMOTER: DECREASE BY SAME FACTOR
    for i in yMax: 
        print (i) #original value
        print (0.3* float(i)) #scaled value 
        #save new value 

    for i in yMin: 
        print(i) 
        print(0.3*float(i)) #scaled value   
        #save new value 

#F. STRONGER RBS: INCREASED K BY A FACTOR

#G. WEAKER RBS: DECREASED K BY A FACTOR

#3. SPECIFY COLLECTION OF GATES, PERFORM SCORING, AND DETERMINE HIGH/LOW VALUES
 
#3. SPECIFY COLLECTION OF GATES 



""" DEFINE MAIN FUNCTION THAT CALLS ALL OTHER FUNCTIONS 
AT THE COMMAND OF THE USER, ETC. """ 

def main() :
    #upload gates library w/ file IO variables
    print('Please upload library') 
    fileName = open('gates.csv', 'r') 
    file = csv.DictReader(fileName) 
    fileName.close()

    #declare global variables 
    #create empty lists 
    yMax = []
    yMin = [] 
    k = [] 
    n = [] 
    
    fileParse(yMax, yMin, k, n, file)
    print('Select gate operations') 
    stretch(yMax, yMin) 
    increaseSlope(n) 
    decreaseSlope(n) 
    strongPromoter(yMax, yMin) 
    weakPromoter(yMax, yMin) 
     
    circuitIn = input('enter input file name') #CREATE CUSTOM INPUT FILE
    circuitIn = open(circuitIn, 'r') #don't need to error check this 
    print ('circuit input files opened successfully') 
    
    circuitOut = input('enter output file name') 
    circuitOut = open(circuitOut, 'r') 
    print ('circuit output file opened successfully')
    
    
    
    

    
if __name__ == '__main__':
  main()
    
