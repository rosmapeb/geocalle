library(Hmisc)
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/B_sleep/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/C_eat/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/D_hangout/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/E_earn/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/F_inter/D")
itable <- read.csv("pruebatabla.csv")
itable2<-replace(itable,itable=="99999","is.na")
attach(itable2)

##VARIABLE
variable<-as.numeric(INDI16)
promedio<-tapply(variable,FID_Buffer,mean,na.rm=TRUE)
promround<-round( promedio, 2 )
desvest<-tapply(variable,FID_Buffer,sd,na.rm=TRUE)
maxi<-tapply(variable,FID_Buffer,max,na.rm=TRUE)
mini<-tapply(variable,FID_Buffer,min,na.rm=TRUE)
limitesup=promedio+desvest

##NOMBRE ARCHIVO
png("Poblacion de 5 años y mas que habla alguna lengua indigena y habla español.png")

plot(promedio, type= 'l',ylim=c(min(mini,na.rm=TRUE),max(limitesup,na.rm=TRUE)))  #Grafica el promedio con límites de max y min de la variable 

lines(maxi, type="o", lty=2, col="gray") #Agrega lineas de máximo y mínimo valor
lines(mini, lty=2, col="gray")


## TITULO
title(main="INDI16 : Poblacion de 5 años y mas que habla alguna lengua indigena y habla español", col.main="black", font.main=1) #xlab="Area de influencia (metros)")
#title(xlab="Area de influencia (metros)", col.lab="black")
     

anillos<-c(1,2,3,4,5)
#anillos<-c(99.95,199.90,299.85,399.80,499.75)
#anillos<-c(37.28,74.56,111.84,149.11,186.39)

errbar( anillos, promedio, promedio+desvest, promedio-promedio,add=TRUE)
text(anillos, promedio, promround, cex=0.7, pos=1, col="red")
#text(promedio2, c("POB_38"), cex=0.7, pos=1, col="red")

dev.off()

