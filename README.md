# 트위치 다시보기 꿀잼 분석기

![001_다시보기꿀잼분석기](https://user-images.githubusercontent.com/46725061/146645415-42163414-2fbd-4612-b840-825449993f75.png)

**다시보기에서 재밌는 부분만 쏙쏙 보고 싶은데 10시간이나 넘는 길이가 막막했나요?**

파이썬으로 간편하게 시청자들이 반응이 핫했던 장면을 알아보세요!

***Python 3.7.1***

## 무엇을 할 수 있나요?

- 방송 흐름을 알 수 있는 그래프 html 파일 저장.

- 시간별 웃음 횟수를 알 수 있는 csv 파일 저장.

## 이런 분들에게 도움이 돼요!

- 10시간이나 넘는 스트리머의 방송을 모두 챙겨보기가 어려운 편집자들.

- 좋아하는 스트리머의 예전 방송에서 꿀잼 부분만 다시 보고 싶은 시청자들.

## 제작기

- [Pgr21 - 파이썬으로 트위치 스트리머 영상 편집점 찾기](https://pgr21.com/freedom/81638)

- [트게더 - 채팅 기록으로 편집점 찾는 방법](https://tgd.kr/c/editorssquare/26984072)

## 사용 방법

1. 파이썬을 실행합니다.

```
python main.py
```

2. 프롬포트 창에 다시보기 ID를 입력합니다. 트위치 다시보기 ID는 다시보기 페이지 URL에서 확인할 수 있습니다.

> http://www.twitch.tv/videos/ + (다시보기 ID)

```
twitch vod id : 
```

3. 분석된 파일이 main.py이 저장된 위치에 출력합니다. 해당 파일들의 내용은 다음과 같습니다.
   
   - video_id.html
     
     시간별로 방송 채팅의 흐름을 알 수 있는 그래프가 포함된 html 파일입니다.
     
     ![001.PNG](https://github.com/tomisblue96/twitch-laughter-chat-analyzer/blob/main/img/001.PNG?raw=true)
   
   - video_id.csv
     
     웃음 갯수가 높은 순서대로 시간이 정렬된 csv 파일입니다. URL 링크로 손쉽게 해당 시간의 다시보기를 시청할 수 있습니다.
     
     ![002.PNG](https://github.com/tomisblue96/twitch-laughter-chat-analyzer/blob/main/img/002.PNG?raw=true)

## 이슈

**2021년 7월 15일**

> {"error":"Not Found","status":404,"message":"The v5 API is deprecated and will be shutdown on February 28, 2022. Applications that have not accessed v5 before July 15, 2021 no longer have access to v5. For more information on the v5 API shutdown plan, see https://blog.twitch.tv/2021/07/15/legacy-twitch-api-v5-shutdown-details-and-timeline/ and the Twitch API documentation at https://dev.twitch.tv/docs/api."}

트위치 v5 API가 7월 15일 이후 지원이 되지 않습니다. 트위치의 최신 API는 채팅 내역을 제공하지 않아 코드가 정상적으로 결과를 출력하지 않습니다. 차후에 다른 방법을 찾아 개선하도록 하겠습니다.

**2021년 12월 19일**

정상적으로 채팅 로그가 수집됩니다. 출력되는 데이터를 꿀잼 장면을 더 손쉽게 알 수 있도록 수정했습니다.

- 클라이언트 ID 교체.

- xlsx 파일이 아닌 그래프가 포함된 html 파일과 csv 파일을 출력.

### 
