from actions.life_actions import get_goals, imAlive, keepOn, success, done, die

print('\n\nI came to life...\n\n')

while imAlive():
    goals = get_goals()
    for goal in goals:
        while success(goal) != True:
            keepOn(goal)
        done(goal)
die()