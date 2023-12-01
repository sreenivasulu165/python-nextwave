distance=100
bonus_score=50
first_40_score=40*2
next_20_score=20*4
next_60_score=60*6
if distance<=40:
    score=distance*2
elif distance<=60:
    remaining_distance=distance-40
    reamaing_distance_score=remaining_distance*4
    score=first_40_score+reamaing_distance_score
elif distance<=120:
    remaining_distance=distance-60
    reamaing_distance_score=remaining_distance*6
    score=first_40_score+next_20_score+remaining_distance
else:
    remaining_distance=distance-120
    reamaing_distance_score=remaining_distance*8
    score=first_40_score+next_20_score+next_60_score+reamaing_distance_score
score=bonus_score+score
print(score)
    