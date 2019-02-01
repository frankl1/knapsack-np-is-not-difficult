# Knapsack problem

Given a set of objects and a sack of limited capacity, how to fill the sack while maximizing the sum of values of the objects in the sack

## Usage

python knapsack.py [Input_file]

## Input file format

The file line contains two integers *N* and *B* separated by a space. *N* is the number of objects and *B* is capacity of the sack. This line is followed by *N* lines (objects) of two integers separated by a space and where the first integer is the utility of the object and the second one is the weight of the object.    

N B 

u1 w1

u2 w2

...

wN wN

## Output

The sum of values of the objects in the sack, the sum of weight of the objects in the sack, the number of objects in the sack and the indices of objects in the sack

## Example

python knapsack.py data/ks_10000_0.txt  
Utility: 1099870  
Weight: 1000000  
Number of objects: 18  
Sack: 3004 569 7056 3024 8035 9757 1825 7578 2169 2947 5621 7235 49 6536 9309 1943 9118 6114 