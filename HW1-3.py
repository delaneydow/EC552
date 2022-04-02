"""
HW1 EC 552 
PARTNER1: DELANEY DOW, PARTNER2: JAMES MAHER 
"""
#import os 
import csv 
import math 
import pandas as pd 
import itertools 

# ============================================================================
# =============================== PARSER =====================================
# ============================================================================
#iterate through and send values to empty list 
def libParse(circuitElem, boolVal, file, circuitFile, library):      
    for rows in file: 
        library.append(rows)

    for rows in circuitFile: 
        promNameList = {str(rows['promName']): str(rows['gateName'])}
        circuitElem.append(promNameList)
        boolValList = {str(rows['promName']): str(rows['input'])}
        boolVal.append(boolValList)
        
# ============================================================================
# =============================== OPERATIONS =================================
# ============================================================================
    
def stretch(name, nameIdx, library): 
    #find particular gate and change the value 
    yMax = library[nameIdx]['ymax']
    yMaxNew = float(yMax) * 2 
    
    #update library with new yMax value 
    for d in library: 
        d.update((k, yMaxNew) for k,v in d.items() if v == yMax)
    
    
    yMin = library[nameIdx]['ymin']
    yMinNew = float(yMin) * 0.3
    
    for d in library: 
        d.update((k, yMinNew) for k,v in d.items() if v == yMin) 
        
def increaseSlope(name, nameIdx, library):     
#b. INCREASE SLOPE BY INCREASING VALUE OF N 
    #find value to index into and then change 
    n = library[nameIdx]['n']
    nNew = float(n) *2 
    
    for d in library: 
        d.update((k, nNew) for k,v in d.items() if v == n)

def decreaseSlope(name, nameIdx, library):     
# c. DECREASE SLOPE BY DECREASING VALUE OF N
     n = library[nameIdx]['n']
     nNew = float(n) *0.3 
     
     for d in library: 
         d.update((k, nNew) for k,v in d.items() if v == n)
    
        
def strongPromoter(name, nameIdx, library):     
#d. STRONGER PROMOTER: INCREASE BOTH Y MIN AND Y MAX BY SAME FACTOR
     yMax = library[nameIdx]['ymax']
     yMaxNew = float(yMax) *2 
     
     for d in library: 
         d.update((k, yMaxNew) for k,v in d.items() if v == yMax)
      
     yMin = library[nameIdx]['ymin']
     yMinNew = float(yMin) *2 
      
     for d in library: 
          d.update((k, yMinNew) for k,v in d.items() if v == yMin)    
    

def weakPromoter(name, nameIdx, library): 
#E. WEAKER PROMOTER: DECREASE BY SAME FACTOR   
    yMax = library[nameIdx]['ymax']
    yMaxNew = float(yMax) *0.3 

    for d in library: 
        d.update((k, yMaxNew) for k,v in d.items() if v == yMax)
 
    yMin = library[nameIdx]['ymin']
    yMinNew = float(yMin) *0.3 
 
    for d in library: 
        d.update((k, yMinNew) for k,v in d.items() if v == yMin)   

    
def strongRBS (name, nameIdx, library): 
#F. STRONGER RBS: INCREASED K BY A FACTOR 
    k = library[nameIdx]['k']
    kNew = float(k) * 2
    
    for d in library: 
        d.update((x, kNew) for x,v in d.items() if v == k)
        
def weakRBS(name, nameIdx, library): 
#G. WEAKER RBS: DECREASED K BY A FACTOR   
    k = library[nameIdx]['k']
    kNew = float(k) * 0.3
    
    for d in library: 
        d.update((x, kNew) for x,v in d.items() if v == k)   
    
