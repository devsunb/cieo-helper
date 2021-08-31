import json
import math
import random
import time


def init_db():
    return json.loads(open("./db.json").read())


def count(index, db, result):
    for item in result:
        if db['list'][index]["id"] == item["id"]:
            try:
                item["count"] = item["count"] + 1
            except KeyError:
                item["count"] = 1


def print_result(result, total_count):
    max_try = 0

    worst_answer = ""
    worst_answer_short = ""

    for (i, item) in enumerate(result):
        if result[max_try]["count"] < item["count"]:
            max_try = i

    for (i, answer) in enumerate(result[max_try]["answer"]):
        if i == len(result[max_try]["answer"]) - 1:
            worst_answer += answer["command"]
            worst_answer_short += answer["command"][0:answer["auto"]]
        else:
            worst_answer += answer["command"] + " "
            worst_answer_short += answer["command"][0:answer["auto"]] + " "

    print("\n" * 24)
    print("모든 문제를 맞추셨습니다!!!\n")
    print("평균 시도 횟수:\t\t{} 회".format(total_count / len(result)))
    print()
    print("가장 오래 걸린 문제:\t{}".format(result[max_try]["question"]))
    print("시도 횟수:\t\t{} 회".format(result[max_try]["count"]))
    print("Mode:\t\t\t{}".format(result[max_try]["prefix"]))
    print("정답:\t\t\t{} ({} 부터 정답)".format(worst_answer, worst_answer_short))


def jungbo(db):
    result = db["list"][0:]
    total_questions = len(result)
    total_count = 1

    print("\n" * 13)
    print("    이 프로젝트는 대덕소프트웨어마이스터고등학교 정보보안과의 정보기기운용기능사 자격증 준비를 위해 기획되었습니다.")
    print("    이 프로젝트는 120*30 터미널에 최적화 되어 있습니다.")
    print("    Made by j43530k")
    print("    3초 후 시작됩니다...")
    print("\n" * 13)
    time.sleep(3)

    while len(db["list"]) != 0:
        correct_flag = True
        index = random.randrange(0, len(db['list']))

        print("\n" * 20)
        print("총 {}개 중 {}번째 질문".format(
            total_questions, db['list'][index]["id"]))
        print("이번 문제 {}번째 시도".format(
            ("count" in db['list'][index]) and db['list'][index]["count"] or 0))
        print("총 {}번째 시도".format(total_count))
        print("\n" * 5)

        print("질문 : " + db['list'][index]["question"])
        print(db['list'][index]["prefix"], end=" ")
        answer_str = input()

        answer_arr = answer_str.split(" ")

        if len(answer_arr) == len(db['list'][index]["answer"]):
            for (i, answer) in enumerate(db['list'][index]["answer"]):
                if len(answer_arr[i]) < answer["auto"] or answer_arr[i] != answer["command"][0:len(answer_arr[i])]:
                    correct_flag = False
                    break
        else:
            correct_flag = False

        count(index, db, result)
        total_count += 1

        if correct_flag:
            db["list"].pop(index)
            print("Correct!\n")
        else:
            print("Wrong!\n")

    print_result(result, total_count)


def main():
    db = init_db()
    jungbo(db)


if __name__ == "__main__":
    main()
