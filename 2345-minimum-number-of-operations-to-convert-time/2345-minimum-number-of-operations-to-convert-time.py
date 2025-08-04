class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        steps = 0
        print(current, correct)
        current_hours = int(current[0])*10 + int(current[1])
        current_mins = int(current[3])*10 + int(current[4])
        correct_hours = int(correct[0])*10 + int(correct[1])
        correct_mins = int(correct[3])*10 + int(correct[4])
        # print(current_hours, current_mins, correct_hours, correct_mins)
        difference = (correct_hours * 60 + correct_mins) - (current_hours * 60 + current_mins)
        # print(difference)
        while difference != 0:
            steps += difference // 60
            difference = difference % 60
            steps += difference // 15
            difference = difference % 15
            steps += difference // 5
            difference = difference % 5
            steps += difference // 1
            difference = difference % 1
        return steps