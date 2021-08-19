from flask import abort
import json
import config
config = config.config()
class dataOperator:
    def readJSON(self):
        with open(config.pathJSON, "r") as jsonFile:
            data = json.load(jsonFile)
            return data

    def writeJSON(self,field,value):
        with open(config.pathJSON, "r+") as jsonFile:
            data = json.load(jsonFile)
            data[field] = value
            jsonFile.seek(0)
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def appendJSON(self,reponseBody):
        if(reponseBody is None):
            abort(400,"The body cannot be null")
        with open(config.pathJSON, "r+") as jsonFile:
            data = json.load(jsonFile)
            if(reponseBody["field"] in data and "value" in reponseBody.keys()):
                data[reponseBody["field"]].append(reponseBody["value"])
            else:
                abort(400,"The field does not exist in the JSON file")
            jsonFile.seek(0)
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def deleteFieldJSON(self, reponseBody):
        if("field" not in reponseBody.keys()):
            abort(400,"The value of parameter field cannot be null")
        with open(config.pathJSON, "r+") as jsonFile:
            data = json.load(jsonFile)
            if(reponseBody["field"] in data):
                del data[reponseBody["field"]]
            else:
                abort(400,"The field does not exist in the JSON file")
            jsonFile.seek(0)
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def addFieldJSON(self,reponseBody):
        if(reponseBody is None):
            abort(400,"The body cannot be null")
        if("field" not in reponseBody.keys()):
            abort(400,"The value of parameter field cannot be null")
        if("value" not in reponseBody.keys()):
            value = ""
        else:
            value = reponseBody["value"]
        with open(config.pathJSON, "r+") as jsonFile:
            data = json.load(jsonFile)
            data[reponseBody["field"]] = value
            jsonFile.seek(0)
            json.dump(data, jsonFile)
            jsonFile.truncate()

    def showField(self, field):
        data = self.readJSON()
        if(field in data.keys()):
            return data[field]
        else:
            return "Field no created"

    def validateField(self, field):
        data = self.readJSON()
        if(field in data.keys()):
            return True
        else:
            return False

    def changeFieldValue(self,field,value,operation):
        if(not(self.validateField(field))):
            return "The field "+field+" was not created"
        if(value is None):
            abort(400,"The value of parameter value cannot be null")
        data = self.readJSON()
        if(operation == "addition"):
            self.writeJSON(field,int(data[field]) + int(value))
        elif(operation == "subtraction"):
            self.writeJSON(field,int(data[field]) - int(value))
        else:
            operation = "assign"
            self.writeJSON(field,value)
        oldValue = str(data[field])
        dataUpdated = self.readJSON()
        newValue = str(dataUpdated[field])
        return operation+" in "+field+" old: "+oldValue+" new: "+newValue
