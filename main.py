import pandas as pd


saison_1011 = pd.read_csv("data/brute/season-1011.csv")
saison_1112 = pd.read_csv("data/brute/season-1112.csv")
saison_1213 = pd.read_csv("data/brute/season-1213.csv")
saison_1314 = pd.read_csv("data/brute/season-1314.csv")
saison_1415 = pd.read_csv("data/brute/season-1415.csv")
saison_1516 = pd.read_csv("data/brute/season-1516.csv")
saison_1617 = pd.read_csv("data/brute/season-1617.csv")
saison_1718 = pd.read_csv("data/brute/season-1718.csv")
saison_1819 = pd.read_csv("data/brute/season-1819.csv")
saison_1920 = pd.read_csv("data/brute/season-1920.csv")
saison_2021 = pd.read_csv("data/brute/season-2021.csv")
saison_2122 = pd.read_csv("data/brute/season-2122.csv")
saison_2223 = pd.read_csv("data/brute/season-2223.csv")
saison_2324 = pd.read_csv("data/brute/season-2324.csv")
saison_2425 = pd.read_csv("data/brute/season-2425.csv")

saisons = (saison_1011, saison_1112, saison_1213, saison_1314, saison_1415, saison_1516, saison_1617, saison_1718, saison_1819, saison_1920, saison_2021, saison_2122, saison_2223, saison_2324, saison_2425)

saisons_key = ("2010-2011", "2011-2012", "2012-2013", "2013-2014", "2014-2015", "2015-2016", "2016-2017", "2017-2018", "2018-2019", "2019-2020", "2020-2021", "2021-2022", "2022-2023", "2023-2024", "2024-2025")

team = input("Saisissez l'équipe que vous souhaitez analyser : ")

stats = []

for saison_key in saisons_key:
    stats.append({
        "Saison": saison_key,
        "buts_marques_dom": 0,
        "buts_marques_ext": 0,
        "buts_marques_total": 0,
        "buts_concedes_dom": 0,
        "buts_concedes_ext": 0,
        "buts_concedes_total": 0,
        "tirs_dom": 0,
        "tirs_ext": 0,
        "tirs_total": 0,
        "tirs_cadres_dom": 0,
        "tirs_cadres_ext": 0,
        "tirs_cadres_total": 0,
        "fautes_causees_dom": 0,
        "fautes_causees_ext": 0,
        "fautes_causees_total": 0,
        "fautes_subies_dom": 0,
        "fautes_subies_ext": 0,
        "fautes_subies_total": 0,
        "cartons_jaunes_neg_dom": 0,
        "cartons_jaunes_neg_ext": 0,
        "cartons_jaunes_neg_total": 0,
        "cartons_rouges_neg_dom": 0,
        "cartons_rouges_neg_ext": 0,
        "cartons_rouges_neg_total": 0,
        "cartons_jaunes_pos_dom": 0,
        "cartons_jaunes_pos_ext": 0,
        "cartons_jaunes_pos_total": 0,
        "cartons_rouges_pos_dom": 0,
        "cartons_rouges_pos_ext": 0,
        "cartons_rouges_pos_total": 0,
        "victoires": 0,
        "nuls": 0,
        "defaites": 0
    })

compteur_saison = 0

