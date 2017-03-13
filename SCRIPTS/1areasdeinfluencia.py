# Name: MultipleRingBuffer_Example2.py
# Description: CREA 5 AREAS DE INFLUENCIA SEGUN EL PERIMETRO DADO
  
 # Import system modules
import arcpy
from arcpy import env
 # Set environment settings
env.workspace = "C:\CartoMaestria\CHCM_UTM\CHCM_PuntosReunion\CHCM_PR1996vector"


 # Set local variables
inFeatures = "CHCM_PR2014_VyN_UTM_perim"
outFeatureClass = "C:\CartoMaestria\Ejercicio\CaracterizacionPMA\A_gral\B\Buffer_mznaselGRAL" #"buffer_mznaall"
#distances = [37.27838,74.55676,111.83514,149.11352,186.3919] #seleccionadas 
distances = [99.94967,199.89934,299.84901,399.79868,499.74836] #todas 
bufferUnit = "meters"
#FieldName="PeriP/4*5"


# Execute MultipleRingBuffer
arcpy.MultipleRingBuffer_analysis(inFeatures, outFeatureClass, distances, bufferUnit,"","ALL")

arcpy.CalculateField_management(Buffer_mznaselGRAL,"FID", "!FID+1!")
