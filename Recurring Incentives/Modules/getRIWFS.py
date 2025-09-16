from . import getEid
import time
import requests

apiKey = ""
headers = {'APIKey' : apiKey}
stp_outcome = {"Outcome": "Work Complete"}
enrollment = "Enrollment/"
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"
Measure = 'Measure'

def getRIWFS(enrollmentNumbers, url):
    #start = time.time()
    endWFSs = url + enrollment + str(getEid.getEid(enrollmentNumbers, url)) + '/' + enrollmentWorkflowStep
    time.sleep(.01)
    response = requests.get(endWFSs, headers=headers)
    rsp_jsn = response.json()
    #NEW EDITS 3-19-2024
    #print(rsp_jsn['Data'])
    rsp_jsn2 = rsp_jsn['Data']
    rsp_jsn3 = len(rsp_jsn['Data'])
    #1st Edit
    for i in range(0, rsp_jsn3):
          #print(rsp_jsn2[i]['WorkflowStepName'])
        if(rsp_jsn2[i]['WorkflowStepName'] == 'Recurring Incentive' and rsp_jsn2[i]['WorkflowStepDisposition'] == 'Open'):
            return rsp_jsn2[i]