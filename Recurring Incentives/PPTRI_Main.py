from Modules import getAppWFSMeasureQty
from Modules import getAppWFSMeasure
from Modules import getEid
from Modules import getIPWFS
from Modules import getIPWFSId
from Modules import getRIWFS
from Modules import getRIWFSId
import requests
import json
import time
import os
import multiprocessing as mp
import datetime
#import xlsxwriter
import csv
from multiprocessing import Manager, Lock

#UPDATE ENVIRONMENT BEFORE RUN!!!
env = 'UA1'
if (env == 'UA1') :
        url = "" 
        apiKey = ""
elif(env == 'PRD'):
        url = "" 
        apiKey = ""

headers = {'APIKey' : apiKey}
stp_outcome = {"Outcome": "Work Complete"}
enrollment = "Enrollment/"
enrollmentWorkflowStep = "EnrollmentWorkflowStep/"
Measure = 'Measure'

def init(l):
      global lock
      lock = l


RI_WFS = {
'ActualVisitDate': '2023-10-25T00:00:00', 
'ActualVisitEndDate': '0001-01-01T00: 00: 00', 
'AssignedContractorId': 1, 
'AssignedContractorName': 
'Austin Energy', 
'AssignedContractorAbbreviation': 'AE', 
#"""'AssignedContractorVendorNumber': '', 
#"AssignedContractorEmployeeName": "Erskine, Marcel",
#"AssignedContractorEmployeeNumber": "AEME1",
#"AssignedContractorEmployeeId": 2090, """
"AssignedContractorVendorNumber": "",
"AssignedContractorEmployeeName": "",
"AssignedContractorEmployeeNumber": "",
"AssignedContractorEmployeeId": ,
'Comments': '', 
'DueDate': '0001-01-01T00: 00: 00', 
'EnrollmentId': 0, 
'EnrollmentWorkflowStepId': 0, 
'Mileage': 0, 'DriveTime': 0.0, 
'Properties': [], 
'ScheduledVisitBeginTime': '0001-01-01T00: 00: 00', 
'ScheduledVisitEndTime': '0001-01-01T00: 00: 00', 
'WorkflowStepId': 6, 
'WorkflowStepName': 'Recurring Incentive', 
'WorkflowStepOutcomeId': 1, 
'WorkflowStepOutcome': 'Work Complete', 
'WorkflowStepOutcomeReasonId': 0, 
'WorkflowStepOutcomeReasonName': '', 
'WorkflowStepStatusId': 1, 
'WorkflowStepStatus': 'Unscheduled / Awaiting Results', 
'WorkflowStepDispositionId': 1, 
'WorkflowStepDisposition': 'Open', 
'InitialFinishDate': '0001-01-01T00: 00: 00', 
'InitiallyFinishedByUserId': 0, 
'InitiallyFinishedByUser': '', 
'Enrollment': '', 
'InspectionAssignmentTypeId': 0, 
'Measures': [], 
'Equipments': []
    }

RI_M = {
      "EnrollmentMeasureId": 0,
      "EnrollmentMeasureDetailId": 0,
      "ParentEnrollmentMeasureDetailId": 0,
      "MeasureCode": "RI",
      "MeasureSubTypeCode": "",
      "MeasureQty": None,
      "IncentiveAmount": 0,
      "IncentiveUnitAmount": 25,
      "MeasureCostAmount": None,
      "MeasureCostUnitAmount": 0,
      "IncrementalMeasureCostAmount": None,
      "IncrementalMeasureCostUnitAmount": 0,
      "Comments": "",
      "MeasureNotFeasibleCodeId": 0,
      "MeasureNotFeasibleCode": "",
      "EnrollmentMeasurePhase": "Installation",
      "PlannedMeasureQty": None,
      "ApprovedMeasureQty": None,
      "InstalledMeasureQty": 0,
      "InspectedMeasureQty": 0,
      "FailCorrectionActionId": 0,
      "FailCorrectionAction": None,
      "FailedQty": 0,
      "CorrectedQty": 0,
      "EnrollmentExistingEquipmentId": 0,
      "HasPastParticipation": False,
      "Properties": [
        {
          "EnrollmentMeasurePropertyId": 0,
          "PropertyName": "Estimated AE Incentive Amount",
          "PropertyValue": ""
        },
        {
          "EnrollmentMeasurePropertyId": 0,
          "PropertyName": "Comments",
          "PropertyValue": ""
        }
      ],
      "RestrictSavings": False,
      "SavingsValues": [],
      "Parts": []
    }


