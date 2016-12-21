setwd("/home/kaihami/Desktop/Python/RR_Bioinfo/Seq_RR/Total_RR/")

x <- read.table('Total.csv', header = TRUE, sep = ",")
library("ggplot2")
bac <- x[,2]; Domain <- x[,4]; Phylum <- x[,3]
data <- log(x[,c(5:length(x))])

data[mapply(is.infinite, data)] <- 0
data[mapply(is.na, data)] <- 0

CDS <- data[,1]; REC <- data[,2];DNA_binding <- data[,9]; RNA_binding <- data[,11]
cdiGMP <- data[,16]; enzymatic <- data[,20]; total <- data[,23]

data_total <- data.frame(bac, Phylum, Domain, CDS, total)

data_bac = subset(data_total, Domain == "Bacteria")

data_arc <- subset(data_total, Domain == "Archaea")

data_rec <- data.frame(bac, Phylum, Domain, CDS, REC,total)

data_rec_sub <- subset(data_rec, REC >0)

#model (Total)
modlinear <- lm(data_total$total ~ data_total$CDS)
xmin <- min(CDS)
xmax <- max(CDS)
predicted <- data.frame(CDS=seq(xmin, xmax, length.out=length(CDS)))
predicted$logTotalRR2 <- predict(modlinear, predicted)

predicted.sub <- subset(predicted, logTotalRR2 >0)

#Total
lab <- format(summary(modlinear)$r.squared, digits = 3)
a <- ggplot(data_total, aes(x = CDS, y = total))+
  geom_point(size=3.2, alpha = 0.4, colour = "cadetblue4") +
  theme_bw()+theme(axis.line = element_line(colour = "black"),
                   panel.grid.major = element_blank(),
                   panel.grid.minor = element_blank(),
                   panel.border = element_blank(),
                   panel.background = element_blank(),
                   legend.title=element_blank(),
                   legend.key=element_blank()) + #sem O titulo da legenda
  labs(y = "RR", x = "CDS")+
  geom_abline(intercept = -11.51695, slope = 1.80829)+
  annotate("text", x = 6.5, y = 3, label = "R² = 0.683")

#Mod Bact
modlinearbac <- lm(data_bac$total ~ data_bac$CDS)
xmin2 <- min(data_bac$CDS)
xmax2 <- max(data_bac$CDS)
predictedbac <- data.frame(CDS=seq(xmin2, xmax2, length.out=length(data_bac$CDS)))
predictedbac$logTotalRR2 <- predict(modlinearbac, predictedbac)

predictedbac.sub <- subset(predictedbac, logTotalRR2 >0)
#Bac
ggplot(data_bac, aes(x = data_bac$CDS, y = data_bac$total))+
  geom_point(size=3.2, alpha = 0.4, colour = "coral3") +
  theme_bw()+theme(axis.line = element_line(colour = "black"),
                   panel.grid.major = element_blank(),
                   panel.grid.minor = element_blank(),
                   panel.border = element_blank(),
                   panel.background = element_blank(),
                   legend.title=element_blank(),
                   legend.key=element_blank()) + #sem O titulo da legenda
  labs(y = "RR", x = "CDS")+
  geom_abline(intercept = -10.62686, slope = 1.72812)+
  annotate("text", x = 6.5, y = 3, label = "R² = 0.779")

#Save pic as 1062, 524

#Mod Arc
modlineararc <- lm(data_arc$total ~ data_arc$CDS)
xmin3 <- min(data_arc$CDS)
xmax3 <- max(data_arc$CDS)
predictedbac <- data.frame(CDS=seq(xmin3, xmax3, length.out=length(data_arc$CDS)))
predictedbac$logTotalRR2 <- predict(modlineararc, predictedar)

predictedarc.sub <- subset(predictedarc, logTotalRR2 >0)
#Arc
ggplot(data_arc, aes(x = data_arc$CDS, y = data_arc$total))+
  geom_point(size=3.2, alpha = 0.4, colour = "coral3") +
  theme_bw()+theme(axis.line = element_line(colour = "black"),
                   panel.grid.major = element_blank(),
                   panel.grid.minor = element_blank(),
                   panel.border = element_blank(),
                   panel.background = element_blank(),
                   legend.title=element_blank(),
                   legend.key=element_blank()) + #sem O titulo da legenda
  labs(y = "RR", x = "CDS")+
  geom_abline(intercept = -16.9369, slope = 2.3528)+
  annotate("text", x = 6.5, y = 3, label = "R² = 0.4114")

#Mod Rec
modlinearREC <- lm(data_rec$REC ~ data_rec$total)
xmin3 <- min(data_arc$CDS)
xmax3 <- max(data_arc$CDS)
predictedbac <- data.frame(CDS=seq(xmin3, xmax3, length.out=length(data_arc$CDS)))
predictedbac$logTotalRR2 <- predict(modlineararc, predictedar)

predictedarc.sub <- subset(predictedarc, logTotalRR2 >0)
#REC
ggplot(data_rec, aes(x = data_rec$total, y = data_rec$REC))+
  geom_point(size=3.2, alpha = 0.4, colour = "coral3") +
  theme_bw()+theme(axis.line = element_line(colour = "black"),
                   panel.grid.major = element_blank(),
                   panel.grid.minor = element_blank(),
                   panel.border = element_blank(),
                   panel.background = element_blank(),
                   legend.title=element_blank(),
                   legend.key=element_blank()) + #sem O titulo da legenda
  labs(y = "REC", x = "Total RR")+
  geom_abline(intercept = -0.60579, slope = 0.56828)+
  annotate("text", x = 1, y = 3, label = "R² = 0.5102")

