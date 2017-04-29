import arcpy
from dbfpy import dbf
import sys
import csv

arcpy.env.workspace = r"c:\OLS"

listavariables=['i_CCULTURA','i_ESCUELA','i_IGLESIA','e_Avenida','cl_LineaMe','d_CMAdequi','d_CMEdotro','d_CMEdbici','d_CMEdinst','d_CMEentie','d_CMEdrevi','d_CMEdart_','d_Ventadbi','s_EDU51_R','s_MIG2','i_cp_Plaza']

def potencia(c): #Calcula y devuelve el conjunto potencia del conjunto c
    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

solucion= potencia(listavariables)
longitud= len(solucion)
soluciontxt=str(solucion)

fo = open("C:/OLS/modelos2.txt", "wb")
fo.write(soluciontxt)
fo.close()

listModel=[]
listModelMoran=[]

for i in range (3767,17181):
	print("MODELO:",i,solucion[i])
	coeficientes=[]
	str1 = ''.join(solucion[i])
	Coef="C" + str1 + ".dbf"
	Diag="D" + str1 + ".dbf"
	ii=str(i)
	OutputOLS="OLS" + ii
	OutputOLSMoran='c:/OLS/'+OutputOLS+'.shp'
	OLStat=arcpy.OrdinaryLeastSquares_stats('c:/OLS/Mznas_FinalVar_ARC.shp','id', OutputOLS, 'i_Counter', solucion[i], Coef,Diag)
	D1 = 'c:/OLS/'+Diag
	Dbf1 = dbf.Dbf(D1)
	C1 = 'c:/OLS/'+Coef
	Cbf1 = dbf.Dbf(C1)
	#print ("(3)¿Las variables explicativas tienen coeficientes estadísticamente significativos?")
	kroenker=Dbf1[8]
	probkroenker=kroenker[2]
	jb=Dbf1[10]
	probjb=jb[2]
	r2a=Dbf1[2]
	vr2a=r2a[2]
	aicc=Dbf1[1]
	vaicc=aicc[2]
	NumCoeff=len(Cbf1)
	NumDiagn=len(Dbf1)
	countp=0
	countpr=0
	for k in range (0,NumCoeff):
		variable=Cbf1[k]
		var_coefi=variable[2]
		prob=variable[5]
		probRob=variable[8]
		coeficientes.append(var_coefi)
		if prob <= 0.05:
			countp=1+countp
		if  probRob <= 0.05:
			countpr=1+countpr
	print("¿Se satisface la probabilidad?")
	if countp == k+1:
		print("¿Se satisface la probabilidad robusta?")
		if  countpr == k+1:
			#print("(4) ¿La prueba de Jarque-Bera NO sea estadísticamente significativa?")
			#if probjb >= 0.05:
			print("(5) ¿Hay rendimiento del modelo?")
			if vr2a > .5:
				listModel.append("MODELO:",solucion[i],"MORAN PVALUE:", pValue,"VALORES COEFICIENTES:",coeficientes,"PROBABILIDAD:",prob,"PROBABILIDAD ROBUSTA:",probRob,"KROENKER:", probkroenker,"JB:",probjb,"R2ADJ:",vr2a,"AICC:",vaicc)
				print ("(6)¿El modelo de residuos está libre de autocorrelación espacial?")
				Moran=arcpy.SpatialAutocorrelation_stats (OutputOLSMoran, 'StdResid', 'NO_REPORT', 'INVERSE_DISTANCE', 'EUCLIDEAN_DISTANCE','ROW', '', '')
				#MoranIndex=float(Moran[0])
				##Zscore=float(Moran[1])
				pValue=float(Moran[2])
				if pValue >= 0.05:
					print("ES UN MODELO VÁLIDO")
					print ("(1)¿La variable explicativa tiene la relación que esperamos?")
					print(coeficientes)
					listModelMoran.append("MODELO:",solucion[i],"MORAN PVALUE:", pValue,"VALORES COEFICIENTES:",coeficientes,"PROBABILIDAD:",prob,"PROBABILIDAD ROBUSTA:",probRob,"KROENKER:", probkroenker,"JB:",probjb,"R2ADJ:",vr2a,"AICC:",vaicc)
				else:
					print("NO")
					print("-----------------------------")
			else:
					print("NO")
					print("-----------------------------")
			#else:
			#	print("NO")
			#	print("-----------------------------")
		else:
			print("NO")
			print("-----------------------------")
	else:
		print("NO")
		print("-----------------------------")