IP_WFS = {
    "ActualVisitDate": "0001-01-01T00:00:00",
    "ActualVisitEndDate": "0001-01-01T00:00:00",
    "AssignedContractorId": 1,
    "AssignedContractorName": "Austin Energy",
    "AssignedContractorAbbreviation": "AE",
    "AssignedContractorVendorNumber": "",
    "AssignedContractorEmployeeName": ", ",
    "AssignedContractorEmployeeNumber": "",
    "AssignedContractorEmployeeId": 2296,
    "Comments": "",
    "DueDate": "0001-01-01T00:00:00",
    "EnrollmentId": 302154,
    "EnrollmentWorkflowStepId": 0,
    "Mileage": 0,
    "DriveTime": 0,
    "Properties": [],
    "ScheduledVisitBeginTime": "0001-01-01T00:00:00",
    "ScheduledVisitEndTime": "0001-01-01T00:00:00",
    "WorkflowStepId": 25,
    "WorkflowStepName": "Initiate Payment",
    "WorkflowStepOutcomeId": 1,
    "WorkflowStepOutcome": "Work Complete",
    "WorkflowStepOutcomeReasonId": 0,
    "WorkflowStepOutcomeReasonName": "",
    "WorkflowStepStatusId": 1,
    "WorkflowStepStatus": "Unscheduled / Awaiting Results",
    "WorkflowStepDispositionId": 1,
    "WorkflowStepDisposition": "Open",
    "InitialFinishDate": "0001-01-01T00:00:00",
    "InitiallyFinishedByUserId": 0,
    "InitiallyFinishedByUser": "",
    "Enrollment": '',
    "InspectionAssignmentTypeId": 0,
    "IsPaymentRequested": 'true',
    "Measures": [],
    "Equipments": []
  }


def addRIWFS_Pool(enrollmentNumbers):
        #lock.acquire()
    with lock:
        #enrollmentWFS endpoint for PUT call
        ri_wfs = RI_WFS
        postEWFS = url + enrollmentWorkflowStep
        eid = getEid.getEid(enrollmentNumbers, url)
        print(eid)
        time.sleep(.01)
        print(f"ProcessId: {os.getpid()} \t Adding Recurring Incentive WFS to Enrollment: ", str(enrollmentNumbers))
        ri_wfs["EnrollmentId"] = str(eid)
        ri_dmp = json.dumps(ri_wfs)
        print(ri_wfs['EnrollmentId'])
        
        #posts Recurring Incentive WFS to Recurring Incentive step
        headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
        r=requests.post(postEWFS, headers=headerp, data=ri_dmp)
        time.sleep(.01)
        print(r)
        #lock.release() 

def addRIWFSMeasure_Pool(enrollmentNumbers):
        #lock.acquire()
    with lock:
        #enrollmentWFS endpoint for PUT call
        postWFS = url + enrollmentWorkflowStep + str(getRIWFSId.getRIWFSId(enrollmentNumbers, url)) + "/" + Measure
        time.sleep(.001)
        #Enrollment 1299499 has only one measure attached - RI (update later)
        ri_jsn = RI_M
        mqty = getAppWFSMeasureQty.getAppWFSMeasureQty(enrollmentNumbers, url)
        time.sleep(.001)
        #adds Recurring Incentive measure for each thermostat added in the Application WFS
        print(f"ProcessId: {os.getpid()} \t Adding Recurring Incentive Measure, Qty: {mqty}", enrollmentNumbers)
        ri_dmp = json.dumps(ri_jsn)
        for i in range(0, mqty):
       
            headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
            r=requests.post(postWFS, headers=headerp, data=ri_dmp)
            time.sleep(.01)
            print(r)
        #lock.release()       

