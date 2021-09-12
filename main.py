# Schedule's non-division games for Indiana's Finest Fantasy Football League
# Author: David Niblick
# Date: 22AUG2021

import random

hermanos = ('david', 'daniel', 'mike m', 'mark m')
amigos = ('zech', 'mitch', 'nick', 'ryan')
sicarios = ('mike a', 'chris', 'mark b', 'matt')

league = (hermanos + amigos + sicarios)
FINISH = False
attempts = 0


if __name__ == '__main__':
    while not FINISH:
        failure = False
        opponent = []
        for i in league:
            opponent.append([])

        for week in range(4, 12):
            if failure:
                break
            week_teams = []
            teams_yet_to_play = list(league)
            while len(teams_yet_to_play) > 0:
                if failure:
                    break
                team_index = league.index(teams_yet_to_play[0])
                if teams_yet_to_play[0] in hermanos:
                    possible_opponents = set(amigos + sicarios)
                elif teams_yet_to_play[0] in amigos:
                    possible_opponents = set(hermanos + sicarios)
                else:
                    possible_opponents = set(hermanos + amigos)
                possible_opponents = possible_opponents - set(opponent[team_index])
                possible_opponents = possible_opponents - set(week_teams)
                if len(possible_opponents) == 0:
                    failure = True
                    break
                else:
                    opposing_team = random.choice(list(possible_opponents))
                    opponent[team_index].append(opposing_team)
                    opponent[league.index(opposing_team)].append(teams_yet_to_play[0])
                    week_teams.append(teams_yet_to_play[0])
                    week_teams.append(opposing_team)
                    teams_yet_to_play.remove(teams_yet_to_play[0])
                    teams_yet_to_play.remove(opposing_team)

        attempts += 1
        print(attempts)

        if not failure:
            FINISH = True

    count = 0
    for team in league:
        print(team)
        print(opponent[count])
        print()
        print()
        count += 1
