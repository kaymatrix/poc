import csv
onboarding_list =[]
onboarding_and_deleted = []
with open('input.csv','r') as f:
    reader = csv.reader(f,delimiter = "|")
    for row in reader:
        name = row[0].strip()
        customer_id = row[1].strip()
        deleted = row[2].strip()
        mss = row[3].strip()
        mf = row[4].strip()
        empty = row[5].strip()
        onboard_status = row[6].strip()
        #print(name,customer_id,deleted,mss,mf,onboard_status)
        if onboard_status == 'Onboarded':
            print(name,'\t',customer_id,'\t',deleted,'\t',mss,'\t',mf,'\t',onboard_status)