"""
HW1 EC 552 
PARTNER1: DELANEY DOW, PARTNER2: JAMES MAHER """
#import os 
import csv 
import math 
import pandas as pd 
import itertools 
from operator import itemgetter

# ============================================================================
# =============================== PARSER =====================================
# ============================================================================
#iterate through and send values to empty list 
def libParse(yMax, yMin, k, n, gateType, circuitElem, boolVal, file, circuitFile, library):      
    for rows in file: 
        #print(rows)
        library.append(rows)
        #libList = {str(rows['name']): str(rows['type']): float(rows['ymax']): float(rows['ymin']): float(rows['K']): float(rows['n']) }
        #library.append(libList)
        
        gateType_list = {str(rows['name']): str(rows['type'])}
        gateType.append(gateType_list)
        
        yMax_list = {str(rows['name']): float(rows['ymax'])}
        yMax.append(yMax_list)
        
        yMin_list = {str(rows['name']): float(rows['ymin'])} 
        yMin.append(yMin_list)
        
        k_list = {str(rows['name']): float(rows['k'])}
        k.append(k_list)
        
        n_list = {str(rows['name']): float(rows['n'])}
        n.append(n_list) 
    for rows in circuitFile: 
        promNameList = {str(rows['promName']): str(rows['gateName'])}
        circuitElem.append(promNameList)
        boolValList = {str(rows['promName']): str(rows['input'])}
        boolVal.append(boolValList)
        
# ============================================================================
# =============================== OPERATIONS =================================
# ============================================================================

def stretch(name, yMax, yMin): 
    #find particular gate and change the value 
    indexYMax = next(i for i,d in enumerate(yMax) if name in d) #stores value to change
    print("index is", indexYMax)
    yMaxNew = (yMax[indexYMax][name])*2
    yMax[indexYMax][name] = yMaxNew
    
#decrease slope in yMin by 0.3
    indexYMin = next(i for i,d in enumerate(yMin) if name in d) #stores value to index into
    yMinNew = (yMin[indexYMin][name]) * 0.3
    yMin[indexYMin][name] = yMinNew  
        
def increaseSlope(name, n):     
#b. INCREASE SLOPE BY INCREASING VALUE OF N 
    #find value to index into and then change 
    indexN = next(i for i,d in enumerate(n) if name in d)
    nNew =  (n[indexN][name]) * 2                   
    n[indexN][name] = nNew

def decreaseSlope(name, n):     
# c. DECREASE SLOPE BY DECREASING VALUE OF N
    indexN = next(i for i,d in enumerate(n) if name in d)
    nNew =  (n[indexN][name]) * 0.3                   
    n[indexN][name] = nNew
        
def strongPromoter(name, yMax, yMin):     
#d. STRONGER PROMOTER: INCREASE BOTH Y MIN AND Y MAX BY SAME FACTOR
    indexYMax = next(i for i,d in enumerate(yMax) if name in d)
    yMaxNew = (yMax[indexYMax][name]) * 2
    yMax[indexYMax][name] = yMaxNew

    indexYMin = next(i for i,d in enumerate(yMin) if name in d)
    yMinNew = (yMax[indexYMin][name]) * 2
    yMin[indexYMin][name] = yMinNew

def weakPromoter(name, yMax, yMin): 
#E. WEAKER PROMOTER: DECREASE BY SAME FACTOR    
    indexYMax = next(i for i,d in enumerate(yMax) if name in d)
    yMaxNew = (yMax[indexYMax][name]) * 0.3
    yMax[indexYMax][name] = yMaxNew

    indexYMin = next(i for i,d in enumerate(yMin) if name in d)
    yMinNew = (yMax[indexYMin][name]) * 0.3
    yMin[indexYMin][name] = yMinNew
    
def strongRBS (name, k): 
#F. STRONGER RBS: INCREASED K BY A FACTOR 
    indexK = next(i for i,d in enumerate(k) if name in d)
    kNew =  (k[indexK][name]) * 2                   
    k[indexK][name] = kNew

def weakRBS(name, k): 
#G. WEAKER RBS: DECREASED K BY A FACTOR      
    indexK = next(i for i,d in enumerate(k) if name in d)
    kNew =  (k[indexK][name]) * 0.3                   
    k[indexK][name] = kNew
      

