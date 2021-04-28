#! /usr/bin/Rscript --vanilla

library(readr)
library(dplyr) # to use  %>% notation
library(ggplot2)

#------------------------------------------------
# Reading file
#------------------------------------------------
#f <- file.choose(new = FALSE)
f <- "result.csv"
data <- read_csv(file = f)
nf<- factor(d$n) # for boxPlot

d <- data %>%
  filter(resultConcerns=="Results")

#------------------------------------------------
# Draw the graph
#------------------------------------------------
d %>%
  # filter(resultConcerns=="m1Results") %>%
  ggplot(aes(x = nf, y = (makespan/LowBound), color=algoName, shape=algoName))+
  geom_boxplot()+
  facet_grid(d$m ~ d$generateMethode)
labs(
  title = "Comparaison",
  y = "Makespan normalisé Cmax-optimal"
)
ggsave(file = "res_boxPlot_nVariable_nat.pdf")

