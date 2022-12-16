myfile = open("1518337.json")
content = myfile.read()

import json
data = json.loads(content)

import pandas as pd
import math
score_data = {}
for person in data['members'].values():
    person_scores = person['completion_day_level']
    scores = [math.inf] * 50
    for day_number in person_scores:
        if '1' in person_scores[day_number]:
            scores[(int(day_number)-1)*2] = person_scores[day_number]['1']['get_star_ts']
        if '2' in person_scores[day_number]:
            scores[((int(day_number)-1)*2)+1] = person_scores[day_number]['2']['get_star_ts']
    if person['name'] != None:
        score_data[person['name']] = scores
    else:
        score_data["anonymous: " + person['id']] = scores

df_times = pd.DataFrame(score_data)
df_temp_scores = df_times.copy()
df_final_scores = df_times.copy()[:25]
num_people = len(df_times.columns)

from datetime import datetime
import time
for day in range(2, 26):
    date_time = datetime(2021, 12, day, 16, 00)
    unix_time = time.mktime(date_time.timetuple())
    df_temp_times = df_times.copy()
    df_temp_times[df_times > unix_time] = math.inf
    for i, row in enumerate(df_temp_times.iterrows()):
        row = row[1]
        df_temp_scores.loc[i] = num_people - (row.rank()-1)
    # Ignore the scores for people who haven't completed the problem
    df_temp_scores[df_temp_times == math.inf] = 0
    df_final_scores.loc[day-2] = df_temp_scores.sum()

df_final_scores = df_final_scores.T.sort_values(12, ascending=False).T
df_final_scores.to_csv("Scores.csv")

for day in range(1, 26):
    date_time = datetime(2021, 12, day, 16, 00)
    unix_time = time.mktime(date_time.timetuple())
    df_times.loc[(day-1)*2] -= unix_time
    df_times.loc[((day-1)*2)+1] -= unix_time

df_times = df_times.T.reindex(df_final_scores.columns).T
df_times.to_csv("Times.csv")

for i in range(0, 22, 2):
    df_times.loc[i] = df_times.loc[i+1]-df_times.loc[i]

df_times.iloc[list(range(0, 22, 2))].to_csv("Time Diffs.csv")  
