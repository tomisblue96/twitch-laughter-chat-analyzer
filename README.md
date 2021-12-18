# 트위치 다시보기 꿀잼 분석기

![001_다시보기꿀잼분석기](https://user-images.githubusercontent.com/46725061/146645415-42163414-2fbd-4612-b840-825449993f75.png)

**다시보기에서 재밌는 부분만 쏙쏙 보고 싶은데 10시간이나 넘는 길이가 막막했나요?**

파이썬으로 간편하게 시청자들이 반응이 핫했던 장면을 알아보세요!



***Python 3.7.1***



## 무엇을 할 수 있나요?

- 시간별 채팅 횟수를 정리한 엑셀 파일 다운로드

- 시간별 웃음 횟수를 정리한 엑셀 파일 다운로드



## 이런 분들에게 도움이 돼요!

- 10시간이나 넘는 스트리머의 방송을 모두 챙겨볼 수 없는 편집자들

- 아쉽게 놓쳤던 생방송에서 재밌는 부분만 다시 보고 싶은 시청자들



## 제작기

- [Pgr21 - 파이썬으로 트위치 스트리머 영상 편집점 찾기](https://pgr21.com/freedom/81638)

- [트게더 - 채팅 기록으로 편집점 찾는 방법](https://tgd.kr/c/editorssquare/26984072)



## 사용 방법

1. 파이썬을 실행합니다.

```
python main.py
```



2. 프롬포트 창에 <mark>다시보기 ID</mark>를 입력합니다. 트위치 다시보기 ID는 다시보기 페이지 URL에서 확인할 수 있습니다.

> http://www.twitch.tv/videos/ + (다시보기 ID)

```
분석할 트위치 다시보기 번호를 입력하세요 : 
```



3. 엑셀 파일이 main.py이 저장된 위치에 출력됩니다. 해당 파일들의 내용은 다음과 같습니다.
   
   - *_total.xlsx
     
     시간과 시간별 채팅 갯수가 2개의 열로 저장됩니다.
     
     ![001.png](D:\dev\python\temp\001.png)
   
   - *_laugter.xlsx
     
     시간과 시간별 웃음('ㅋ') 갯수가 2개의 열로 저장됩니다.
     
     ![002.png](D:\dev\python\temp\002.png)



4. 엑셀 내부 기능과 엑셀 분석 툴을 이용해 시각화할 수 있습니다. 유저들이 어느 시각에 반응이 좋았는지 확인할 수 있습니다.

![003.png](D:\dev\python\temp\003.png)



## 이슈

**2021년 7월 15일**

> {"error":"Not Found","status":404,"message":"The v5 API is deprecated and will be shutdown on February 28, 2022. Applications that have not accessed v5 before July 15, 2021 no longer have access to v5. For more information on the v5 API shutdown plan, see https://blog.twitch.tv/2021/07/15/legacy-twitch-api-v5-shutdown-details-and-timeline/ and the Twitch API documentation at https://dev.twitch.tv/docs/api."}

트위치 v5 API가 7월 15일 이후 지원이 되지 않습니다. 트위치의 최신 API는 채팅 내역을 제공하지 않아 코드가 정상적으로 결과를 출력하지 않습니다. 차후에 다른 방법을 찾아 개선하도록 하겠습니다.



### 
