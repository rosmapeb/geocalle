library(Hmisc)
library(Rcmdr)

setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_DENUE/Sector dividido/Pendientes")
itable <- read.csv("Actividades.csv")

#InformacionComplementariaPoly
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_CartografiaUrbanaINEGI/InformacionComplementariaPoly")
itable <- read.csv("poly4pend.csv")
#Ejes Viales
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_CartografiaUrbanaINEGI/EjesViales")
itable <- read.csv("ejesV4pend.csv")
#InformacionComplementariaL
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_CartografiaUrbanaINEGI/InformacionComplementariaL")
itable <- read.csv("infoL4pend.csv")
#InformacionComplementariaP
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_CartografiaUrbanaINEGI/InformacionComplementariaP")
itable <- read.csv("infoP4pend.csv")
#INFO INFRAESTRUCTURA
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_Carto_INEGI")
itable <- read.csv("infra4pend.csv")
#INFO ESTADISTICA SCINCE
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/D")
itable <- read.csv("scinceprom.csv")

sizet<-dim(itable)
itable[is.na(itable)]<-0
attach(itable)

itable<-itable[,2:length(itable)]
A1<-itable$X1
A2<-itable$X2
A3<-itable$X3
A4<-itable$X4
A5<-itable$X5
M <- matrix(nrow=sizet[1], ncol = 1)

m12<-(A2-A1)/99.95
m23<-(A3-A2)/99.95
m34<-(A4-A3)/99.95
m45<-(A5-A4)/99.95

for (i in 1:sizet[1])
{
  fvector<-c(m12[i],m23[i],m34[i],m45[i])
  mprom<-mean(fvector)
  M[i]<-(mprom)
}

ftable<-data.frame(clave,actividades,m12,m23,m34,m45,M)
ftable<-data.frame(itable$n,m12,m23,m34,m45,M)

write.csv(ftable, "pendientes.csv")