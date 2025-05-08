
import csv
def filterfile(fil_path):
    with open("converted.csv", 'r') as infile, open(fil_path, 'w', newline='') as outfile:
        writer=csv.writer(outfile)
        header = ['ID', 'TIME STAMP','STACK VOLTAGE', 'BATTERY VOLTAGE', 'STACK CURRENT', 'TEMPERATURE', 'AUX', 'BATTERY CURRENT', 'ERROR']
        writer.writerow(header)
        reader = csv.reader(infile)
        for row in reader:
            if row[3]=='01458001':
                stvo=(int((row[5]+row[6]),16))/100
                bvo=(int((row[7]+row[8]),16))/100
                sc=(int((row[9]+row[10]),16))/100
                temp=(int((row[11]+row[12]),16))/10
                writer.writerow([row[3],row[1],stvo,bvo, sc, temp, '-', '-', '-'])
            elif row[3]=='01458008':
                aux=(int((row[7]+row[8]),16))/100
                bc=(int((row[11]+row[12]),16))/100
                writer.writerow([row[3],row[1],'-', '-', '-','-', aux, bc, '-'])
            elif row[3]=='01458002':
                if row[7]=="0B":
                    writer.writerow([row[3],row[1],'-', '-', '-','-', '-', '-', 'CAN error'])
                if row[7]=="0A":
                    writer.writerow([row[3],row[1],'-', '-', '-','-', '-', '-', 'Out of Buck error'])
                if row[7]=="0C":
                    writer.writerow([row[3],row[1],'-', '-', '-','-', '-', '-', 'Battery Voltage error'])
                if row[7]=="0D":
                    writer.writerow([row[3],row[1],'-', '-', '-','-', '-', '-', 'Stack Voltage error'])
                if row[7]=="0E":
                    writer.writerow([row[3],row[1],'-', '-', '-','-', '-', '-', 'Temperature error'])
                






                            

            
            
