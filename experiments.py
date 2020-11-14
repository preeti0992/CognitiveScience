from flask import Flask,render_template, request,json

import numpy as np
from itertools import combinations 
import cogscimodel as csm


# In[1]:

def run_exp():

    emotions = ['rage', 'anger', 'desperation', 'fear']
    sit = ['psychological', 'trauma', 'relationship']

    model=csm.bayes_model()
  
    prob_results=[]
    
    for i in range(4):
        comb=combinations(emotions, i+1)
        for el in list(comb):
#            print("--")
#            print(np.asarray(el))
            variables=np.asarray(el)
#            for e in el:
#                print(e,"-")
            for j in range(3):
                sitcomb=combinations(sit, j+1)
                for sl in list(sitcomb):
#                        print(sl)
#                    print(np.asarray(sl))
                    factors=np.asarray(sl)
                    evidence ={};
                    for f in factors:
                        evidence[f]=1
#                    print('variables','evidence')
#                    print(variables,evidence)
                    print(variables)
                    print(factors)
                    prob =model.query(variables,evidence)
                    print(prob)
                    prob_results.append(prob)
    
#    print('prob_results')
#    print(prob_results)
    return prob_results


# In[2]:

if __name__=='__main__':
    print(run_exp())
                        

# In[3]: