#! /usr/bin/Rscript --vanilla

library(readr)
library(dplyr) # to use  %>% notation
library(scatterplot3d)
#install.packages("plyr")
#install.packages("reshape2")
library(ggplot2)
library(plot3D)

library(plyr)
library(reshape2)


#------------------------------------------------
#init workspace
#------------------------------------------------
rm(list=ls())

#------------------------------------------------
# Reading file
#------------------------------------------------
#f <- file.choose(new = FALSE)
f <- "result.csv"
data <- read_csv(file = f)

d <- data %>%
  filter(resultConcerns=="m1Results")

val <- (d$makespan/d$m1Optimal)  # value
job <- d$n         # x
proc<- d$m        # Y
algo<- d$algoName[1]

#------------------------------------------------
# to save Draw in pdf file (vector)
#------------------------------------------------
name <- algo
ext <- ".pdf"
n <- paste(name,"_n_m_variable_3d",ext) 

pdf(file=n)


#------------------------------------------------
# Draw the graph
#------------------------------------------------
p <- scatter3D(x=job,y=proc,z=val, 
              colvar = val, 
              bty = "b2",          # “b”, “b2”, “f”, “g”, “bl”, “bl2”, “u”, “n”
              type = "h",          # l (lines) h (sticks) b ()
              ticktype = "detailed", 
              lwd = 4,
              colkey = TRUE, 
              main =algo,
              pch = 19,  
              theta = 30, 
              phi = 30, 
              xlab = "jobs numbers",
              ylab ="machines number", 
              zlab = "nomalized makespan Cmax/Optimal"
)

#------------------------------------------------
# save the file
#------------------------------------------------
dev.off()

#------------------------------------------------
# doesn't work
#------------------------------------------------
#surface <- reshape2::melt(d)
#p <- ggplot(d, aes(x=job, y=proc, z=val)) +geom_point()
#p + stat_contour(geom="polygon", aes(fill=..level..))
#  geom_bin2d(bins=10)
#  stat_contour(geom="polygon", aes(fill=..level..))
#  stat_contour(geom="polygon", aes(fill=..level..))
#stat_density2d(geom="polygon", aes(fill = ..level..))
#geom_contour_filled() +
#geom_contour(color = "black", size = 0.1)
#         expand =1.5
#         col.panel ="steelblue", 
#         col.grid = "darkblue") 


