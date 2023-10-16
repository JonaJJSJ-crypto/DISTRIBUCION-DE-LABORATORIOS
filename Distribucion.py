import pandas as pd
import numpy as np

Columnas=["DOCENTE", "FACULTAD", "PARALELO", "ASISTENTE", "Num Est", "Num Prac", "Num Inf", "DIA", "HORA"]

df = pd.read_excel("horario.xlsx", sheet_name="distribucion",header=3, usecols=Columnas)
for i in range (7,21):
    df[str(i)] = None
for index , row in df.iterrows():
    hora = row["HORA"].lower()
    position = hora.find("h")
    if position!=-1:
        #df.loc[index][str(int(hora[0:position]))] = int(hora[0:position])
        ini = int(hora[0:position])
        #print(hora,"\n", ini, end=" ")
        hora = hora[position+1:]
        end = int(hora[hora.find("-")+1:hora.find("h")])
        while ini < end+1:
            df.at[index,str(ini)] = ini
            ini += 1
        #print(end)

#df.to_excel("Final.xlsx", index=True)

# Define the number of bins and their boundaries
bin_labels = ["1","2","3","4","5"]

# Cut the 'Values' column into equal bins
df['Binned'] = pd.qcut(df["Num Inf"], q = 5, labels=bin_labels)

Matutino = ["JORGE CALDERON", "JORGE GUACHAMIN", "JORGE CHIMARRO", "ELSA AREQUIPA", "EDDY", 
            "WASHINGTON LOMAS", " VANESA CHALUISA", "SANTIAGO POMA", "LUIS",
            "WLADIMIR", "EVERSON", "DANIEL", "DANIELA", "FELIPE"]
Vespertino = ["CLAUDIA", "JONATHAN", "JORGE POMA", "ALEJANDRA", "FERNANDO SISA"]
df["HORARIO"] = None
for index , row in df.iterrows():
    tec = row["ASISTENTE"]
    for name in Matutino:
        if tec.find(name) != -1:
            df.at[index, "HORARIO"] = "713"

    for name in Vespertino:
        if tec.find(name) != -1:
            df.at[index, "HORARIO"] = "1220"

    if df.at[index, "HORARIO"] == None:
        print(row["ASISTENTE"])

for i in range(1):
    ss=1
# Display the sorted and binned DataFrame
print(df)
for index, row in df.iterrows():
    squed = row["HORARIO"]
    ini = (int(squed) // 100) % 10 + ((int(squed) // 1000) % 10) *10
    end = int(squed) - (ini * 100)
    #print(squed, ini, end)
    hora = row["HORA"].lower()
    position = hora.find("h")
    ini1 = int(hora[0:position])
    #print(hora,"\n", ini, end=" ")
    hora = hora[position+1:]
    end1 = int(hora[hora.find("-")+1:hora.find("h")])

    if ini1 < ini or end < end1: print(row["ASISTENTE"], ini, ini1, end, end1)
df.to_excel("Final.xlsx", index=True)
 


#duplicates = df[df.duplicated(subset=['DIA', 'HORA'], keep=False)]

#print(duplicates)
