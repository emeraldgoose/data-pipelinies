# data-pipelines
- 로그 수집부터 시각화 도구까지 이어지는 전체 파이프라인을 구성해보는 개인 프로젝트입니다.

![스크린샷 2022-12-02 오후 4 30 59](https://user-images.githubusercontent.com/50171632/205239615-69152b4b-112b-492e-ae90-ef752b436f6b.png)

ELK 스택은 로그를 수집하고 실시간으로 대시보드를 통해 확인할 수 있는 파이프라인에 사용했고 HDFS와 스파크는 배치 처리를 위한 파이프라인으로 구성했습니다.  
Elasticsearch와 Kibana는 docker-compose로 구성하지 않았습니다. 전체 파이프라인이 너무 커져 엘라스틱서치와 키바나는 [ide.goorm.io](https://ide.goorm.io)에 설치하여 사용했습니다.  
