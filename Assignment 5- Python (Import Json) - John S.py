import json
import datetime

def get_questions_from_json():
    with open('trivia.json', 'r') as file:
        data = json.load(file)
        return data

def play_game(questions):
    score = 0
    for q in questions:
        print(q['question'])
        for i, option in enumerate(q['options'], 1):
            print(f"{i}. {option}")
        answer = input("Enter your answer (or 'wipe' to reset hiscores): ")
        if answer == 'wipe':
            wipe_hiscore()
            return
        if int(answer) == q['correct_answer']:
            score += 1
    return score

def wipe_hiscore():
    with open('hiscore.txt', 'w') as file:
        file.write('')

def store_hiscore(name, score):
    with open('hiscore.txt', 'a') as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{name},{score},{timestamp}\n")

def get_top_3_hiscores():
    scores = []
    with open('hiscore.txt', 'r') as file:
        for line in file:
            name, score, timestamp = line.strip().split(',')
            scores.append((name, int(score), timestamp))
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:3]

def main():
    questions = get_questions_from_json()
    score = play_game(questions)
    if score is not None:
        print(f"\nYour score is: {score}")
        name = input("Enter your name: ")
        while not name.strip():
            name = input("Enter a valid name (at least one non-whitespace character): ")
        store_hiscore(name, score)
        print("\nTop 3 High Scores:")
        for name, score, timestamp in get_top_3_hiscores():
            print(f"{name}: {score} points on {timestamp}")

if __name__ == "__main__":
    main()
