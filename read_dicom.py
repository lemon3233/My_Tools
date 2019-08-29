#coding=utf-8
import pydicom
from pydicom import dcmread

filename = r"E:\code\dicom\98416244_20130514_CT_1_1_1.dcm"
#dcm = pydicom.read_file(filename)
dataset = dcmread('E:\code\dicom\98416244_20130514_CT_1_1_1.dcm')
print(dataset.pixel_array)