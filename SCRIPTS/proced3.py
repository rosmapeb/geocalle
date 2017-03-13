import arcpy
from arcpy import env
fieldList= arcpy.ListFields('C:\CartoMaestria\Ejercicio\CaracterizacionPMA\F_inter\C\SCINCE2010PobUnionDissCen.shp')
fc= 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\F_inter\C\SCINCE2010PobUnionDissCen.shp'


lista=[]
for field in fieldList:
    fieldname=field.name
    lista.append(fieldname)
cursor = arcpy.UpdateCursor(fc,lista)
for row in cursor:
    for field in lista:
        if row.getValue(field) == -6:
            row.setValue(field,99999)
            cursor.updateRow(row)
        if row.getValue(field) == -9:
            row.setValue(field,99999)
            cursor.updateRow(row)              
        if row.getValue(field) == -8:
            row.setValue(field,99999)
            cursor.updateRow(row) 			
del row
del cursor



fc= 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\F_inter\C\SCINCE2010PobUnionDissCen.shp'
field2=['EDU1','EDU4','EDU7','EDU10','EDU13','EDU16','POB_46','POB_47','POB_71','POB_72']
cursor3 =  arcpy.UpdateCursor(fc,field2)
for row in cursor3:
    for field in field2:
        #print(field)
        if row.getValue(field) == 0:
            row.setValue(field,100000000)
            cursor3.updateRow(row)
del row
del cursor3



intable = 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\F_inter\C\SCINCE2010PobUnionDissCen.shp'
arcpy.AddField_management(intable,'POB4647','LONG',10,'','','','NULLABLE')
arcpy.AddField_management(intable,'POB7172','LONG',10,'','','','NULLABLE')
arcpy.AddField_management(intable,'EDU1713','LONG',10,'','','','NULLABLE')
arcpy.AddField_management(intable,'EDU41016','LONG',10,'','','','NULLABLE')
arcpy.CalculateField_management(intable,'POB4647','!POB_46!+!POB_47!','PYTHON','')
arcpy.CalculateField_management(intable,'POB7172','!POB_71!+!POB_72!','PYTHON','')
arcpy.CalculateField_management(intable,'EDU1713','!EDU1!+!EDU7!+!EDU13!','PYTHON','')
arcpy.CalculateField_management(intable,'EDU41016','!EDU4!+!EDU10!+!EDU16!','PYTHON','')



fc= 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\F_inter\C\SCINCE2010PobUnionDissCen.shp'
upfield=['POB4647','POB7172']
cursor2 = arcpy.UpdateCursor(fc,upfield)
for row in cursor2:
    for field in upfield:
        if row.getValue(field) >= 100099999:
            row.setValue(field,0)
            cursor2.updateRow(row) 
        while row.getValue(field) > 100000000 and row.getValue(field) < 100099999:
            resta=row.getValue(field)-100000000
            row.setValue(field,resta)
            cursor2.updateRow(row)
        while row.getValue(field) > 99999 and row.getValue(field) <= 299997:
            resta=row.getValue(field)-99999
            row.setValue(field,resta)
            cursor2.updateRow(row) 
del row
del cursor2



fc= 'C:\CartoMaestria\Ejercicio\CaracterizacionPMA\F_inter\C\SCINCE2010PobUnionDissCen.shp'
upofield=['EDU1713','EDU41016']
cursor4 = arcpy.UpdateCursor(fc,upofield)
for row in cursor4:
    for field in upofield:
        if row.getValue(field) == 300000000:
            row.setValue(field,0)
            cursor4.updateRow(row)
        if row.getValue(field) == 200099999:
            row.setValue(field,0)
            cursor4.updateRow(row)
        if row.getValue(field) == 100199998:
            row.setValue(field,0)
            cursor4.updateRow(row)
        while row.getValue(field) > 100000000 and row.getValue(field) < 200099999:
            resta2=row.getValue(field)-100000000
            row.setValue(field,resta2)
            cursor4.updateRow(row)
        while row.getValue(field) > 99999 and row.getValue(field) <= 299997:
            resta3=row.getValue(field)-99999
            row.setValue(field,resta3)
            cursor4.updateRow(row) 
del row
del cursor4