#parse through file to get gate operations 
def gateOp(circuitFile, library): 
    fileName = open('circuitIn.csv', 'r') 
    file = csv.DictReader(fileName) 
    #parse through file then run a switch statement 
    for row in file: 
        instruction = row['gateSpec']
        name = row['gateName']
        nameIdx = next((index for (index, d) in enumerate(library) if d['name'] == name), None)
        
        #switch statement to run all possible gate operations 
        if instruction == 'A': 
            print("stretching gate ", name)
            stretch(name, nameIdx, library)
        elif instruction == 'B': 
            print("increasing slope for gate", name)
            increaseSlope(name, nameIdx, library)
        elif instruction == 'C': 
            print("decrease slope for gate ", name)
            decreaseSlope(name, nameIdx, library)
        elif instruction == 'D': 
            print("strenthening promoter for ", name)
            strongPromoter(name, nameIdx, library)
        elif instruction == 'E': 
            print("weakening proter for ", name)
            weakPromoter(name, nameIdx, library)
        elif instruction == 'G': 
            print("stronger RBS for ", name)
            strongRBS(name, nameIdx, library)
        elif instruction == 'H': 
            print("weaker RBS for ", name)
            weakRBS(name, nameIdx,library)
        else: 
            print('No gate operations detected') 
 # ============================================================================
 # ======================== CIRCUIT CONSTRUCTION ==============================
 # ============================================================================  
    
 #generate all possible permutations for gate scoring 
def circuitPerm(circuitElem, numElem): 
     #add in check for duplicates and if-else statements 
     perm_iterator = itertools.permutations(circuitElem, numElem)
     #outputs result of perm_iterator to be submitted for scoring 
     "circuit permutations created and sending to the circuit Constructor"
     circuitConstruct(perm_iterator)
     return perm_iterator

def circuitConstruct(perm_iterator): 
     return perm_iterator

def notGate(circuitElem, boolVal): #TRANSFORM BOOL INPUTS AND UPDATE
    for j in circuitElem: 
        gate = list(j.values())[0]
        prom = list(j.keys())[0]
        #find gate in library then index into input 
        
        for k in boolVal: 
            if prom in k: 
                inVal1 = k[prom]
                for i, v in enumerate(inVal1):
                    if v == '0': 
                        v = '1'
                        #update v in input 
                        inVal1[i] = v
                        

def norGate(circuitElem, boolVal): #TRANSFORM BOOL INPUTS AND UPDATE
     for j in circuitElem: 
        gate = list(j.values())[0]
        prom = list(j.keys())[0]
        
        #for k in boolVal: 
            #if prom in k: 
                #inVal1 = k[prom]
                #for i, v in enumerate(inVal1): 
                    #print(v)
                        
        
def calcScore(circuitPossibilities, boolVal, promName, circuitElem, truthBool, library): 
    fileName = open('circuitIn.csv', 'r') 
    file = csv.DictReader(fileName) 
    boolDict = {}
    scoreTbl = []
    #append final score to each circuitPossibility 
    circs = list(circuitPossibilities)
    for row in file: 
        name = row['promName'] 
        promName.append(name)    
    for j in promName: 
        gate = [i[j] for i in circuitElem if j in i]
        gateVal = gate[0]  
        val = [i[j] for i in boolVal if j in i]
        inputVal = val[0]
        
       #extract gate name for appropriate promName
        for i, v in enumerate(inputVal):     
            if v == '0':#off state, get yMin value for gate 
                idx = 0
                #look for gate as a key into yMin
                for j in library: 
                    
                    if gateVal in j.values(): #locates gateName in library 
                        minIdx = library[idx]['ymin'] #extract ymin val for gate 
                        boolDict = {gateVal : {v : minIdx}}
                        truthBool.append(boolDict)
                        
                        #send to response function for scoring 
                        maxIdx = library[idx]['ymax']
                        x = minIdx
                        k = library[idx]['k']
                        n = library[idx]['n']
                        
                        score = responseFunc(float(minIdx), float(maxIdx), float(x), float(k), float(n)) #gt score for input
                        #append score
                        add = {'gateVal': gateVal, 'bool': v , 'score': score}
                        scoreTbl.append(add)
                    idx = idx +1    
            if v == '1' : #on state, get yMax value for gate 
                idx = 0
                for j in library:      
                    if gateVal in j.values(): 
               
                        maxIdx = library[idx]['ymax'] #extract ymax val for gate
                        boolDict = {gateVal: {v: maxIdx}}
                        truthBool.append(boolDict)  
                        
                        #send to response function for scoring 
                        minIdx = library[idx]['ymin']
                        x = minIdx
                        k = library[idx]['k']
                        n = library[idx]['n']
                        score = responseFunc(float(minIdx), float(maxIdx), float(x), float(k), float(n)) #gt score for input
                        #append value of score 
                        add = {'gateVal': gateVal, 'bool': v , 'score': score}
                        scoreTbl.append(add)
                    idx = idx + 1   
    return scoreTbl
      
         