for saison in saisons:
    for i in range(len(saison)):
        if saison["HomeTeam"][i] == team:
            stats[compteur_saison]["buts_marques_dom"] += saison["FTHG"][i]
            stats[compteur_saison]["buts_concedes_dom"] += saison["FTAG"][i]
            stats[compteur_saison]["tirs_dom"] += saison["HS"][i]
            stats[compteur_saison]["tirs_cadres_dom"] += saison["HST"][i]
            stats[compteur_saison]["fautes_causees_dom"] += saison["HF"][i]
            stats[compteur_saison]["fautes_subies_dom"] += saison["AF"][i]
            stats[compteur_saison]["cartons_jaunes_neg_dom"] += saison["HY"][i]
            stats[compteur_saison]["cartons_rouges_neg_dom"] += saison["HR"][i]
            stats[compteur_saison]["cartons_jaunes_pos_dom"] += saison["AY"][i]
            stats[compteur_saison]["cartons_rouges_pos_dom"] += saison["AR"][i]

            if saison["FTR"][i] == "H":
                stats[compteur_saison]["victoires"] += 1
            elif saison["FTR"][i] == "D":
                stats[compteur_saison]["nuls"] += 1
            else:
                stats[compteur_saison]["defaites"] += 1
        
        elif saison["AwayTeam"][i] == team:
            stats[compteur_saison]["buts_marques_ext"] += saison["FTAG"][i]
            stats[compteur_saison]["buts_concedes_ext"] += saison["FTHG"][i]
            stats[compteur_saison]["tirs_ext"] += saison["AS"][i]
            stats[compteur_saison]["tirs_cadres_ext"] += saison["AST"][i]
            stats[compteur_saison]["fautes_causees_ext"] += saison["AF"][i]
            stats[compteur_saison]["fautes_subies_ext"] += saison["HF"][i]
            stats[compteur_saison]["cartons_jaunes_neg_ext"] += saison["AY"][i]
            stats[compteur_saison]["cartons_rouges_neg_ext"] += saison["AR"][i]
            stats[compteur_saison]["cartons_jaunes_pos_ext"] += saison["HY"][i]
            stats[compteur_saison]["cartons_rouges_pos_ext"] += saison["HR"][i]

            if saison["FTR"][i] == "A":
                stats[compteur_saison]["victoires"] += 1
            elif saison["FTR"][i] == "D":
                stats[compteur_saison]["nuls"] += 1
            else:
                stats[compteur_saison]["defaites"] += 1
        
    stats[compteur_saison]["buts_marques_total"] = stats[compteur_saison]["buts_marques_dom"] + stats[compteur_saison]["buts_marques_ext"]
    stats[compteur_saison]["buts_concedes_total"] = stats[compteur_saison]["buts_concedes_dom"] + stats[compteur_saison]["buts_concedes_ext"]
    stats[compteur_saison]["tirs_total"] = stats[compteur_saison]["tirs_dom"] + stats[compteur_saison]["tirs_ext"]
    stats[compteur_saison]["tirs_cadres_total"] = stats[compteur_saison]["tirs_cadres_dom"] + stats[compteur_saison]["tirs_cadres_ext"]
    stats[compteur_saison]["fautes_causees_total"] = stats[compteur_saison]["fautes_causees_dom"] + stats[compteur_saison]["fautes_causees_ext"]
    stats[compteur_saison]["fautes_subies_total"] = stats[compteur_saison]["fautes_subies_dom"] + stats[compteur_saison]["fautes_subies_ext"]
    stats[compteur_saison]["cartons_jaunes_neg_total"] = stats[compteur_saison]["cartons_jaunes_neg_dom"] + stats[compteur_saison]["cartons_jaunes_neg_ext"]
    stats[compteur_saison]["cartons_rouges_neg_total"] = stats[compteur_saison]["cartons_rouges_neg_dom"] + stats[compteur_saison]["cartons_rouges_neg_ext"]
    stats[compteur_saison]["cartons_jaunes_pos_total"] = stats[compteur_saison]["cartons_jaunes_pos_dom"] + stats[compteur_saison]["cartons_jaunes_pos_ext"]
    stats[compteur_saison]["cartons_rouges_pos_total"] = stats[compteur_saison]["cartons_rouges_pos_dom"] + stats[compteur_saison]["cartons_rouges_pos_ext"]

    compteur_saison += 1

df_stats = pd.DataFrame(stats)

file_name = "statistiques_" + team

df_stats.to_csv("data/propre/" + file_name + ".csv")