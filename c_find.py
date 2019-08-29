#coding=utf-8
from pydicom.dataset import Dataset
from pydicom.uid import (
ImplicitVRLittleEndian,
ExplicitVRLittleEndian,
ExplicitVRBigEndian)
from pynetdicom import AE
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind
from pynetdicom.sop_class import BasicWorklistManagementServiceClass
from pynetdicom import AE, BasicWorklistManagementPresentationContexts
# Initialise the Application Entity
ae = AE(ae_title=b'WHTM-116')
#VerificationSOPClas'1.2.840.10008.3.1.1.1'#
ae.add_requested_context('1.2.840.10008.5.1.4.31',
 [ImplicitVRLittleEndian,
  ExplicitVRLittleEndian,
ExplicitVRBigEndian])

# Create our Identifier (query) dataset
ds = Dataset()
#ds.PatientName = ''
#ds.PatientID ='2019052700000014'
#ds.ScheduledProcedureStepStartDate = "20190711-20190711"

#在tag(0040,0100)中指定程序执行所需要执行的特定内容，例如此处指定需要查询的登记时间
proc_seq = Dataset()
#proc_seq.ScheduledStationAETitle = 'WORKLISTSERVER'
proc_seq.ScheduledProcedureStepStartDate = '20190717-'  #指定查询格式为-20190713，即查询13号之前的所有病例
#proc_seq.Modality = 'CT'
ds.ScheduledProcedureStepSequence = [proc_seq]

print(ds)
# Associate with peer AE at IP 127.0.0.1 and port 11112
assoc = ae.associate('10.3.2.79',3321,ae_title=b'WORKLISTSERVER')

if assoc.is_established:
    # Use the C-FIND service to send the identifier
    responses = assoc.send_c_find(ds , msg_id=1, priority=2,query_model='W')
    for (status, identifier) in responses:
        if status:
            print('C-FIND query status: 0x{0:04x}'.format(status.Status))

            # If the status is 'Pending' then identifier is the C-FIND response
            if status.Status in (0xFF00, 0xFF01):
                print(identifier)
        else:
            print('Connection timed out, was aborted or received invalid response')

     # Release the association
    assoc.release()
else:
    print('Association rejected, aborted or never connected')