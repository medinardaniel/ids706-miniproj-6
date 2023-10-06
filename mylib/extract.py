"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests
import pandas as pd
import io

def extract(url1="https://raw.githubusercontent.com/datasets/football-datasets/master/datasets/la-liga/season-1819.csv", 
            url2="https://raw.githubusercontent.com/datasets/football-datasets/master/datasets/premier-league/season-1819.csv",
            file_path1="/workspaces/ids706-miniproj-6/data/laliga.csv",
            file_path2="/workspaces/ids706-miniproj-6/data/epl.csv"):
    """"Extract a url to a file path"""
    with requests.get(url1) as r:
        df = pd.read_csv(io.StringIO(r.text))
        # rename columns
        df = df.rename(columns={"FTHG": "home_goals", "FTAG": "away_goals", "FTR": "result",
                                "HTHG": "home_goals_half_time", "HTAG": "away_goals_half_time",
                                "HTR": "result_half_time", "HS": "home_shots", "AS": "away_shots",
                                "HST": "home_shots_on_target", "AST": "away_shots_on_target", "HF": "home_fouls",
                                "AF": "away_fouls", "HC": "home_corners", "AC": "away_corners",
                                "HY": "home_yellow_cards", "AY": "away_yellow_cards", "HR": "home_red_cards",
                                "AR": "away_red_cards"})
        df.to_csv(file_path1, index=False)
    with requests.get(url2) as r:
        df = pd.read_csv(io.StringIO(r.text))
        # drop referee column
        df = df.drop(columns=["Referee"])
        # rename columns
        df = df.rename(columns={"FTHG": "home_goals", "FTAG": "away_goals", "FTR": "result",
                        "HTHG": "home_goals_half_time", "HTAG": "away_goals_half_time",
                        "HTR": "result_half_time", "HS": "home_shots", "AS": "away_shots",
                        "HST": "home_shots_on_target", "AST": "away_shots_on_target", "HF": "home_fouls",
                        "AF": "away_fouls", "HC": "home_corners", "AC": "away_corners",
                        "HY": "home_yellow_cards", "AY": "away_yellow_cards", "HR": "home_red_cards",
                        "AR": "away_red_cards"})
        df.to_csv(file_path2, index=False)
    return file_path1, file_path2
