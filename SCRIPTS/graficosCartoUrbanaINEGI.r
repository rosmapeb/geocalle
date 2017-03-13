library(Hmisc)
library(Rcmdr)
#setwd("C:/CartoMaestria/Ejercicio/CartografiaUrbanaINEGI/InformacionComplementariaPoly")
#itable <- read.csv("InfoComplemPoly.csv")

#setwd("C:/CartoMaestria/Ejercicio/CartografiaUrbanaINEGI/InformacionComplementariaP")
#itable <- read.csv("InfoComplemP.csv")

#setwd("C:/CartoMaestria/Ejercicio/CartografiaUrbanaINEGI/EjesViales")
#itable <- read.csv("EjesViales.csv")

setwd("C:/CartoMaestria/Ejercicio/CartografiaUrbanaINEGI/InformacionComplementariaL")
itable <- read.csv("InfoComplemL.csv")

itable[is.na(itable)]<-0
nombres <- read.csv("namesinegi.csv")
tam<-dim(itable)
output <- matrix(unlist(itable), nrow=tam[1], ncol =tam[2], byrow = FALSE)
n<-nombres$geografico
metros<-c("99.95","199.9","299.85","399.8","499.75")
ext<-c("png")

for (i in 1:length(n))
{
  file<-as.character(n[i])
  union <- paste(file,ext,sep=".")
  png(union)
  print (i)
  data <- output[,i]
  plot(metros,data,type= 'l')
  title(n[i])
  dev.off()
}