import pandas as pd

entry_file = "consolidado.xlsx"

exit_file = "consolidado_powerbi.xlsx"

columns = [
    "HABILIDADES DE TRABALHO",
    "NODE",
    "TECNICO",
    "LOGIN",
    "SUPERVISOR",
    "COP",
    "PERIODO",
    "INICIO",
    "FIM",
    "DESLOCAMENTO",
    "CONTRATO",
    "WO",
    "OS",
    "COD",
    "TIPO OS",
    "JOB COD",
    "TIPO DE VALOR",
    "VALOR TECNICO",
    "PONTO"
]

# Carrega a planilha
df = pd.read_excel(entry_file)

# Mantém apenas as colunas desejadas (colunas que existirem)
df_filtrado = df[columns]

# Salva o resultado em um novo arquivo
df_filtrado.to_excel(exit_file, index=False)

print("Arquivo gerado com sucesso:", entry_file)


### STEP 2 ###
df_filtrado = df_filtrado.dropna(subset=["CIDADE"])
