# data-pipelines

## About
로그 수집부터 시각화 도구까지 이어지는 전체 파이프라인을 구성해보는 개인 프로젝트입니다.
![스크린샷 2024-08-20 21 47 48](https://github.com/user-attachments/assets/ebe76740-b1de-4d5e-b42c-52f2bd2020f8)
가상으로 생성된 로그를 Elasticsearch와 Postgresql에 적재하는 파이프라인을 구축했습니다. 각 데이터 프레임워크들은 Dockerfile을 작성했고 Docker-compose로 관리할 수 있습니다.

Python 코드로 생성되어 `/var/log/httpd/access_log/*.log`에 기록되는 로그는 다음과 같습니다.
```
206.176.215.237 - - [02/Dec/2022:18:57:34 +0900] "GET /api/items HTTP/1.1" 200 3456 477 "https://www.dummmmmy.com" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1"
```

## RUN
```
docker compose -f "docker-compose.yml" up -d --build 
```

### Elasticsearch + Kibana
Elasticsearch와 Kibana는 Goorm IDE에 설치하여 사용했지만 무료계정의 경우 항상 켜두기 제공이 종료되어 사용할 수 없습니다.
