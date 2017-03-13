# Name: 
# Description: OBTIENE CENTROIDES


import arcpy
from arcpy import env

env.workspace = "C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\B"

inFeatures = ["SCINCE2010_MznasCorr_UTM", "Buffer_mznaselGRAL"]
outFeatures = "C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\C\SCINCE2010PobUnion"

arcpy.Union_analysis (inFeatures, outFeatures,"ALL")
selani= arcpy.SelectLayerByAttribute_management ("SCINCE2010PobUnion", "NEW_SELECTION", "FID_buffer >= 0 ")
dissolves=arcpy.Dissolve_management(selani, "C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\C\SCINCE2010PobUnionDiss",["FID_buffer", "CVEGEO"], "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.FeatureToPoint_management (dissolves, "C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\C\SCINCE2010PobUnionDissCen", "INSIDE")