#parse through file to get gate operations 
def gateOp(circuitFile, yMax, yMin, k, n): 
    #parse through file then run a switch statement 
    for row in circuitFile: 
        instruction = row['gateSpec']
        name = row['gateName']
        #switch statement to run all possible gate operations 
        if instruction == 'A':   
            stretch(name, yMax, yMin)
        elif instruction == 'B': 
            increaseSlope(name, n)
        elif instruction == 'C': 
            decreaseSlope(name, n)
        elif instruction == 'D': 
            strongPromoter(name, yMax, yMin)
        elif instruction == 'E': 
            weakPromoter(name, yMax, yMin)
        elif instruction == 'G': 
            strongRBS(name, k)
        elif instruction == 'H': 
            weakRBS(name, k)
        else: 
            print('No gate operations detected') 
            
 # ============================================================================
 # =============================== SCORING ====================================
 # ============================================================================           
#generate all possible permutations for gate scoring 
def circuitPerm(circuitElem, numElem): 
    #add in check for duplicates and if-else statements 
    perm_iterator = itertools.permutations(circuitElem, numElem)
    #outputs result of perm_iterator to be submitted for scoring 
    return perm_iterator
    
def calcScore(circuitPossibilities, circuitVal, boolVal, promName, circuitElem, yMax, yMin, truthBool): 
    fileName = open('circuitIn.csv', 'r') 
    file = csv.DictReader(fileName) 
    yMin = tuple(yMin)
    for row in file: 
        name = row['promName'] 
        promName.append(name)    
    for j in promName: 
        gate = [i[j] for i in circuitElem if j in i]
        gate = tuple(gate)
        gateVal = gate[0]   
        val = [i[j] for i in boolVal if j in i]
        inputVal = val[0]
        
        #extract gate name for appropriate promName
        for i, v in enumerate(inputVal):  
            if v == '0':#off state, get yMin value for gate
                #look for gate as a key into yMin
                indexGate = next(k for k,d in enumerate(yMin) if gateVal in d)
                #take value of key and store in truth table 
                zeroVal = (yMin[indexGate][gateVal])
                #print("z",zeroVal)
                #zeroValList = {([v]): ([zeroVal])}
                #truthBool.append(zeroValList)
            if v == '1' : #on state, get yMax value for gate 
                print("no")     

def responseFunction (input): 
    x = input
    return input 

def score(output):    
    if len(output) == 2: 
        score = math.log10(output[0]/output[1])    
        return score 
    else: 
        score = math.log10(output[0]/max(output[1:3]))
        return score

# ============================================================================
# =============================== MAIN =====================================
# ============================================================================

def main() :
    #upload gates library w/ file IO variables
    print('Please upload library') 
    fileName = open('gates.csv', 'r') 
    file = csv.DictReader(fileName) 
    
    circuitIn = 'circuitIn.csv' #CREATE CUSTOM INPUT FILE
    circuitIn = open(circuitIn, 'r') #don't need to error check this
    circuitFile = csv.DictReader(circuitIn) 
    
    numElem = len(pd.read_csv('circuitIn.csv')) #get # of gates
    
    #declare global variables 
    #create create dictionaries to access every value by name 
    yMax = [] #store yMax value from gates
    yMin = [] #store yMin value from gates
    k = [] #store k value from gates
    n = [] #store n value from gates
    gateType = [] #store gate type from gates
    circuitElem = [] #store circuit element names from circuitIn 
    boolVal = [] #stores bool val of each promoter input 
    promName = [] #stores promoter name
    circuitVal = [] #store nested list of circuit values 
    truthBool = [] #stores value of yMin and yMax from promoter input values for score calculating
    library = []
     

    libParse(yMax, yMin, k, n, gateType, circuitElem, boolVal, file, circuitFile, library)

        
   # 1. Find the gate # in the gate file, perform gate operations  
    gateOp(circuitFile, yMax, yMin, k, n)
    
    #2. generate all possible circuit combinations 
       #send to function that determines all permutations from list 
    circuitPossibilities = circuitPerm(circuitElem, numElem) 
    #print (type(circuitPossibilities))
    
    #submit circuitPossibilities for ordered scoring 
    calcScore(circuitPossibilities, circuitVal, boolVal, promName, circuitElem, yMax, yMin, truthBool)
    
    #display gate connection, truth table for input file 
    #calcScore(yMin, yMax, x, k, n)
    print("library", library)

    
if __name__ == '__main__':
  main()
    
