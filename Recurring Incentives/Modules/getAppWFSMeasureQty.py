from . import getAppWFSMeasure
import time
import json
import requests

apiKey = ""
headers = {'APIKey' : apiKey}
Measure = "Measure"
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"

def getAppWFSMeasureQty(enrollmentNumber, url):
    
    app = getAppWFSMeasure.getAppWFSMeasure(enrollmentNumber, url)
    time.sleep(.01)
    measureEndpoint = url + enrollmentWorkflowStep + str(app['EnrollmentWorkflowStepId']) + "/" + Measure
    response = requests.get(measureEndpoint, headers = headers)
    time.sleep(.01)
    #print(app['EnrollmentWorkflowStepId'])
    rsp_jsn = response.json()
    rsp_ln = len(rsp_jsn['Data'])
    #print("rsp_jsn", rsp_jsn)
    arr = ""
    #rsp_dmp = json.dumps(rsp_jsn['Data'])
    mqty = 0
    for item in range(0, rsp_ln):
        arr = rsp_jsn['Data'][item]
        if(arr['MeasureCode'] == 'PPT'):
            mqty +=arr['MeasureQty']
        elif(arr['MeasureCode'] == 'EVRI'):
            mqty +=arr['MeasureQty']
    
    #Wfs Properties
    #rsp_ld = json.loads(rsp_dmp)
    return int(mqty)
    #return(rsp_ld)