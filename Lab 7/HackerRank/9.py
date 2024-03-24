n = int(input())

scores = list(map(int, input().split()))

scores.sort(reverse=True)

runner_up_score = None
for score in scores:
    if score != scores[0]:
        runner_up_score = score
        break

print(runner_up_score)
