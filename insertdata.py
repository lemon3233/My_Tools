#coding=utf-8
import time
import mysql.connector
import uuid
import random as Ran

conn = mysql.connector.connect(
    host = '10.3.11.173',
    port = 3306,
    user = 'root',
    passwd = '111111',
    db = 'hm20170803',
)
cur = conn.cursor()
def RanNum(level1,level2):
    num=Ran.randint(level1,level2)
    return num
#生成uid
def uid():
    suuid = str(uuid.uuid1())
    iuuid = suuid.split('-')
    suuid = ''.join(iuuid)
    return suuid
#生成sql执行语句
def cmd(insertCnt):
    s = ("%s," * 9)[:-1]
    patientString = r"""INSERT INTO patient(Refid,id,NAME,SEX,BIRTHDAY,IDCARD_NO,ACTIVE,DELETED,VERSION)VALUES(%s)"""%(s)
    s = ("%s," * 30)[:-1]
    rclcString = r"""INSERT INTO clt_consultation(REFID,ID ,CONSULTATION_INTENT ,CONSULTATION_TYPE ,PRIORITYDIC ,APPOINTMENT ,INTERACTIVE ,APPLY_MEDICAL ,APPLY_DEPART ,APPLY_DOCTOR,
    APPLY_DATE ,SPECIFY_DATE  ,PATIENT_TYPE ,PATIENT_REFID ,APPLY_TYPE ,PATIENT_AGE ,DIAGNOSIS_TYPE ,DIAGNOSIS_STATE ,IS_UPLOAD ,APPLICATIONSTATUS ,
    CONSULTATIONSTATUS ,ACTIVE ,CREATE_DATETIME ,DELETED ,MODIFY_DATETIME ,PATIENT_AGE_UNIT ,COUNT_NUM,INSPECTION_DATE ,RECEIVE_DATE ,SAMPLING_QUANTITY )VALUES(%s)"""%(s)
    patientStringList = []
    rclcStringList = []
    for i in range(insertCnt):
        patientrefid = uid()
        rclcrefid = uid()
        patientStringList.append([patientrefid,'1','num','M','2006-05-11 00:00:00','222222222222333','1','0','1'])
        rclcStringList.append([rclcrefid, RanNum(1,20000),'TEST', '2', '1', '0', '1', '13bf65e1c07744c7b18efbf092e5b46a', 'fe9be9ae961c457a943d99361aff334a',
	    'd601d2e9e620475f8643b0dc8bc1a7ba', '2017-08-04 10:12:31',  '0001-01-01 00:00:00', '0',
	    'f57b7cdc6ab3417ab30c47d2ad5099d2',  '0', '31', '0', '0', '0', '1', '1', '0', '2017-06-29 10:12:31',  '0',
	    '1900-01-01 00:00:00', 'D', '1', '0001-01-01 00:00:00', '0001-01-01 00:00:00','0'])
    return patientString, patientStringList, rclcString, rclcStringList
def execute(insertCnt):
    starttime = time.localtime()
    print starttime
    sql1, sqll1, sql2, sqll2 = cmd(insertCnt)
    cur.executemany(sql1,sqll1)
    cur.executemany(sql2,sqll2)
    conn.commit()
    endtime = time.localtime()
    cur.close()
    print 'done',endtime
if __name__ == '__main__':
    execute(10000)