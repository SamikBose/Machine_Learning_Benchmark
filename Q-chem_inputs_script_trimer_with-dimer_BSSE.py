fin = open("100K+300K_452snaps_noPBC_center.gro", "r")
lines = fin.readlines()
length = len(lines)
numsnap = length/33
icount = 0
x = 0

for i in xrange(452):
	icount = icount +2
	l = 10
	for j in xrange(10):
		toksj1 = lines[icount+3*j+0].split()
		toksj2 = lines[icount+3*j+1].split()
		toksj3 = lines[icount+3*j+2].split()
		for k in xrange(1,10 - j): #This loop needs to be modified
			toksk1 = lines[icount+3*j+3*k+0].split()
			toksk2 = lines[icount+3*j+3*k+1].split()
			toksk3 = lines[icount+3*j+3*k+2].split()
			for m in xrange(1,10 - j - k):
				x = x + 1
#				print x
				fout = open("Water_BSSE_tri-with-di_100K+300K_config_"+str(x)+".in", 'w') 
				toksm1 = lines[icount+3*j+3*k+3*m+0].split()
                                toksm2 = lines[icount+3*j+3*k+3*m+1].split()
                                toksm3 = lines[icount+3*j+3*k+3*m+2].split()

				fout.write("$rem\njobtype BSSE\nbasis 6-31+G*\nexchange omegab97X-D\nmax_scf_cycles 200\nSCF_convergence 6\n$end\n\n$molecule\n0 1\n--\n0 1\n")
				newline1 = (toksj1[1][:1] +"  "+ str(float(toksj1[3])*10) +"  "+ str(float(toksj1[4])*10) +"  "+ str(float(toksj1[5])*10)+"\n")
                	        newline2 = (toksj2[1][:1] +"  "+ str(float(toksj2[3])*10) +"  "+ str(float(toksj2[4])*10) +"  "+ str(float(toksj2[5])*10)+"\n")
                        	newline3 = (toksj3[1][:1] +"  "+ str(float(toksj3[3])*10) +"  "+ str(float(toksj3[4])*10) +"  "+ str(float(toksj3[5])*10)+"\n")
                        	newline4 = (toksk1[1][:1] +"  "+ str(float(toksk1[3])*10) +"  "+ str(float(toksk1[4])*10) +"  "+ str(float(toksk1[5])*10)+"\n")
                        	newline5 = (toksk2[1][:1] +"  "+ str(float(toksk2[3])*10) +"  "+ str(float(toksk2[4])*10) +"  "+ str(float(toksk2[5])*10)+"\n")
                        	newline6 = (toksk3[1][:1] +"  "+ str(float(toksk3[3])*10) +"  "+ str(float(toksk3[4])*10) +"  "+ str(float(toksk3[5])*10)+"\n")
                                newline7 = (toksm1[1][:1] +"  "+ str(float(toksm1[3])*10) +"  "+ str(float(toksm1[4])*10) +"  "+ str(float(toksm1[5])*10)+"\n")
                                newline8 = (toksm2[1][:1] +"  "+ str(float(toksm2[3])*10) +"  "+ str(float(toksm2[4])*10) +"  "+ str(float(toksm2[5])*10)+"\n")
                                newline9 = (toksm3[1][:1] +"  "+ str(float(toksm3[3])*10) +"  "+ str(float(toksm3[4])*10) +"  "+ str(float(toksm3[5])*10)+"\n")

#			fout.write("$end")
	                        fout.write(newline1)
        	                fout.write(newline2)
	                        fout.write(newline3)
				fout.write("--\n0 1\n")
	                        fout.write(newline4)
	                        fout.write(newline5)
	                        fout.write(newline6)
                                fout.write("--\n0 1\n")
                                fout.write(newline7)
                                fout.write(newline8)
                                fout.write(newline9)
                                fout.write("$end\n\n@@@\n\n$rem\njobtype BSSE\nbasis 6-31+G*\nexchange omegab97X-D\nmax_scf_cycles 200\nSCF_convergence 6\n$end\n\n$molecule\n0 1\n--\n0 1\n")
                                fout.write(newline1)
                                fout.write(newline2)
                                fout.write(newline3)
                                fout.write("--\n0 1\n")
                                fout.write(newline4)
                                fout.write(newline5)
                                fout.write(newline6)
                                fout.write("$end\n\n@@@\n\n$rem\njobtype BSSE\nbasis 6-31+G*\nexchange omegab97X-D\nmax_scf_cycles 200\nSCF_convergence 6\n$end\n\n$molecule\n0 1\n--\n0 1\n")
                                fout.write(newline1)
                                fout.write(newline2)
                                fout.write(newline3)
                                fout.write("--\n0 1\n")
                                fout.write(newline7)
                                fout.write(newline8)
                                fout.write(newline9)
                                fout.write("$end\n\n@@@\n\n$rem\njobtype BSSE\nbasis 6-31+G*\nexchange omegab97X-D\nmax_scf_cycles 200\nSCF_convergence 6\n$end\n\n$molecule\n0 1\n--\n0 1\n")
                                fout.write(newline4)
                                fout.write(newline5)
                                fout.write(newline6)
                                fout.write("--\n0 1\n")
                                fout.write(newline7)
                                fout.write(newline8)
                                fout.write(newline9)
                                fout.write("$end\n\n@@@\n\n")
				fout.close()
	icount = icount + 31
fin.close()
