import csv
import json
import sys
from time import sleep

from bokeh.plotting import figure, output_file, show
import requests

from client_config import Config


def min_to_time(minute):
    hour_str = str(minute // 60)
    minute_str = str(minute % 60).zfill(2)
    return f"{hour_str}시 {minute_str}분"


def min_to_query(minute):
    hour_str = str(minute // 60)
    minute_str = str(minute % 60).zfill(2)
    return f"?t={hour_str}h{minute_str}m00s"


def chat_analyse(id):
    # 초기화
    video_id = id
    twitch_url = f"https://www.twitch.tv/videos/{id}"

    if not video_id:
        print("WARNING : 올바른 ID를 입력해주세요!")
        return

    chat_list = []
    minute_list = []

    next_cursor = ''

    header = {"Accept": "application/vnd.twitchtv.v5+json; charset=UTF-8"}
    params = {'client_id': "kimne78kx3ncx6brgo4mv6wki5h1ko"}

    i = 0
    count = 1

    # 다시보기 채팅 내역 가져오기
    while True:
        if i == 0:
            url = f"https://api.twitch.tv/v5/videos/{video_id}/comments?content_offset_seconds=0"
            i += 1
        else:
            url = f"https://api.twitch.tv/v5/videos/{video_id}/comments?cursor={next_cursor}"

        try:
            response = requests.get(url, params=params, headers=header, timeout=10)
        except:
            sleep(1)
            continue

        count += 1

        j = json.loads(response.text)
        print(j["comments"][0]['created_at'])

        for comment in j["comments"]:
            timer = float(comment["content_offset_seconds"])
            minute_list.append(int(timer // 60))
            chat_list.append(comment["message"]["body"])

        if '_next' not in j:
            break

        next_cursor = j["_next"]

    # 채팅 정보에서 분당 웃음 갯수 세기
    max_minute = minute_list[-1]
    laughter_per_min_list = [0 for _ in range(max_minute + 1)]
    time_list = range(max_minute + 1)
    for minute, chat in zip(minute_list, chat_list):
        laughter_per_min_list[minute] += chat.count('ㅋ')

    # 가져온 채팅 내역을 그래프를 포함한 html 파일로 만들기
    output_file(f"{video_id}.html")
    p = figure(title=f"#{video_id} 다시보기 결과",
               x_axis_label='x',
               y_axis_label='y',
               plot_width=1600)
    p.line(time_list, laughter_per_min_list, legend="분당 웃음 개수", line_width=2)
    show(p)

    # csv 파일로 저장하기
    with open(f"{video_id}.csv", "w", newline='') as f:
        writer = csv.writer(f)
        csv_list = [[min_to_time(minute), laughter, twitch_url + min_to_query(minute)]
                    for minute, laughter in zip(time_list, laughter_per_min_list)]
        csv_list.sort(key=lambda x: -x[1])
        writer.writerows(csv_list)



def main():
    while True:
        print("twitch vod id : ", end='')
        url = sys.stdin.readline().rstrip()
        chat_analyse(url)


if __name__ == "__main__":
    main()
