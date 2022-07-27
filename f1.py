import fastf1 as ff1
from matplotlib import pyplot as plt
import datetime as dt

ff1.Cache.enable_cache('/Users/iman/Desktop/code/f1/cache')

race_count = ff1.get_event_schedule(2021, include_testing=False).shape[0]

# store data
gp_names = []
ver_max_speed = []
lec_max_speed = []

for i in range(race_count):

    race = ff1.get_session(2022, i + 1, 'R')

    # dont get future events
    if race.event.RoundNumber == 12:
        break

    race.load()

    ver_lap = race.laps.pick_driver('VER').pick_fastest()
    lec_lap = race.laps.pick_driver('LEC').pick_fastest()

    ver_stats = ver_lap.get_car_data()
    lec_stats = lec_lap.get_car_data()

    ver_max_speed.append(ver_stats['Speed'].max())
    lec_max_speed.append(lec_stats['Speed'].max())

    gp = race.event['EventName']
    gp = gp.replace(' Grand Prix', '')
    gp = gp.replace(' Arabian', '')
    gp = gp.replace(' Romagna', '')

    gp_names.append(gp)

fig, ax = plt.subplots()

ax.plot(gp_names, ver_max_speed, color='blue', label='VER')
ax.plot(gp_names, lec_max_speed, color='red', label='LEC')

plt.xticks(fontsize=6)
ax.set_xlabel('Grand Prix')
ax.set_ylabel('Max Speed in km/h')

ax.legend()

plt.suptitle('Max Speed Comparison for 2022 Races')

plt.show()
