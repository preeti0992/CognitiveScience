from flask import Flask,render_template, request,json
from pprint import pprint

#import rules as rs
import cogscimodel as csm
import experiments as exp

app = Flask(__name__)

model=csm.bayes_model()

@app.route('/')
def cogapp():
    return render_template('cogapp.html')

@app.route('/getProb', methods=['POST'])
def getProb():
    
    data=json.loads(request.get_data());
    
#    rs.check()
#    prob = rs.getProb(data['emotions'],data['situations']);
    
#    model=csm.bayes_model();
    variables = data['emotions']
    
#    pprint(variables)
    
    factors=data['situations'];
    evidence ={};
    for f in factors:
        evidence[f]=1
    
#    pprint(evidence)
    
    prob = model.query(variables,evidence);

    return json.dumps({'status':'OK','result':prob, 'error':0});

@app.route('/getExp', methods=['POST'])
def getExp():
    
    prob = exp.run_exp();
    return json.dumps({'status':'OK','result':prob, 'error':0});

if __name__=='__main__':
    app.run()