from . import getEid
import time
import requests

apiKey = ""
headers = {'APIKey' : apiKey}
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"

def getAppWFSMeasure(enrollmentNumber, url):
    gWFSM = url + enrollmentWorkflowStep + "GetStepsByEnrollmentId?enrollmentId=" + str(getEid.getEid(enrollmentNumber, url))
    time.sleep(.01)
    presponse = requests.get(gWFSM, headers = headers)
    pr_jsn = presponse.json()
    rsp_jsn3 = len(pr_jsn['Data'])

    #NEW EDIT 3-28-2024
    rsp_jsn2 = pr_jsn['Data']
    for i in range(0, rsp_jsn3):
          #print(rsp_jsn2[i]['WorkflowStepName'])
        if(rsp_jsn2[i]['WorkflowStepName'] == 'Application'):
            return rsp_jsn2[i]