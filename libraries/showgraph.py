import matplotlib.pyplot as plt
import csv
import numpy as np

def showgraph(fil_path):
    with open(fil_path, "r", encoding='utf-8') as f: 
        parameter = list(csv.reader(f))
        sv = []
        bv = []
        sc = []
        bc = []
        time = []
        for i in range(1, len(parameter)):
            if parameter[i][0] == '01458001':
                sv.append(float(parameter[i][2]))
                bv.append(float(parameter[i][3]))
                sc.append(float(parameter[i][4]))
                time.append(float(parameter[i][1]))
            if  parameter[i][0] == '01458008':
                bc.append(float(parameter[i][7]))

    fig, axs1 = plt.subplots(2, 1, figsize=(14, 8))
    axs1[0].plot(time, sv, label="Stack Voltage")
    axs1[0].plot(time, bv, label="Battery Voltage")
    axs1[0].set_xlabel("Time", labelpad=20)
    axs1[0].set_ylabel("Values")
    axs1[0].legend()
    axs1[0].grid(True)
    axs1[0].set_xticks(np.arange(min(time), max(time) + 30000, 30000))

    axs1[1].plot(time, sc, label="Stack Current")
    axs1[1].plot(time, bc, label="Battery Current")
    axs1[1].set_xlabel("Time", labelpad=20)
    axs1[1].set_ylabel("Values")
    axs1[1].legend()
    axs1[1].grid(True)
    axs1[1].set_xticks(np.arange(min(time), max(time) + 30000, 30000))

    fig2, axs2=plt.subplots(1, 1, figsize=(14, 8))
    axs2.plot(time, sv, label="Stack Voltage")
    axs2.plot(time, bv, label="Battery Voltage")
    axs2.plot(time, sc, label="Stack Current")
    axs2.plot(time, bc, label="Battery Current")
    axs2.legend()
    axs2.grid(True)
    axs2.set_xticks(np.arange(min(time), max(time) + 30000, 30000))

    plt.tight_layout() 
    plt.show()

    plt.figure(figsize=(14,8))





        
        
        
    

        

    
