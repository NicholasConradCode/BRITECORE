from flask import Flask, render_template, request, redirect, url_for
import os
import json

class Risk:
    def __init__(self,name,data):
        self.name = name
        self.data = data
        self.saveRisk()
    
    def saveRisk(self):
        #if we already have the RISK in our database
        #then we can skip this
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/"+self.name+".json")
        riskExists = os.path.isfile(path)
        if(riskExists == False):
            print("Creating risk data")
            #Create a JSON file to save the Risk data
            newfile = open(path, "w")
            data = {};
            data['riskName'] = self.name
            data['data'] = self.data
            json.dump(data, newfile)
            newfile.close()
        
        
    
        
        

def loadRisk(riskName):
    path =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/"+riskName+".json")
    if os.path.isfile(path):
        with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
            return Risk(data['riskName'],data['data'])
    return None
    
def getRiskFormContent(risk):
    
    content = risk.name + "<br><br><form action='ThankYou'>"
    for x in risk.data:
        if x[1] == "enum":
            content+= x[0] + " <select>"
            for o in x[2]:
                content += "<option>"+o+"</option>"
            content+="</select><br>"
        else:
            content+= x[0] + " <input placeholder='Type: "+x[1]+"' type='"+x[1]+"'/><br>"
    content +="<br><input type='submit'/></form>"
    return content

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    if request.method == "POST":
        data = []
        for x in range(len(request.form.getlist('fieldNames'))):
            
            #Make sure field name value is not empty
            if request.form.getlist('fieldNames')[x] != "":
                #if fieldtype is enum, make sure that there are at least two options
                if request.form.getlist('fieldTypes')[x] == "enum":
                    if len(request.form.getlist('enumOpts')[x].split(',')) > 1:
                        data.append((request.form.getlist('fieldNames')[x],request.form.getlist('fieldTypes')[x],request.form.getlist('enumOpts')[x].split(',')))
                else:
                    data.append((request.form.getlist('fieldNames')[x],request.form.getlist('fieldTypes')[x],request.form.getlist('enumOpts')[x]))             
        #We would also validate the Risk Name depending on your specifications
        riskName = request.form.get('riskName')
        risk = Risk(riskName,data)
        return render_template('viewRiskForm.html',title=risk.name,content=getRiskFormContent(risk))
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def viewExistingRisk():
    risk = loadRisk(request.args.get('riskName'))
    if risk == None:
        return redirect(url_for('main'))
    return render_template('viewRiskForm.html',title=risk.name,content=getRiskFormContent(risk))

@app.route('/ThankYou')
def submitData():
    return render_template('viewRiskForm.html',title="Thank You",content="Thank you for taking the time to review my application. I enjoyed the process!")

if __name__ == '__main__':
    app.run(debug=True)