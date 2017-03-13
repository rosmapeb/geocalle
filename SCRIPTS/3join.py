import os
import arcpy
from arcpy import env

path = 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\SCINCE2010i' #Establece un directorio
lstFiles = []
lstDir = os.walk(path)   #Enlista los archivos del directorio path
for root, dirs, files in lstDir:    #PARECE QUE SOLO SIRVE files
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)    #Separa el nombre del archivo de su extensión
        if(extension == ".shp"):     #Realiza la acción solo si su extensión es .SHP
            lstFiles.append(nombreFichero+extension)   #Une de nuevo el nombre y extensión del archivo


#VALORES PARA JOIN
in_data = 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\C\SCINCE2010PobUnionDissCen.shp'
in_field = 'CVEGEO'
join_field = 'CVEGEO'

#print(in_data)
#print(in_field)
#print(join_field)

env.workspace = 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\SCINCE2010i'

for i in lstFiles:
  join_table = i
  print(join_table)
  opciones = {'CHCM_SCINCE2010Poblacion_UTM.shp': ['POB_1','POB_38','POB_41','POB_45','POB_46','POB_47','POB_55','POB_64','POB_67','POB_70','POB_71','POB_72','POB_80'],'CHCM_SCINCE2010Economia_UTM.shp':['ECO2','ECO3','ECO5','ECO6','ECO7','ECO10','ECO13','ECO16','ECO19','ECO22','ECO26','ECO27','ECO29','ECO30','ECO31','ECO34','ECO37','ECO40','ECO43'],'CHCM_SCINCE2010Educacion_UTM.shp': ['EDU1','EDU7','EDU13','EDU4','EDU10','EDU16','EDU25','EDU28','EDU31','EDU34','EDU37','EDU40'],'CHCM_SCINCE2010Discapacida_UTM.shp':['DISC2','DISC3','DISC4','DISC5','DISC6'], 'CHCM_SCINCE2010HogaresCensales_UTM.shp':['HOGAR2','HOGAR3','HOGAR7','HOGAR13','HOGAR19','HOGAR25'],'CHCM_SCINCE2010LenIndigena_UTM.shp': ['INDI19','INDI20'],'CHCM_SCINCE2010Migracion_UTM.shp':['MIG2','MIG3','MIG5','MIG6','MIG7'],'CHCM_SCINCE2010Religion_UTM.shp':['RELIG1','RELIG2','RELIG3','RELIG4'],'CHCM_SCINCE2010Salud_UTM.shp':['SALUD1','SALUD2'],'CHCM_SCINCE2010SitConyugal_UTM.shp':['SCONY1','SCONY4','SCONY7'],'CHCM_SCINCE2010Vivienda_UTM.shp':['VIV0','VIV1','VIV2']}
  #directory= 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\C\Cen' + join_table
  #print(directory)
  try:
    fields=opciones[join_table]
    print (fields)
    print('-----------')
    #print(in_data)
    #print(in_field)
    #print(join_field)
    #print('-----------')
    arcpy.JoinField_management (in_data, in_field, join_table, join_field, fields)
    #arcpy.CopyFeatures_management(joinprov,directory)
  except:
    print("ERROR-----------ERROR-----------")