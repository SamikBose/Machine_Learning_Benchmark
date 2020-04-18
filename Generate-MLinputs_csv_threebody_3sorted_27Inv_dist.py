import numpy as np
import math
numsnap = 120*452
fout1_inv = open("100K+300K-ThreeBodyTerm-3sort-trimer.csv","w")         #Output csv file
fout1_inv.write("f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20,f21,f22,f23,f24,f25,f26,f27,resp\n")
mean_int_en  = 0.00000000
tup1 = []
tup2 = []
tup3 = []
for x in xrange(1,numsnap+1):     #This counter can be modified as per the number of omega dimer files.
        lines = []
        tup1 = []
        tup2 = []
        tup3 = []
        a = 0
        b = 0
        fin1= open("Water_BSSE_tri-with-di_100K+300K_config_"+str(x)+".in.out","r")
        lines1= fin1.readlines()

        for y in xrange(len(lines1)):
                if ("WARNING:      negative BSSE" not in lines1[y]):
                        lines.append(lines1[y])
                else:
                        print x

	length = len(lines)

        for y in xrange(length):
                toks= lines[y].split()
                if((y < 0.25*length) and (len(toks)>3)and(toks[0]=="Fragment")and(toks[1]=="E(TOTAL)")and(toks[2]=="E(CP-CORR)")and(toks[3]=="DE(BSSE)")):
                        toks1 = lines[y+2].split()
                        fr1_tri_mono = float(toks1[2])
                        toks2 = lines[y+3].split()
                        fr2_tri_mono = float(toks2[2])
                        toks3 = lines[y+4].split()
                        fr3_tri_mono = float(toks3[2])
                        toks4 = lines[y+5].split()
                        tri_total_en = float(toks4[1])

                        tri_int_en = (tri_total_en - fr1_tri_mono - fr2_tri_mono - fr3_tri_mono)


                if ((y < 0.25*length) and (len(toks)>3) and toks[0]=="O" and toks[1]=="("):
                        a = a + 1
                        if ((a == 2) or (a == 3)):
                                for i in xrange(a - 1):
                                        tup1.append(1.000000000/float(toks[3*(i+1)]))
                                        tup2.append(1.000000000/float(toks[3*(i+1)+1]))
                                        tup2.append(1.000000000/float(toks[3*(i+1)+2]))

                if ((y < 0.25*length) and (len(toks)>3) and toks[0]=="H" and toks[1]=="("):
                        b = b + 1
                        if (( b > 2) and (b < 7)):
                                for i in xrange((b-1)/2):
                                        tup2.append(1.000000000/float(toks[3*(i+1)]))
                                        tup3.append(1.000000000/float(toks[3*(i+1)+1]))
                                        tup3.append(1.000000000/float(toks[3*(i+1)+2]))

        	if((y<length/2)and(y>length/4)and(len(toks)>3)and(toks[0]=="Fragment")and(toks[1]=="E(TOTAL)")and(toks[2]=="E(CP-CORR)")and(toks[3]=="DE(BSSE)")):
                	toks1 = lines[y+2].split()
              	 	fr1_di1_mono = float(toks1[2])
                	toks2 = lines[y+3].split()
                	fr2_di1_mono = float(toks2[2])
                	toks3 = lines[y+4].split()
                	di1_total_en = float(toks3[1])


        	if((y<3*length/4)and(y>length/2)and(len(toks)>3)and(toks[0]=="Fragment")and(toks[1]=="E(TOTAL)")and(toks[2]=="E(CP-CORR)")and(toks[3]=="DE(BSSE)")):
                	toks1 = lines[y+2].split()
                	fr1_di2_mono = float(toks1[2])
                	toks2 = lines[y+3].split()
                	fr2_di2_mono = float(toks2[2])
                	toks3 = lines[y+4].split()
                	di2_total_en = float(toks3[1])

        	if((y<length)and(y>3*length/4)and(len(toks)>3)and(toks[0]=="Fragment")and(toks[1]=="E(TOTAL)")and(toks[2]=="E(CP-CORR)")and(toks[3]=="DE(BSSE)")):
                	toks1 = lines[y+2].split()
                	fr1_di3_mono = float(toks1[2])
                	toks2 = lines[y+3].split()
                	fr2_di3_mono = float(toks2[2])
                	toks3 = lines[y+4].split()
                	di3_total_en = float(toks3[1])

#       i_total_en,di1_total_en,di2_total_en,di3_total_en
        sum_delta_di_BSSE=(di1_total_en - fr1_di1_mono - fr2_di1_mono) + (di2_total_en - fr1_di2_mono - fr2_di2_mono) + (di3_total_en - fr1_di3_mono - fr2_di3_mono)
#	print di1_total_en, fr1_di1_mono, fr2_di1_mono
#	print di2_total_en, fr1_di2_mono, fr2_di2_mono
#	print di3_total_en, fr1_di3_mono, fr2_di3_mono
#	print sum_delta_di_BSSE

	delta_tri_BSSE = (tri_int_en - sum_delta_di_BSSE)

        s_tup1 = sorted(tup1)
        s_tup2 = sorted(tup2)
        s_tup3 = sorted(tup3)

#       print s_tup1
#       print s_tup2
#       print s_tup3

        NEWLINE1_inv= ("%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f\n")%(s_tup1[0],s_tup1[1],s_tup1[2],s_tup2[0],s_tup2[1],s_tup2[2],s_tup2[3],s_tup2[4],s_tup2[5],s_tup2[6],s_tup2[7],s_tup2[8],s_tup2[9],s_tup2[10],s_tup2[11],s_tup3[0],s_tup3[1],s_tup3[2],s_tup3[3],s_tup3[4],s_tup3[5],s_tup3[6],s_tup3[7],s_tup3[8],s_tup3[9],s_tup3[10],s_tup3[11],delta_tri_BSSE)
#		print tri_int_en
        fout1_inv.write(NEWLINE1_inv)

