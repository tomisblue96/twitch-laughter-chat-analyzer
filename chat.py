import requests
import json
import time

import openpyxl


def chat_analyse(v_id):
    # 초기화
    video_id = v_id
    client_id = '*'

    chat_list = []
    minute_list = []

    next_cursor = ''

    params = {'client_id': client_id}

    i = 0
    count = 1

    # 다시보기 채팅 내역 가져오기
    while True:
        if i == 0:
            url = 'https://api.twitch.tv/v5/videos/' + video_id + '/comments?content_offset_seconds=0'
            i += 1
        else:
            url = 'https://api.twitch.tv/v5/videos/' + video_id + '/comments?cursor=' + next_cursor

        try:
            response = requests.get(url, params=params, timeout=2)
        except:
            time.sleep(2)
            continue

        count += 1

        j = json.loads(response.text)

        for k in range(0, len(j["comments"])):
            timer = j["comments"][k]["content_offset_seconds"]
            minute_list.append(timer // 60)
            chat_list.append(j["comments"][k]["message"]["body"])

        if '_next' not in j:
            break

        next_cursor = j["_next"]

    # 가져온 채팅 내역을 엑셀 파일로 내보내기
    wb_total = openpyxl.Workbook()
    wb_laughter = openpyxl.Workbook()
    sheet_total = wb_total.active
    sheet_laughter = wb_laughter.active
    max_minute = minute_list[-1] + 1

    # 시간당 채팅 빈도 파일 만들기
    sheet_total.append(["시간", "채팅 갯수"])
    total_list = [0 for _ in range(max_minute)]

    for minute in minute_list:
        total_list[minute] += 1
    for chat_min, chat_sum in enumerate(total_list):
        sheet_total.append([chat_min, chat_sum])

    wb_total.save(video_id + '_total.xlsx')

    # 시간당 'ㅋ'의 갯수 빈도 파일 만들기
    sheet_laughter.append(["시간", "웃음 갯수"])
    laughter_list = [0 for _ in range(max_minute)]

    for minute, chat in zip(minute_list, chat_list):
        laughter_list[minute] += chat.count('ㅋ')
    for chat_min, chat_sum in enumerate(laughter_list):
        sheet_laughter.append([chat_min, chat_sum])

    wb_laughter.save(video_id + '_laugh.xlsx')


def main():
    while True:
        vid_num = input("분석할 트위치 다시보기 번호를 입력하세요 : ")
        chat_analyse(vid_num)


if __name__ == "__main__":
    main()