def processRIWFS_Pool(enrollmentNumbers):
    with lock:
        #lock.acquire()
        #enrollmentWFS endpoint for GET call
        response = getRIWFS.getRIWFS(enrollmentNumbers, url)
        time.sleep(.01)

        #utcnow depracated
        #response['ActualVisitDate'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT00:00:00')
        response['ActualVisitDate'] = datetime.datetime.now().strftime('%Y-%m-%dT00:00:00')
        #response['ActualVisitDate'] = response['ActualVisitDate'].replace(microsecond=0).isoformat()
        response['ActualVisitDate'] = str(response['ActualVisitDate']) #+ "Z"
        riwfsid = str(response['EnrollmentWorkflowStepId'])

        #update Actual Visit Date in open RI Wfs before POST call
        putWFS = url + enrollmentWorkflowStep + riwfsid
        rsp_ld = json.dumps(response).replace('Unassigned', '')
        print(f"Process Id: {os.getpid()} \t Updating Recurring Incentive WFS: {enrollmentNumbers}")
        headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
        r=requests.put(putWFS, headers=headerp, data=rsp_ld)
        time.sleep(.01)
        print(r)
        rjsn = r.json()
        #UPDATE RESPONSE HANDLING FROM MESSAGES
        if(rjsn['Messages']):
            print(rjsn['Messages'])

        #POST call to Process RI Wfs    
        print("Processing Recurring Incentive WFS")
        pWFS = url + enrollmentWorkflowStep + riwfsid + '/Process'
        headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
        r=requests.post(pWFS, headers=headerp, data=stp_outcome)
        time.sleep(.01)
        print(r)
        rjsn = r.json()
        if(rjsn['Messages']):
            print(rjsn['Messages'])
        #lock.release()

def addIPWFS_Pool(enrollmentNumbers):
     #lock.acquire()
 with lock:
     ip_wfs = IP_WFS
          #enrollmentWFS endpoint for PUT call
     postEWFS = url + enrollmentWorkflowStep
     print(f"ProcessId: {os.getpid()} \t Adding Initiate Payment WFS: {enrollmentNumbers}")
     ip_wfs["EnrollmentId"] = str(getEid.getEid(enrollmentNumbers, url))
     time.sleep(.01)
     ri_dmp = json.dumps(ip_wfs).replace('Unassigned', '')
    
     headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
     r=requests.post(postEWFS, headers=headerp, data=ri_dmp)
     #print(r)
     time.sleep(.01)
     print(r)
     rjsn = r.json()
     if(rjsn['Messages']):
            print(rjsn['Messages'])
     #lock.release()

def processIPWFS_Pool(enrollmentNumbers):
        #lock.acquire()    
    with lock:
        #GET Initiate Payment Wfs
        response = getIPWFS.getIPWFS(enrollmentNumbers, url)
        time.sleep(.01)
        #true: True

        #utcnow is depracated 3-13-2024 *Marcel Franklin
        #response['ActualVisitDate'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT00:00:00')
        response['ActualVisitDate'] = datetime.datetime.now().strftime('%Y-%m-%dT00:00:00')
        response['ActualVisitDate'] = str(response['ActualVisitDate'])# + "Z"
        response['IsPaymentRequested'] = True
        ipwfsid = str(response['EnrollmentWorkflowStepId'])
        
        rsp_ld = json.dumps(response).replace('Unassigned', '')
        
        #update Actual Visit Date in open IP Wfs before POST 
        putWFS = url + enrollmentWorkflowStep + ipwfsid
        rsp_ld = json.dumps(response).replace('Unassigned', '')
       
     
        #PUT to update new dates and 'IsPaymentRequested' field
        headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
        r=requests.put(putWFS, headers=headerp, data=rsp_ld)
        time.sleep(.01)
        
        rjsn = r.json()
        if(rjsn['Messages']):
            print(rjsn['Messages'])

        #POST call to Process IP Wfs  
        print(f"ProcessId: {os.getpid()} \t Processing Initiate Payment WFS: {enrollmentNumbers}")
        pWFS = url + enrollmentWorkflowStep + ipwfsid + '/Process'
        headerp={'APIKey' : apiKey, 'Content-Type': 'application/json'}
        r=requests.post(pWFS, headers=headerp, data=stp_outcome)
        time.sleep(.01)
        print(r)
        rjsn = r.json()
        if(rjsn['Messages']):
            print(enrollmentNumbers, rjsn['Messages'])
        #lock.release()

