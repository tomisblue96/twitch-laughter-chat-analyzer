# 트위치 다시보기 꿀잼 분석기

![001_다시보기꿀잼분석기](https://user-images.githubusercontent.com/46725061/146641028-b8e57e85-2278-4f44-9bdc-89d6f4a5564b.png)

트위치 다시보기 ID를 입력하면 채팅 로그를 분석하여 시간당 'ㅋ'의 갯수를 엑셀(xlsx) 파일로 출력합니다.



트위치 다시보기 ID는 다시보기 페이지 URL에서 확인할 수 있습니다.

> www.twitch.tv/videos/(다시보기 ID)

------

**2021년 7월 15일 issue**

> {"error":"Not Found","status":404,"message":"The v5 API is deprecated and will be shutdown on February 28, 2022. Applications that have not accessed v5 before July 15, 2021 no longer have access to v5. For more information on the v5 API shutdown plan, see https://blog.twitch.tv/2021/07/15/legacy-twitch-api-v5-shutdown-details-and-timeline/ and the Twitch API documentation at https://dev.twitch.tv/docs/api."}

트위치 v5 API가 7월 15일 이후 지원이 되지 않습니다. 트위치의 최신 API는 채팅 내역을 제공하지 않아 코드가 정상적으로 결과를 출력하지 않습니다.
