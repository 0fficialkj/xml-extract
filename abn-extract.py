import os #re
import xml.etree.ElementTree as ET
import time
import csv
    

def writeHeader():
    with open('Out.csv', 'w', newline='') as xml_data_to_csv:
        Csv_writer = csv.writer(xml_data_to_csv)
        list_head = ['ABN', 'ABN Status', 'Entity Type Ind', 'Entity Type Text', ' GST Status', 'GST Status From Date']
        Csv_writer.writerow(list_head)

def strip_abn_xml(filename):
    with open('Out.csv', 'a', newline='') as xml_data_to_csv:
        tree = ET.parse(filename)
        root = tree.getroot()
        Csv_writer = csv.writer(xml_data_to_csv)
        
        for element in root.findall('ABR'):
            List_nodes = []
            #get ABN value
            ABN = element.find('ABN').text
            List_nodes.append(ABN)  

            #get ABN Status Value
            ABNStatus = element.find('ABN').get('ABNStatusFromDate')
            List_nodes.append(ABNStatus)

            #get Entity Type Ind value
            EntityTypeInd = element.find('EntityType').find('EntityTypeInd').text
            List_nodes.append(EntityTypeInd) 

            #get entity type text value
            EntityTypeText = element.find('EntityType').find('EntityTypeText').text
            List_nodes.append(EntityTypeText) 

            #get GST status value
            GSTStatus = element.find('GST').get('status')
            List_nodes.append(GSTStatus) 

            #get GST status from date value
            GSTStatusFromDate = element.find('GST').get('GSTStatusFromDate')
            List_nodes.append(GSTStatusFromDate) 

            Csv_writer.writerow(List_nodes)

        xml_data_to_csv.close()

if __name__ == "__main__":
    writeHeader()
    for c in range(1, 10):
        strip_abn_xml(f"C:\\Users\\637981\\Desktop\\ABN-XML-CSV\\20200226_Public0{c}.xml")
    for c in range(10, 21):
        strip_abn_xml(f"C:\\Users\\637981\\Desktop\\ABN-XML-CSV\\20200226_Public{c}.xml")


