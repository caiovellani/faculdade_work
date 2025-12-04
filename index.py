
import pandas as pd
df = pd.read_csv('consolidado.xlsx',  delimitert=';' ,  low_memory_ false)

df = df.loc[:, 
    [
        "DATA_TOA", 
        "CIDADES", 
        "STATUS", 
        "STATUS SERVICO", 
        "TIPO DE SERVICO" , 
        "TIPO RESIDENCIA",
        "VALOR EMPRESA"
    ]
]

df.dropna(subset=['CIDADES'])
