import sys
from pylint import lint

THRESHOLD = 10

run = lint.Run(["--rcfile=.pylintrc",'haromszog.py'], exit=False)

score = run.linter.stats.global_note
print('Score: {score}')

if (score < THRESHOLD):
    print("Score is below threshold")
    sys.exit(1)
else:
    print("Score is above threshold, all good")
    sys.exit(0)