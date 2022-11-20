1. 회원가입 정보를 커스텀화하기

- Registerserializer를 상속받아 재정의해 줘야 한다.
- AUTH_USER_MODEL = 'accounts.User'(완)
- 데이터 베이스 설계(진행중)\
- 모델 클래스 설정(완)
- django-rest-auth 사용을 위한 설치, 설정(진행 중)

2. 유저

   1. 회원가입/탈퇴
   2. 로그인/로그아웃
   3. 디테일
   4. 좋아요
   5. ㅇ

3. App

   1. 서비스 이름
   2. 검색창
   3. 내비게이션 바

3) 영화

   1. 좋아하는 영화를 선택하세요-(추천알고리즘)
   2. 요즘 트렌드 영화 제시

4. 무비아이템디테일(클릭 시)
   1. 영화 제목
   2. 영화 배우들

========================================
팁

내용.
사실 장고에서 워낙 잘만들어 놓았기 때문에 알뜰하게 사용법만 익히면 아주 쉽다.

- 기본 명령어

python manage.py dumpdata > xxx.json

이렇게 명령어를 치면 내 장고가 사용하고 있는 모든 DB의 데이터를 json형식으로 저장을 알아서 해준다.

- 특정 앱의 데이터만 덤프할때

python manage.py dumpdata appname > xxx.json

dumpdata 뒤에 파라미터로 앱이름을 적어주면 해당 앱의 내용만 데이터 덤프가 된다.

- 특정 데이터만 빼고 덤프할때

python manage.py dumpdata --exclude appname > xxx.json

dumpdata 뒤에 파라미터로 제외할 앱이름을 적어주면 된다.

P.S 장고 DB를 보통 통으로 옮길 때 내가 사용하는 명령어이다.

python3 manage.py dumpdata --exclude auth.permission --exclude authtoken --exclude contenttypes > 2018-11-29.json

그럼 우리에겐 데이터를 덤프뜬 json파일이 있으니, 이걸 내가 원하는 장고 서버에 올려야 한다.

- 기본 명령어

python manage.py loaddata xxx.json

기존에 내가 덤프뜬 JSON 파일을 알아서 내 장고 DB에 넣어준다.

장고의 loaddata에도 exclude와 같은 기능이 있지만

간편하게 dump를 뜰때 이쁘게 떠서 바로 로드하는 것이 더 편하다.
 
 
====================================
의문점
1. 역참조한 comments정보를 어떻게 serializer로 같이 보내줄까? - 221005(수)_코딩 Live 강의 Python 트랙_오후_1_Comment 구현 2 

2. makemigration과 migrate를 하는데 설계도는 정상적으로 불러오지만 db반영이 되지 않음!