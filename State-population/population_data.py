import pandas as pd


df = pd.DataFrame()
pop_df = pd.read_csv("NST-EST2021-popchg2020_2021.csv")
pop_df = pop_df.drop(columns = ["SUMLEV","REGION","DIVISION","STATE","ESTIMATESBASE2020","POPESTIMATE2020","NPOPCHG_2020","NPOPCHG_2021","PPOPCHG_2020","PPOPCHG_2021","NRANK_ESTBASE2020","NRANK_POPEST2020","NRANK_POPEST2021","NRANK_NPCHG2020","NRANK_NPCHG2021","NRANK_PPCHG2020","NRANK_PPCHG2021"])
pop_df = pop_df.iloc[5:]
pop_df.rename(columns = {'NAME':'State', 'POPESTIMATE2021':'Population'}, inplace = True)
p = pop_df.reset_index(drop=True)
df = df.append([p])
df.to_csv(f"State-population.csv")
