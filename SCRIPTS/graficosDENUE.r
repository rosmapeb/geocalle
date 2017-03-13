#TABLA denue filter.csv <-> Contiene los valores de cada variable en sentido vertical, y los nombres
#                           de los campos son cada variable, es decir cada columna es una variable y
#                           cada una de sus filas el valor de cada area de influencia
#TABLA names.csv        <-> Contiene los nombres de cada variable, o los nombres de cada campo de
#                           denue filter.csv. Estos se acomodan en una columna y cada fila es un nombre.
#                           El nombre de la columna debe ser "nombre"

library(Hmisc)
setwd("C:/CartoMaestria/Ejercicio/CaracterizacionPMA/A_gral/E_DENUE/Sector dividido/K1K2-TLC")
itable <- read.csv("denue filterK1K2TLC.csv")
#itable<-replace(itable,itable=="NA","0")
itable[is.na(itable)]<-0
nombres <- read.csv("namesK1K2TLC.csv")
output <- matrix(unlist(itable), nrow=5, ncol = 588, byrow = FALSE)
n<-nombres$nombre
metros<-c("99.95","199.9","299.85","399.8","499.75")
ext<-c("png")


for (i in 1:length(n))
{
  file<-as.character(n[i])
  union <- paste(file,ext,sep=".")
  png(union)
  print (i)
  #print (n[i])
  #print (output[,i])
  data <- output[,i]
  plot(metros,data,type= 'l',ylim=c(min(0,na.rm=TRUE),max(max(output[,i]),na.rm=TRUE)))
  text(metros, data, data, cex=0.7, pos=1, col="red")
  title(n[i])
  dev.off()
}

#SALVAR COMANDOS
#substring(h, 1,21)<-t SUSTITUYE PARTE DE UN TEXTO
#sub(" +$", "", h)    QUITA ESPACIOS EN BLANCO