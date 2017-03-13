library(Hmisc)
library(Rcmdr)

########### ~~~ DATA INPUT ~~~ ###########
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/B_sleep/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/C_eat/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/D_hangout/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/E_earn/D")
#setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/F_inter/D")
itable <- read.csv("pruebatabla.csv")
nombres <- read.csv("namesinegi.csv")

########### ~~~ PREPARATION DATA ~~~ ###########
itable<-replace(itable,itable=="99999","is.na")
itable<-replace(itable,itable=="100000000","is.na")
tam<-dim(itable)
output <- matrix(unlist(itable), nrow=tam[1], ncol =tam[2], byrow = FALSE)
FID_Buffer<-as.numeric(output[,4])
output <- output[,6:92]
n<-nombres$geografico
subn<-nombres$clave
metros<-c("99.95","199.9","299.85","399.8","499.75")
ext<-c("png")
tamM<-dim(output)
M <- matrix(nrow=tamM[2], ncol =5)

########### ~~~ LOOP ~~~ ###########
for (i in 1:length(n))
{
  #PREPARA NOMBRE DEL ARCHIVO
  file<-as.character(n[i])
  union <- paste(file,ext,sep=".")
  png(union)
  #PREPARA DATOS
  data <- as.numeric(output[,i])
  promedio<-tapply(data,FID_Buffer,mean,na.rm=TRUE)
  promround<-round(promedio, 2)
  desvest<-tapply(data,FID_Buffer,sd,na.rm=TRUE)
  maxi<-tapply(data,FID_Buffer,max,na.rm=TRUE)
  mini<-tapply(data,FID_Buffer,min,na.rm=TRUE)
  limitesup=promedio+desvest
  #TABLA
  for (j in 1:length(promedio))
  {
    M[i,j]<-(promround[j])
  }
  #GRAFICA
  plot(promedio, type= 'l')#,ylim=c(min(mini,na.rm=TRUE),max(limitesup,na.rm=TRUE)))
  lines(maxi, type="o", lty=2, col="gray")
  lines(mini, lty=2, col="gray")
  anillos<-c(1,2,3,4,5)
  #errbar( anillos, promedio, promedio+desvest, promedio-promedio,add=TRUE)
  #FORMATO GRAFICA
  title(main=n[i], col.main="black", font.main=1, sub=subn[i])
  text(anillos, promedio, promround, cex=0.7, pos=1, col="red")
  #LIBERA GRAFICO
  dev.off()
  print (i)
}

ftable<-data.frame(n,M)
write.csv(ftable, "scinceprom.csv")
