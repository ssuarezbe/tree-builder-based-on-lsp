from tmengine import TextMateEngine
import json
import os

sample_code = """
//MTLUSR00 JOB (999,POK),'METAL',CLASS=A,MSGCLASS=H,NOTIFY=&SYSUID
//* 
//* BINDER USING THE METAL XPI SAMPLE PROGRAM 
//* //LKED     EXEC  PGM=IEWL,REGION=256K, 
//    PARM='LIST,LET,XREF,MAP,AC(0),RENT,REUS,AMODE(31)' 
//SYSPRINT DD  SYSOUT=* 
//SYSUT1   DD  SPACE=(CYL,(10,10)),UNIT=SYSDA 
//SYSLMOD  DD  DSN=MTLUSR.XPLINK.LOAD,DISP=SHR 
//SYSLIB   DD  DSN=CICSTS41.CICS.SDFHLOAD,DISP=SHR 
//         DD  DISP=SHR,DSN=MTLUSR.METAL.OBJ 
//         DD  DISP=SHR,DSN=MTLUSR.METALC.SCCNOBJ 
//USROBJ   DD  DSN=MTLUSR.METAL.OBJ,DISP=SHR 
//SYSLIN    DD *  
INCLUDE USROBJ(MTLBTXPI)  
INCLUDE USROBJ(MTL2XPI)  
ENTRY MTLBTXPI  
NAME  MTLBTXPI(R) 
/*
"""

code_2 = """
METAL GENASM
OPT(0) PHASEID LANGLVL(EXTENDED)
SO LIST CSECT
float(ieee)
DEF(MVS,CM_MVS,_TCP31_PROTOS)
nose se(/usr/include/metal, DD:SYSLIB)
SSCOM
AGG
RENT
"""

current_path = os.path.dirname(__file__) 
grammar_file = os.path.join(current_path, 'syntaxes/jcl.tmLanguage.json')
print(f"grammar_file={grammar_file}")
with open(grammar_file, 'r') as f:
    engine2 = TextMateEngine(json.load(f)) 
    print(engine2.languages)
    r = engine2.parse('source.jcl', code_2)
    for v in r:
        print(f"token={v}")
        range_vals = v.range
        print(f"range_vals={range_vals}")
        t = code_2[range_vals[0]:range_vals[1]]
        print("text=''''\n{}''")