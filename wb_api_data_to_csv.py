import wbdata
import datetime
import os
os.chdir('C:/Users/CKIRAC15')
 
data_date = (datetime.datetime(2005, 1, 1), datetime.datetime(2019, 1, 1))
countries=['ARG','TUR','BRA','POL','FIN','BGR','BIH','USA','AUT','KAZ',\
           'NOR','TUN','KOR','NIC','COL','MLT','ROM','SWE','RUS','IND',\
           'FIN','FRA','GRC','UKR','CAN','HRV','CHE','MKD']
indicators = {"NY.GDP.PCAP.PP.KD": "GDP_PER_CAPITA",\
             "SP.DYN.LE00.IN":"LIFE_EXPECTANCY","JI.UEM.1524.HE.ZS":'YOUTH_UNEMPLOYED',\
             "TX.VAL.TECH.MF.ZS":"HIGH_TECH_EXPORTS",\
             "VC.IHR.PSRC.P5":"HOMICIDE_INDEX",\
             "RL.PER.RNK":"RULE_OF_LAW_INDEX","SI.POV.GINI":"INCOME_INEQUALITY","UIS.SLE.02.GPI":"GENDER_PARITY_TERTIARY_EDUCATION"}
df = wbdata.get_dataframe(indicators, country=countries, data_date=data_date)
#new_df=df.dropna()
df.to_csv('gdp_per_capita.csv')