def responseFunc (ymin, ymax, x, k, n): 
    z = ymin + (ymax  - ymin)/(1+pow((x/k), n)) 
    return z

#calculates best score --- have to fix 
def scoreCirc(scoreTbl, circs): 
    idx = 0
    max0 = -500
    min1 = 500 
    for j in circs: 
        dic = j[-1]
        first = list(dic.values())[0] #gets value of final output gate
        
        
    #extract all score values for each input 
    #from score Table 
        for i in scoreTbl: 
            gate = (i['gateVal'])
            boolVal = (i['bool'])
            if (gate == first) and (int(boolVal) == 0):
                minCurr = (i['score'])
                if (minCurr > max0): 
                    max0 = minCurr    
            if (gate == first) and (int(boolVal) == 1): 
                maxCurr = (i['score'])
                if (maxCurr < min1): 
                    min1 = maxCurr  
                    
        idx = idx + 1 

    score = -(math.log10((min1/max0)))
    return score
    
# ============================================================================
# ============================= FORMATTING ===================================
# ============================================================================ 
    
def printSpace(): 
    print()
    print()   
    
def printCircuitCombos(circs): 
    print("the possible circuit combinations are as follows:")
    print(circs)    

# ============================================================================
# =============================== MAIN =======================================
# ============================================================================

def main() :
    #upload gates library w/ file IO variables
    
    fileName = open('gates.csv', 'r') 
    file = csv.DictReader(fileName) 
    print("Gates file has been opened") 
    
    circuitIn = 'circuitIn.csv' #CREATE CUSTOM INPUT FILE
    circuitIn = open(circuitIn, 'r') #don't need to error check this
    circuitFile = csv.DictReader(circuitIn) 
    print("Circuit specification file has been opened")
    
    numElem = len(pd.read_csv('circuitIn.csv')) #get # of gates
    
    #declare global variables 
    #create create dictionaries to access every value by name 
    circuitElem = [] #store circuit element names from circuitIn 
    boolVal = [] #stores bool val of each promoter input 
    promName = [] #stores promoter name
    
    truthBool = [] #stores value of yMin and yMax from promoter input values for score calculating
    library = []
    
    libParse(circuitElem, boolVal, file, circuitFile, library)
    print("the circuit and gate files have been sucessfully parsed")
    printSpace() 
    print("the gate library is below:")
    print(library)
    printSpace()
    

        
   # Find the gate # in the gate file, perform gate operations  
    print("now applying gate operations...")
    gateOp(circuitFile, library)
    printSpace()
    print("the library after performing the gate operatios is :")
    print(library)
    printSpace()
    
    # generate all possible circuit combinations 
       #send to function that determines all permutations from list 
    print("now generating possible circuit combinations...")    
    circuitPossibilities = circuitPerm(circuitElem, numElem)  
    circs = list(circuitPossibilities) 
    printCircuitCombos(circs)
    
    
    printSpace()
    print("now submitting these circuits for scoring...") 
    
    #submit circuitPossibilities for ordered scoring 
    scoreTbl = calcScore(circuitPossibilities, boolVal, promName, circuitElem, truthBool, library)
    #print(scoreTbl)
    
    score = scoreCirc(scoreTbl, circs)
    print("The best circuit score is:") 
    print(score)
    
    
if __name__ == '__main__':
  main()
    
