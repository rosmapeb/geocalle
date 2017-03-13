library(Hmisc)
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/D")
itable <- read.csv("pruebatabla.csv")
itable2<-replace(itable,itable=="99999","is.na")
attach(itable2)

##AUXILIARES
variable2<-as.numeric(EDU31)
promedio2<-tapply(variable2,FID_Buffer,mean,na.rm=TRUE)
variable3<-as.numeric(EDU34)
promedio3<-tapply(variable3,FID_Buffer,mean,na.rm=TRUE)
variable4<-as.numeric(EDU37)
promedio4<-tapply(variable4,FID_Buffer,mean,na.rm=TRUE)
#variable5<-as.numeric(ECO43)
#promedio5<-tapply(variable5,FID_Buffer,mean,na.rm=TRUE)
#variable6<-as.numeric(ECO19)
#promedio6<-tapply(variable6,FID_Buffer,mean,na.rm=TRUE)

##VARIABLE
variable<-as.numeric(EDU40)
promedio<-tapply(variable,FID_Buffer,mean,na.rm=TRUE)
promround<-round( promedio, 2 )
desvest<-tapply(variable,FID_Buffer,sd,na.rm=TRUE)
maxi<-tapply(variable,FID_Buffer,max,na.rm=TRUE)
mini<-tapply(variable,FID_Buffer,min,na.rm=TRUE)
limitesup=promedio+desvest

##NOMBRE ARCHIVO
png("Educacion.png")

plot(promedio, type= 'l',ylim=c(min(mini,na.rm=TRUE),max(limitesup,na.rm=TRUE)))  #Grafica el promedio con límites de max y min de la variable 

#lines(maxi, type="o", lty=2, col="gray") #Agrega lineas de máximo y mínimo valor
#lines(mini, lty=2, col="gray")

##AUXILIARES
lines(promedio2, lty=2, col="blue")
lines(promedio3, lty=3, col="red")
lines(promedio4, lty=4, col="grey")
#lines(promedio5, lty=5, col="green")
#lines(promedio6, lty=6, col="deeppink4")

## TITULO
title(main="Educacion", col.main="black", font.main=1) #xlab="Area de influencia (metros)")
#title(xlab="Area de influencia (metros)", col.lab="black")


anillos<-c(1,2,3,4,5)
#anillos<-c(99.95,199.90,299.85,399.80,499.75)
#anillos<-c(37.28,74.56,111.84,149.11,186.39)

errbar( anillos, promedio, promedio+desvest, promedio-promedio,add=TRUE)
text(anillos, promedio, promround, cex=0.7, pos=1, col="red")
legend("topleft", c("EDU31", "EDU34", "EDU37", "EDU40"), cex=0.8, col=c("blue", "red", "grey","black"),pch=21:22, lty=1:2)
#text(promedio2, c("POB_38"), cex=0.7, pos=1, col="red")

dev.off()
