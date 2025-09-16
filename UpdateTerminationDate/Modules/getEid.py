import time
import requests

apiKey = ""
headers = {'APIKey' : apiKey}
enrollment = "Enrollment/"


def getEid(enrollmentNumber, url):
    
   #set Endpoint for API GET Call
    enrollNum = "?filter=enrollmentNumber(" + enrollmentNumber + ")"
    endpointEnrollment = url + enrollment + enrollNum
    response = requests.get(endpointEnrollment, headers=headers) #,verify=False : bypasses check for ssl certificate
    time.sleep(.01)
    #sets variable to json response body
    rsp_jsn = response.json()
    return(str(rsp_jsn['Data']['EnrollmentId']))

