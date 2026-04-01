#install.packages("ggplot2")
#install.packages("areaplot")
#install.packages("tidyr")

library(ggplot2)
library(areaplot)
library(tidyr)

team <- readline("Saisissez l'équipe que vous souhaitez analyser : ")

df_stats <- read.csv(paste("data/propre/statistiques_", team, ".csv", sep = ""))

df_stats$Saison <- factor(df_stats$Saison, 
                      levels = c("2010-2011", "2011-2012", "2012-2013", "2013-2014", 
                                 "2014-2015", "2015-2016", "2016-2017", "2017-2018", 
                                 "2018-2019", "2019-2020", "2020-2021", 
                                 "2021-2022", "2022-2023", "2023-2024", "2024-2025"),
                      ordered = TRUE)


ggplot(df_stats, aes(x = Saison)) + geom_line(aes(y = buts_marques_total, group = 1), linewidth = 1, colour = "red") + geom_line(aes(y = buts_marques_dom, group = 1), linewidth = 1, colour = "blue") + geom_line(aes(y = buts_marques_ext, group = 1), linewidth = 1, colour = "green") + labs(title = "Nombre de buts marqués (domicile et extérieur)", x = "Saisons", y = "Nombre total de Buts")

ggplot(df_stats, aes(x = Saison)) + geom_line(aes(y = buts_concedes_total, group = 1), linewidth = 1, colour = "red") + geom_line(aes(y = buts_concedes_dom, group = 1), linewidth = 1, colour = "blue") + geom_line(aes(y = buts_concedes_ext, group = 1), linewidth = 1, colour = "green") + labs(title = "Nombre de buts concédés (domicile et extérieur)", x = "Saisons", y = "Nombre total de Buts")

fautes <- data.frame(
  Saison = df_stats$Saison,
  Jaunes = df_stats$cartons_jaunes_neg_total,
  Rouges = df_stats$cartons_rouges_neg_total,
  Fautes = df_stats$fautes_causees_total
)
areaplot(fautes$Saison, fautes[, c("Jaunes", "Rouges")], xlab = "Saisons", ylab = "Fautes totales", main = "Répartition des cartons rouges par rapport aux jaunes", col = c("yellow", "red"))

ggplot(df_stats, aes(x = buts_concedes_total)) + geom_line(aes(y = fautes_causees_total, group = 1), linewidth = 1, colour = "red") + labs(title = "Nombre de fautes causées en fonction du nombre de buts concédés",x = "Nombre de buts concédés", y = "Nombre de fautes causées")

df_resultats <- pivot_longer(df_stats, cols = c(victoires, nuls, defaites), names_to = "Resultat", values_to = "Nombre")
ggplot(df_resultats, aes(x = Saison, y = Nombre, fill = Resultat)) + geom_bar(stat = "identity") + labs(title = "Résultats par saison (victoires, nuls, défaites)", x = "Saison", y = "Résultats")

df_tirs <- pivot_longer(df_stats, cols = c(tirs_total, tirs_cadres_total, buts_marques_total), names_to = "Stats_tirs", values_to = "Nombre_tirs")
ggplot(df_tirs, aes(x = Saison, y = Nombre_tirs, fill = Stats_tirs)) + geom_bar(stat = "identity") + labs(title = "Précision des tirs par saison", x = "Saison", y = "Précision des tirs")

df_fautes <- pivot_longer(df_stats, cols = c(fautes_causees_dom, fautes_causees_ext, fautes_causees_total), names_to = "Stats_fautes", values_to = "Nombre_fautes")
ggplot(df_fautes, aes(x = Saison, y = Nombre_fautes, fill = Stats_fautes)) + geom_bar(stat = "identity") + labs(title = "Répartions des fautes à domicile et à l'extérieur", x = "Saison", y = "Fautes")