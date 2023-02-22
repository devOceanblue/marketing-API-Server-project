# 광고서버

### Run
docker-compose up -d

### API 문서
http://localhost:8082/docs#


### pre-commit
pre-commit을 통해 PEP8 형식에 맞게 자동화
1. pip install pre-commit
2. pre-commit install


### Database
1. create_db.sql
2. create_tables.sql
3. insert_ad_campaigns.sql

Docker compose up -d 명령어를 실행하면 위 세개의 파일을 mysql Docker entrypoint에서 실행하여 테스트 DB 초기화함.
만약 스키마 변경이나 테스트 데이터 추가가 필요하다면 위 sql파일을 수정 후 다시 Docker 빌드 및 실행
