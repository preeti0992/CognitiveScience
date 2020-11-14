#!/usr/bin/env python
# coding: utf-8



# coding: utf-8

# In[1]:

import pgmpy
from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


# In[2]:

class bayes_model:
    
    def __init__(self):
        
        # In[3]:        
        
        # set up network object
        networkA = BayesianModel()
        
        
        # In[4]:
        
        # Add nodes
        networkA.add_node('psychological')
        networkA.add_node('trauma')
        networkA.add_node('relationship')
        networkA.add_node('fear')
        networkA.add_node('anger')
        networkA.add_node('rage')
        networkA.add_node('desperation')
        networkA.add_node('murder')
        
        
        # In[5]:
        
        # Add edges
        networkA.add_edge('psychological', 'fear')
        networkA.add_edge('trauma', 'fear')
        networkA.add_edge('relationship', 'fear')
        networkA.add_edge('relationship', 'anger')
        networkA.add_edge('fear', 'anger')
        networkA.add_edge('fear', 'desperation')
        networkA.add_edge('fear', 'rage')
        networkA.add_edge('anger', 'rage')
        networkA.add_edge('relationship', 'rage')
        networkA.add_edge('psychological', 'rage')
        networkA.add_edge('anger', 'murder')
        networkA.add_edge('rage', 'murder')
        networkA.add_edge('desperation', 'murder')
        

        # In[6]:
        
        # add CPDs
        cpd_psy = TabularCPD('psychological', 2, values=[[0.8], [0.2]])
        cpd_trauma = TabularCPD('trauma', 2, values=[[0.7], [0.3]])
        cpd_relationship = TabularCPD('relationship', 2, values=[[0.567], [0.433]])
        cpd_fear = TabularCPD('fear', 2, values=[[0.683,0.921,0.864,0.966,0.757,0.939,0.896,0.974], [0.317,0.079,0.136,0.034, 0.243,0.061,0.104,0.026]], evidence=['relationship','trauma', 'psychological'], evidence_card=[2, 2,2])
        cpd_anger = TabularCPD('anger', 2, values=[[0.528,0.906,0.639, 0.928], [0.472, 0.094,0.361,0.072]], evidence=['relationship', 'fear'], evidence_card=[2, 2])
        cpd_desperation = TabularCPD('desperation', 2, values=[[0.833,0.167], [0.167, 0.833]], evidence=['fear'], evidence_card=[2])
        cpd_rage = TabularCPD('rage', 2, values=[[0.799,0.846,0.96,0.969,0.95,0.961,0.989,0.993,0.824,0.865,0.965,0.973,0.956,0.966,0.991,0.993], [0.201,0.154,0.04,0.031,0.05,0.039,0.01,0.008,0.176,0.135,0.035,0.027,0.044,0.034,0.009,0.007]], evidence=['anger', 'psychological','fear', 'relationship'], evidence_card=[2,2,2,2])
        cpd_murder = TabularCPD('murder', 2, values=[[0.842,0.862,0.82,0.842,0.909,0.920,0.896,0.909], [0.158,0.138,0.18,0.158,0.091,0.08,0.104,0.091]], evidence=['desperation', 'rage', 'anger'], evidence_card=[2,2,2])
        
        # Don't forget this step!
        networkA.add_cpds(cpd_psy, cpd_trauma, cpd_relationship, cpd_fear, cpd_anger, cpd_desperation, cpd_rage, cpd_murder)
                
        # Check to make sure it works
#        print(networkA.check_model())# In[6]:
        
        # Set up solver
        self.solver = VariableElimination(networkA)
        
        
        # In[7]:       
        
    def query(self, variables, evidence):
        
        # Query solver for conditional probability        
#        marginal_prob = self.solver.query(variables=['anger'], evidence={'murder': 1})
#        print("in query")
        prob_var={}
        for v in variables:
            marginal_prob = self.solver.query([v], evidence)
            prob = marginal_prob[v].values
#            print("Probability given murder occurred: {}".format(prob))
            prob_var[v]=round(prob[1],3)
#        print(prob_var)
        return prob_var
        
    
        # In[8]:




