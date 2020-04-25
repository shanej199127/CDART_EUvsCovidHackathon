# %%

import pandas as pd


# %% Init Variable Names

rki_file = 'data\RKI_Corona_Landkreise.csv'
mob_file = 'data\Global_Mobility_Report.csv'
lookup_file = 'data\LookUp_RKI_Google.csv'


rki_dropcols = ['OBJECTID', 'ADE', 'GF', 'BSG', 'RS', 'AGS', 'SDV_RS', 'GEN', 'BEZ',
                'IBZ', 'BEM', 'NBD', 'SN_L', 'SN_R', 'SN_K', 'SN_V1', 'SN_V2', 'SN_G',
                'FK_S3', 'NUTS', 'RS_0', 'AGS_0', 'WSK', 'EWZ', 'KFL', 'DEBKG_ID',
                'SHAPE__AREA', 'SHAPE__LENGTH']
# %% Load and filter

df_lookup = pd.read_csv(lookup_file)
df_lookup.columns = df_lookup.columns.str.upper()
df_rki = pd.read_csv(rki_file)
df_rki.columns = df_rki.columns.str.upper()
df_rki = df_rki.drop(columns=rki_dropcols)
df_temp = pd.read_csv(mob_file)
df_temp.columns = df_temp.columns.str.upper()
df_mob = df_temp[df_temp['SUB_REGION_1'].isin(df_lookup['GOOGLE'])]
df_mob = df_mob[df_mob['DATE'] == df_mob['DATE'].max()]

# %% merge dataframes

df_rki = df_rki.merge(df_lookup, how='left', left_on='BL', right_on='RKI')
df_data = df_rki.merge(df_mob,how='left', left_on='GOOGLE', right_on='SUB_REGION_1', )