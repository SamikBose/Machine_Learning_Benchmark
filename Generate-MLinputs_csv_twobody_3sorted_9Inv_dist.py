numsnap = 45*452
fout2 = open("Sorted_typewise-3-class_9Inv-dist_1int-en_dimer.dat","w")
fout1_inv = open("Sorted_typewise-3-class_9Inv-dist_1int-en_dimer.csv","w")         #Input csv file
fout1_inv.write("f1,f2,f3,f4,f5,f6,f7,f8,f9,resp\n")
FLAG = True

#Next line changed
for x in xrange(1,numsnap+1):     #This counter can be modified as per the number of omega dimer files.
	tupO = []
	tupOH = []
	tupH = []
	a = 0
	b = 0
	FLAG = True
        fin1= open("Water_BSSEdimer100K+300K_conf_"+str(x)+".in.out","r")
        lines= fin1.readlines()	
        for z in xrange(len(lines)):
                if ("WARNING:      negative BSSE" in lines[z]):
                        FLAG = False
			print x
        if(FLAG == True):

		for y in xrange(len(lines)):
			toks= lines[y].split()
			if((len(toks)>3)and(toks[0]=="Fragment")and(toks[1]=="E(TOTAL)")and(toks[2]=="E(CP-CORR)")and(toks[3]=="DE(BSSE)")):
        			toks1 = lines[y+2].split()
        			fr1_di_mono = float(toks1[2])
        			toks2 = lines[y+3].split()
        			fr2_di_mono = float(toks2[2])
        			toks4 = lines[y+4].split()
	       			di_total_en = float(toks4[1])
	
				di_int_en = (di_total_en - fr1_di_mono - fr2_di_mono)


			if ((len(toks)>5) and toks[0]=="O" and toks[1]=="(" and toks[2] == "4)"):
				tupO.append(1.000000000/float(toks[3]))
                                tupOH.append(1.000000000/float(toks[4]))
                                tupOH.append(1.000000000/float(toks[5]))                       
			if ((len(toks)>5) and toks[0]=="H" and toks[1]=="("):
				tupOH.append(1.000000000/float(toks[3]))
				tupH.append(1.000000000/float(toks[4]))
                                tupH.append(1.000000000/float(toks[5]))

		s_tupO = sorted(tupO)
        	s_tupOH = sorted(tupOH)
        	s_tupH = sorted(tupH)


#	        print "sorted tupO", s_tupO
#		print "sorted tupO1H", s_tupO1H 
#		print "sorted tupO2H", s_tupO2H
#		print "sorted tupO3H", s_tupO3H
#        	print "sorted tupH", s_tupH

#		print "inter en", tri_int_en

		NEWLINE1_inv= ("%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f,%12.8f\n")%(s_tupO[0],s_tupOH[0],s_tupOH[1],s_tupOH[2],s_tupOH[3],s_tupH[0],s_tupH[1],s_tupH[2],s_tupH[3],di_int_en)

		NEWLINE = ("%12.8f  %12.8f  %12.8f  %12.8f  %12.8f  %12.8f  %12.8f  %12.8f  %12.8f  %12.8f\n")%(s_tupO[0],s_tupOH[0],s_tupOH[1],s_tupOH[2],s_tupOH[3],s_tupH[0],s_tupH[1],s_tupH[2],s_tupH[3],di_int_en)


		fout1_inv.write(NEWLINE1_inv)
		fout2.write(NEWLINE)
