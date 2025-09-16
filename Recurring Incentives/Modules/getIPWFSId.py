from . import getEid
import time
import requests

apiKey = ""
headers = {'APIKey' : apiKey}
enrollment = "Enrollment/"
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"

def getIPWFSId(enrollmentNumber, url):
    endpointWFS = url + enrollment + str(getEid.getEid(enrollmentNumber, url)) + "/" + enrollmentWorkflowStep
    time.sleep(.01)
    response = requests.get(endpointWFS, headers=headers)
    rsp_jsn = response.json()
    rsp_jsn3 = len(rsp_jsn['Data'])
    if(rsp_jsn3 > 1):
            #NEW EDIT 3-28-2024
        rsp_jsn2 = rsp_jsn['Data']
        for i in range(0, rsp_jsn3):
          #print(rsp_jsn2[i]['WorkflowStepName'])
            if(rsp_jsn2[i]['WorkflowStepName'] == 'Application'):
             return rsp_jsn2[i]['EnrollmentWorkflowStepId']