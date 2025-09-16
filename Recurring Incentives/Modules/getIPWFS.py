from . import getEid
import time
import requests

apiKey = ""
headers = {'APIKey' : apiKey}
enrollment = "Enrollment/"
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"

def getIPWFS(enrollmentNumbers, url):
    endWFSs = url + enrollment + str(getEid.getEid(enrollmentNumbers, url)) + '/' + enrollmentWorkflowStep
    time.sleep(.01)
    response = requests.get(endWFSs, headers=headers)
    time.sleep(.01)
    rsp_jsn = response.json()
    rsp_jsn2 = rsp_jsn['Data']
    rsp_jsn3 = len(rsp_jsn['Data'])
    #1st Edit
    for i in range(0, rsp_jsn3):
          #print(rsp_jsn2[i]['WorkflowStepName'])
        if(rsp_jsn2[i]['WorkflowStepName'] == 'Initiate Payment' and rsp_jsn2[i]['WorkflowStepDisposition'] == 'Open'):
          return rsp_jsn2[i]