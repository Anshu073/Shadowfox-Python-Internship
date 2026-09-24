# Cricket Fielding Analysis Data Collection Objective
import pandas as pd

raw_data = [
    ("IPL2024", 2, "RCB", "Virat Kohli", 2.3, "Cover", "Fielded cleanly, quick throw", "Y", "Y", 1, 2, "Bengaluru"),
    ("IPL2024", 2, "RCB", "Virat Kohli", 5.1, "Cover", "Fumbled the ball, wide throw", "N", "N", -2, 5, "Bengaluru"),
    ("IPL2024", 2, "RCB", "Virat Kohli", 8.4, "Cover", "Took a low catch", "C", None, 0, 8, "Bengaluru"),
    ("IPL2024", 2, "RCB", "Virat Kohli", 11.2, "Cover", "Direct hit run out attempt", "Y", "DH", 2, 11, "Bengaluru"),
    ("IPL2024", 2, "RCB", "Virat Kohli", 14.5, "Cover", "Dropped a sitter", "DC", None, -2, 14, "Bengaluru"),
    ("IPL2024", 2, "RCB", "Virat Kohli", 17.6, "Cover", "Clean stop, good throw", "Y", "Y", 1, 17, "Bengaluru"),

    ("IPL2024", 2, "CSK", "MS Dhoni", 3.2, "Wicket Keeper", "Collected byes cleanly", "Y", "Y", 0, 3, "Bengaluru"),
    ("IPL2024", 2, "CSK", "MS Dhoni", 6.5, "Wicket Keeper", "Lightning stumping", "S", None, 0, 6, "Bengaluru"),
    ("IPL2024", 2, "CSK", "MS Dhoni", 9.3, "Wicket Keeper", "Good take, quick return", "Y", "Y", 1, 9, "Bengaluru"),
    ("IPL2024", 2, "CSK", "MS Dhoni", 12.1, "Wicket Keeper", "Missed run out chance", "Y", "MR", -1, 12, "Bengaluru"),
    ("IPL2024", 2, "CSK", "MS Dhoni", 15.4, "Wicket Keeper", "Broke stumps for run out", "Y", "RO", 2, 15, "Bengaluru"),
    ("IPL2024", 2, "CSK", "MS Dhoni", 18.2, "Wicket Keeper", "Routine take", "Y", "Y", 0, 18, "Bengaluru"),

    ("IPL2024", 2, "CSK", "Ravindra Jadeja", 1.5, "Backward Point", "Sharp stop, good throw", "Y", "Y", 1, 1, "Bengaluru"),
    ("IPL2024", 2, "CSK", "Ravindra Jadeja", 4.6, "Backward Point", "Direct hit run out", "Y", "DH", 2, 4, "Bengaluru"),
    ("IPL2024", 2, "CSK", "Ravindra Jadeja", 7.2, "Backward Point", "Diving catch", "C", None, 0, 7, "Bengaluru"),
    ("IPL2024", 2, "CSK", "Ravindra Jadeja", 10.3, "Backward Point", "Clean pick, good throw", "Y", "Y", 1, 10, "Bengaluru"),
    ("IPL2024", 2, "CSK", "Ravindra Jadeja", 13.6, "Backward Point", "Clean pick, good throw", "Y", "Y", 1, 13, "Bengaluru"),
    ("IPL2024", 2, "CSK", "Ravindra Jadeja", 16.4, "Backward Point", "Relay throw run out", "Y", "RO", 2, 16, "Bengaluru"),
]

columns = ["Match No.", "Innings", "Team", "Player Name", "BallCount", "Position",
           "Short Description", "Pick", "Throw", "Runs", "Overcount", "Venue"]

df = pd.DataFrame(raw_data, columns=columns)

df.to_csv("fielding_ball_by_ball_data.csv", index=False)
print("Raw data saved in fielding_ball_by_ball_data.csv")
print(df)

W_CP = 1
W_GT = 1
W_C = 3
W_DC = -3
W_ST = 3
W_RO = 3
W_MRO = -2
W_DH = 2

all_players = []
for name in df["Player Name"]:
    if name not in all_players:
        all_players.append(name)

print("\nPlayers found:", all_players)

final_results = []

for player in all_players:
    CP = 0
    GT = 0
    C = 0
    DC = 0
    ST = 0
    RO = 0
    MRO = 0
    DH = 0
    RS = 0

    for i in range(len(df)):
        if df["Player Name"][i] == player:
            pick_value = df["Pick"][i]
            throw_value = df["Throw"][i]
            runs_value = df["Runs"][i]

            if pick_value == "Y":
                CP = CP + 1
            elif pick_value == "C":
                C = C + 1
            elif pick_value == "DC":
                DC = DC + 1
            elif pick_value == "S":
                ST = ST + 1

            if throw_value == "Y":
                GT = GT + 1
            elif throw_value == "DH":
                DH = DH + 1
            elif throw_value == "RO":
                RO = RO + 1
            elif throw_value == "MR":
                MRO = MRO + 1

            RS = RS + runs_value

    PS = (CP * W_CP) + (GT * W_GT) + (C * W_C) + (DC * W_DC) + (ST * W_ST) + (RO * W_RO) + (MRO * W_MRO) + (DH * W_DH) + RS

    player_result = {
        "Player Name": player,
        "Clean Picks (CP)": CP,
        "Good Throws (GT)": GT,
        "Catches (C)": C,
        "Dropped Catches (DC)": DC,
        "Stumpings (ST)": ST,
        "Run Outs (RO)": RO,
        "Missed Run Outs (MRO)": MRO,
        "Direct Hits (DH)": DH,
        "Runs Saved (RS)": RS,
        "Performance Score (PS)": PS
    }

    final_results.append(player_result)

matrix_df = pd.DataFrame(final_results)
matrix_df.to_csv("fielding_performance_matrix.csv", index=False)

print("\nPerformance matrix saved in fielding_performance_matrix.csv")
print(matrix_df)

best_score = 0
best_player_name = ""

for result in final_results:
    if result["Performance Score (PS)"] > best_score:
        best_score = result["Performance Score (PS)"]
        best_player_name = result["Player Name"]

print(f"\nBest fielder of this innings: {best_player_name} with score {best_score}")