if __name__ == "__main__":
    


    enr = [
      '1280825'
        ] 
      
    #Read Enrollments from apiEnrollments1.csv
    #workbook = xlsxwriter.Workbook(r'L:\Python\Recurring Incentive - PPT\Recurring Incentive PPT - Final\apiEnrollments1.csv')
    #0worksheet = workbook.add_worksheet()
    '''with open(r'L:\Python\Recurring Incentive - PPT\Recurring Incentive PPT - Final\apiEnrollments1.csv') as apiread:
        print("Pool Start Time: ", datetime.datetime.now())
        csvi = csv.DictReader(apiread)
        for data in csvi:
            #print(data['Enrollments'])
            if data != None:
                enr.append(data['Enrollments'])
        time.sleep(.001)'''
    
    #datetime.datetime.now(datetime.UTC)
    whole_start = time.time()
    process_start = time.time()
    l = mp.Lock()
    
    '''
    #proc = []
    print("Add RIWFS Start Time: ", datetime.datetime.now())
    addrifws_start = time.time()
    pool = mp.Pool(mp.cpu_count())
    pool = mp.Pool(initializer= init, initargs= (l,))
    pool.map(addRIWFS_Pool, enr)
    pool.close()
    pool.join()
    #proc.append(pool)
    #for p in proc:
       # p.join()
    

    addrifws_end = time.time() - addrifws_start
    addrifwssec = addrifws_end % 60
    addrifwsmin = int(addrifws_end/60)
    print("Add RIWFS Time Elapsed: ", addrifwsmin, "minutes ", addrifwssec, "seconds\n")
    
    
    #proc2 = []  
    print("Add RIWFS Measure Start Time: ", datetime.datetime.now())
    addrim_start = time.time()
    pool2 = mp.Pool(mp.cpu_count())
    pool2 = mp.Pool(initializer= init, initargs= (l,))
    pool2.map(addRIWFSMeasure_Pool, enr)
    pool2.close()
    #proc2.append(pool2)
    pool2.join()
    #for p2 in proc2:
        #p2.join()
    addrim_end = time.time() - addrim_start
    addrimsec = addrim_end % 60
    addrimmin = int(addrim_end/60)
    print("Add RIWFS Measure Time Elapsed: ", addrimmin, "minutes ", addrimsec, "seconds\n")
    
    #proc3 = []
    print("Process RIWFS Start Time: ", datetime.datetime.now())
    proriwfs_start = time.time()   
    pool3 = mp.Pool(mp.cpu_count())       
    pool3 = mp.Pool(initializer= init, initargs= (l,))
    pool3.map(processRIWFS_Pool, enr)
    pool3.close()
    pool3.join()
    #proc3.append(pool3)
    #for p3 in proc3:
        #p3.join()
    proriwfs_end = time.time() - proriwfs_start
    proriwfssec = proriwfs_end % 60
    proriwfsmin = int(proriwfs_end/60)
    print("Process RIWFS Time Elapsed: ", proriwfsmin, "minutes ", proriwfssec, "seconds\n")
    
    #proc4 = []
    print("Add IPWFS Start Time: ", datetime.datetime.now())
    addipwfs_start = time.time()   
    pool4 = mp.Pool(mp.cpu_count())
    pool4 = mp.Pool(initializer= init, initargs= (l,))
    pool4.map(addIPWFS_Pool, enr)
    pool4.close()
    pool4.join()
    #proc4.append(pool4)
    #for p4 in proc4:
        #p4.join()
    addipwfs_end = time.time() - addipwfs_start
    addipwfssec = addipwfs_end % 60
    addipwfsmin = int(addipwfs_end/60)
    print("Add IPWFS Time Elapsed: ", addipwfsmin, "minutes ", addipwfssec, "seconds\n")
    '''
    #proc5 = []
    print("Process IPWFS Start Time: ", datetime.datetime.now())
    proipwfs_start = time.time()  
    pool5 = mp.Pool(mp.cpu_count())
    pool5 = mp.Pool(initializer= init, initargs= (l,))
    pool5.map(processIPWFS_Pool, enr)
    pool5.close()
    pool5.join()
    #proc5.append(pool5)
    #for p5 in proc5:
        #p5.join()
    proipwfs_end = time.time() - proipwfs_start
    proipwfssec = proipwfs_end % 60
    proipwfsmin = int(proipwfs_end/60)
    print("Process IPWFS Time Elapsed: ", proipwfsmin, "minutes ", proipwfssec, "seconds\n")
    
    whole_end = time.time() - whole_start
    wsec = whole_end % 60
    wmin = int(whole_end/60)
    print("Project Time Elapsed: ", wmin, "minutes ", wsec, "seconds")
    