import openpyxl
import requests
import json
import time


def doubleDigit(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


def chatAnalyse(v_id):

    video_id = v_id
    client_id = '*'

    chat = []
    min = []
    user = []
    total = []
    laugh = []

    next_cursor = ''

    params = {}
    params['client_id'] = client_id

    i = 0
    count = 1

    while True:
        if i == 0:
            URL = 'https://api.twitch.tv/v5/videos/' + video_id + '/comments?content_offset_seconds=0'
            i += 1
        else:
            URL = 'https://api.twitch.tv/v5/videos/' + video_id + '/comments?cursor=' + next_cursor

        try:
            response = requests.get(URL, params=params, timeout=2)
        except:
            print("에러발생")
            print("2초후 재시도 시작")
            time.sleep(2)
            continue

        print(count)
        count += 1

        print(response.text)
        j = json.loads(response.text)

        for k in range(0, len(j["comments"])):
            timer = j["comments"][k]["content_offset_seconds"]
            time_minute = int(timer / 60)

            min.append(doubleDigit(time_minute))
            user.append(j["comments"][k]["commenter"]["display_name"])
            chat.append(j["comments"][k]["message"]["body"])

        if '_next' not in j:
            break

        next_cursor = j["_next"]

    print("추출 시작")
    wb = openpyxl.Workbook()
    wb_total = openpyxl.Workbook()
    wb_laugh = openpyxl.Workbook()
    sheet = wb.active
    sheet_total = wb_total.active
    sheet_laugh = wb_laugh.active

    print("로그 추출 시작")
    sheet.append(["시간", "유저 이름", "채팅", "웃음 개수"])
    for x in range(0, len(min)):
        sheet.append([str(min[x]), str(user[x]), str(chat[x]), chat[x].count('ㅋ')])

    wb.save(video_id + '.xlsx')
    print("로그 추출 완료")

    print("전체 분석 시작")
    sheet_total.append(["시간", "채팅 갯수"])
    for i in range(0, int(min[-1])+1):
        total.append(0)
    for x in range(0, len(min)):
        total[int(min[x])] += 1
    for x in range(0, len(total)):
        sheet_total.append([x, total[x]])

    wb_total.save(video_id + '_total.xlsx')
    print("전체 분석 완료")

    print("ㅋㅋ 분석 시작")
    sheet_laugh.append(["시간", "웃음 갯수"])
    for i in range(0, int(min[-1]) + 1):
        laugh.append(0)
    for x in range(0, len(min)):
        laugh[int(min[x])] += chat[x].count('ㅋ')
    for x in range(0, len(laugh)):
        sheet_laugh.append([x, laugh[x]])

    wb_laugh.save(video_id + '_laugh.xlsx')
    print("ㅋㅋ 분석 완료")

    print("end")


def main():
    while 1:
        vid_num = input("분석할 트위치 다시보기 번호를 입력하세요 : ")
        chatAnalyse(vid_num)


if __name__ == "__main__":
    main()