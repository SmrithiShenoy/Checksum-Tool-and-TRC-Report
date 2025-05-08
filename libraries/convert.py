import csv

def trc_to_csv(trc_path):
      start_row = 13
      with open(trc_path, 'r') as infile, open("converted.csv", 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            header = ['Index', 'Time', 'Type', 'ID', 'Length', 'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6','D7']
            writer.writerow(header)
            readinfo=list(csv.reader(infile))
            for i in range(0, len(readinfo)):
                  if i>start_row:
                        parts=readinfo[i][0].strip().split() 
                        writer.writerow(parts)
      print(f"Successfully converted {trc_path} to converted.csv")




