# -*- coding: utf-8 -*-
S='0A0D10131013161A'
m4=(int(S[4:6],16)-int(S[0:2],16)+int(S[8:10],16)-22)/2
m2=int(S[4:6],16)-m4-16
m0=int(S[0:2],16)-m2-10
 
m5=(int(S[6:8],16)-int(S[2:4],16)+int(S[10:12],16)-25)/2
m1=int(S[10:12],16)-m5-19
m3=int(S[2:4],16)-m1-13
 
if (m0 >= 0 and m1 >= 0 and m2 >= 0 and m3 >= 0 and m4 >= 0 and m5 >= 0):
        print 'MAC地址为%02x:%02x:%02x:%02x:%02x:%02x'%(m0,m1,m2,m3,m4,m5)
else:
        MAC0 = '%02x:%02x:%02x:%02x:%02x:%02x'%(m0%256,m1%256,m2%256,m3%256,m4%256,m5%256)
        MAC = MAC0.replace(':','')
        S2 = '%02X%02X%02X%02X%02X%02X%02X%02X'%((int(MAC[0:2],16)+int(MAC[4:6],16)+10)%256,(int(MAC[2:4],16)+int(MAC[6:8],16)+13)%256,(int(MAC[4:6],16)+int(MAC[8:10],16)+16)%256,(int(MAC[6:8],16)+int(MAC[10:12],16)+19)%256,(int(MAC[8:10],16)+int(MAC[0:2],16)+16)%256,(int(MAC[10:12],16)+int(MAC[2:4],16)+19)%256,(int(MAC[0:2],16)+int(MAC[4:6],16)+22)%256,(int(MAC[2:4],16)+int(MAC[6:8],16)+26)%256)
        if (S.lower() == S2.lower()):
                print 'MAC地址为'+MAC0
        else:
                print '反推失败'