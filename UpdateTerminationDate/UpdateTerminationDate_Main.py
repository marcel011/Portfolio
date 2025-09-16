import requests
import json
import csv
import time
import datetime
from datetime import timedelta
import multiprocessing as mp
from multiprocessing import Manager, Lock
from Modules import getAppWFS


env = 'UA1'
if (env == 'UA1') :
        url = "https://rebates-ua1.austinenergy.com/api/v1/" 
        apiKey = ''
elif(env == 'PRD'):
        url = "https://rebates.austinenergy.com/api/v1/" 
        apiKey = ''

headers = {'APIKey' : apiKey}
enrollment = "Enrollment/"
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"
enrollmentWorkflowStepId = "enrollmentWorkflowStepId/"
updateTerm = "UpdateTerminationDate"
termdate = "terminationDate="
Measure = 'Measure'

def init(l):
      global lock
      lock = l




def updateTerminationDate(enrollmentNumber): 
        #/v{version}/Enrollment/{enrollmentId}
        #https://rebates-ua1.austinenergy.com/api/v1/Enrollment/138148/enrollmentWorkflowStepId/264971/UpdateTerminationDate?terminationDate=5%2F23%2F2025

        #Get Application Wfs
    with lock:
        
        terminationDate = str(datetime.datetime.now() - timedelta(1))
        #terminationDate = ""
        print('Termination Date', terminationDate)

        wfsTD = getAppWFS.getAppWFS(enrollmentNumber, url)
        #print('Application WFS Data:', wfsTD)
        time.sleep(.01)

        wfsID = str(wfsTD['EnrollmentWorkflowStepId'])
        enrId = str(wfsTD['EnrollmentId'])
        if(terminationDate == ""):
            updateTD = url + enrollment + enrId + '/' + enrollmentWorkflowStepId + wfsID + '/' + updateTerm 
        else:
            updateTD = url + enrollment + enrId + '/' + enrollmentWorkflowStepId + wfsID + '/' + updateTerm + '?' + termdate + terminationDate
             
             
        
        #print(updateTD)
        print(enrollmentNumber)
        #print(wfsTD['Properties'])
        #for properties, values in wfsTD.items():
         #print(properties, values)
        '''for i in range(len(wfsTD['Properties'])):
             #print(wfsTD['Properties'][i])
             if('Termination Date' in wfsTD['Properties'][i]['Name']): # if (wfsTD['Properties'][i]['Name'] = 'Termination Date'):
                  wfsTD['Properties'][i]['Value'] = (datetime.datetime.now() - timedelta(1)).strftime('%Y-%m-%dT00:00:00')
                  wfsTD['Properties'][i]['Value'] = str(wfsTD['Properties'][i]['Value'])
                  print('Termination Date Found: ', wfsTD['Properties'][i]['Name'], wfsTD['Properties'][i]['Value'])'''
        
   

                
        #update Wfs
        print('Updating Termination Date')
        #print(wfsTD)
        rsp_ld = json.dumps(wfsTD).replace('Unassigned', '')
        headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
        response = requests.put(updateTD, headers=headerp, data=rsp_ld)
        time.sleep(.01)
      

        rjsn = response.json()
        print(response)

        #UPDATE RESPONSE HANDLING FROM MESSAGES
        if(rjsn['Messages']):
            print(rjsn['Messages'])
        
        #process Application wfs to 'save' Termination Date
        
        

if __name__ == "__main__":
    
    whole_start = time.time()
    process_start = time.time()
    l = mp.Lock()

    enr = [
    
]
   
    #with open(r'L:\Python\Recurring Incentive - PPT\Recurring Incentive PPT - Final\UpdateTerminationDateRd4.csv') as apiread:
        #print("Pool Start Time: ", datetime.datetime.now())
        #csvi = csv.DictReader(apiread)
        #for data in csvi:
            #print(data['Enrollments'])
            #if data != None:
                #enr.append(data['Enrollments'])
        #time.sleep(.001)
    

    
   

    print("Update Termination Date Start Time: ", datetime.datetime.now())
    updttd_start = time.time()
    pool = mp.Pool(mp.cpu_count())
    pool = mp.Pool(initializer= init, initargs= (l,))
    pool.map(updateTerminationDate, enr)
    pool.close()
    pool.join()

    updttd_end = time.time() - updttd_start
    updttdsec = updttd_end % 60
    updttdmin = int(updttd_end/60)
    print("Add Termination Date Time Elapsed: ", updttdmin, "minutes ", updttdsec, "seconds\n")

    #updateTerminationDate('1334453', url)