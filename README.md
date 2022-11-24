# Cloudie

## 1. 개요

> 아이디어 배경

본인이 본 영화 중 재밌었던 영화들에 like를 눌러주면 해당 영화들의 장르를 분석해 해당 user가 가장 좋아할 만한 장르의 영화를 추천해줄 수 있는 웹사이트를 개발하고자 하였다.

( 코로나 사태 이후  저조한 영화관 이용률 문제를 해결하기 위해 비슷한 취향을 가진 사용자들을 연결해 함께 영화를 보러 갈 수 있도록 하고자 하였다.

​	사용자는 재밌게 본 영화에 좋아요(like)를 누르고, Cloudie는 저장된 영화들의 장르 분석을 기반으로 사용자가 가장 좋아할 만한 장르의 영화를 추천한다. 또한 사용자의 장르 선호도 분석 결과를 기반으로 비슷한 취향을 가진 사용자와 상호 연결에 활용하고자 하였다.

 함께 관람한 영화는 Cloudie의 게시판(community)에서 다른 사람들과 후기를 공유하고 의견을 주고받을 수 있다.)

### 1-1. 파일 구성

file tree 사진



### 1-2. DB 모델링

ERD 사진



## 2. 프로젝트 목표

### 2-1. 서비스 목표

1. api를 활용한 영화정보 db 구성 및 실시간 영화 데이터 산출
2. db 데이터와 실시간 api를 이용한 최신영화, 추천영화, 모든영화 목록을 display
3. community의 영화 후기 작성, 댓글 작성을 활용한 사용자 간의 소통 창구
4. 팔로잉, 팔로워 기능을 포함한 사용자 정보를 확인할 수 있는 프로필 구현
5. 영화 취향이 비슷한 사용자를 연결해주는 데이트 매칭 기능 구현
6. 정보를 얻고자 하는 영화를 검색해 디테일 페이지로 연결할 수 있는 검색 기능



### 2-2. 팀원 정보 및 업무 분담

1. 학습자의 입장에서 풀스택 경험으로 실력 향상을 도모하기 위해 기능별로 Driver와 Navigator를 번갈아 진행
1. 자칫 모호해질 수 있는 업무 분담을 효과적으로 진행할 수 있도록 매 쉬는 시간 진행 정도와 진행 방향을 공유



( 피그마 사진 )

### 2-3. 대표 기능

1. movies

   1. TMDB api를 통해 영화데이터를 제공받아 DB에 저장하여 활용한다.
   2. user는 로그인 시 다양한 영화를 추천받는다. 추천 받는 내용은 아래와 같다.
      1. TMDB로부터 실시간으로 받아오는 최신 인기영화 목록
      2. user가 'like'한 영화들의 장르를 기반으로 선정된 user 전용 추천 영화 목록
      3. db에 존재하는 모든 영화 목록
   3. 추천목록의 각 영화 포스터를 클릭하면 영화별 세부 정보 페이지로 이동할수 있다.

   

2. accounts

   1. user는 로그인을 해야만 사이트 이용이 가능하도록 되어있다.

   2. 회원 가입, 회원 탈퇴, 회원정보 수정, 비밀번호 변경, 로그인, 로그아웃 기능이 구현되어있다.

   3. 모든 user는 각자의 profile 페이지가 존재하며, 본인의 profile과 타인의 profile에 접속시 보여지는 화면이 다르다.
      1. 본인의 profile에 접속할 경우 상단의 정보 부분에는 팔로워, 팔로잉, 작성 게시글 수, 작성 댓글 수와 프로필 사진, like한 영화들의 포스터가 보여지고, 각 포스터를 클릭하면 해당 영화의 세부정보 페이지로 이동된다.
      
         본인의 profile에서는 사진 이미지를 변경할 수 있는 이미지 변경 버튼 이 있고 해당 버튼은 개인 정보 변경 페이지로 연결된다.
      
         본인의 profile에서는 매칭 시스템 또한 표시된다.
      
         매칭 시스템은 크게 3부분으로 나뉘어 진다.
      
         상대방으로부터 영화 친구 신청이 온 경우 프로필, 신청을 수락, 거절 할 수 있는 버튼을 포함한 신청 공간이 표시된다.
      
         매칭에 성공했을 경우 매칭된 사람의 자세한 정보와 상대의 프로필을 방문 할 수 있는 버튼이 있는 카드들이 표시된다.
      
         새로운 영화 친구를 찾기 위해 본인과 영화 취향이 비슷한 사용자가 추천되어 나열된 카드들이 표시된다.
      
      2. 상대방의 프로필에서는 매칭 부분이 표시되지 않고 전반적인 정보는 유사하나 이미지 변경 태그가 팔로우, 언팔로우 버튼으로 변경된다.

   

3. community

   1. 모든 user는 review 게시글을 작성할 수 있다.
   2. 게시글은 게시글 제목, review할 영화 제목, 본인이 주는 평점, review 내용으로 이루어져 있다.
   3. user는 본인이 작성한 review를 포함한 모든 게시글에 좋아요를 누를 수 있고, 다시 누르면 취소된다.
   4. 게시글들은 작성, 삭제, 수정, 조회가 모두 가능하다.
   5. community 메인 페이지에서는 최근에 작성된 게시글이 맨 위로 계속 쌓이는 방식으로 모든 게시글을 보여주며, 클릭할 경우 댓글을 달 수 있는 게시글 세부 페이지로 이동한다.
   6. 모든 user는 게시글의 세부 페이지에서 댓글을 달 수 있고, 게시글과 마찬가지로 좋아요와 좋아요 취소가 가능하다.

## 3. 실제 구현 정도

> 사용 아키텍처 : Django & Vanilla JavaScript

#### 네비게이션 바

- 네비게이션 바 좌측엔 CLOUDIE 로고와 Home, Community, Select 버튼을 배치함.
  - CLOUDIE로고와 Home 버튼 클릭 시 메인 화면인 movies:index로 이동함.
  - Community 버튼을 클릭 시 게시글을 작성하고 댓글로 유저들끼리 소통이 가능한 community:index로 이동함.
  - Select 버튼 클릭 시 회원가입 직후 진행한 ''마음에 드는 영화 고르기'' 페이지로 이동되고, 이미 좋아요 표시를 했던 영화를 좋아요 취소 하거나 새로운 영화를 좋아요 표시 할 수 있다.
- 네비게이션 바 우측엔 검색창과 dropdown box, 다크모드 버튼이 있다.
  - 검색창은 제목으로 검색할지 장르로 검색할지를 선택할 수 있게 되어있고, 제목을 선택하고 검색하면 검색어가 title에 포함되어있는 영화들의 목록이 출력된다. 또한 장르를 선택하고 검색하면 검색어를 genre.name으로 갖는 영화들의 목록이 출력된다.
  - dropdown box는 username이 써있고 클릭 시 로그인 되어있는 상태라면 프로필, 회원수정, 회원탈퇴, 로그아웃 버튼이 나타난다.
    - 프로필 버튼을 클릭하면 로그인한 유저의 profile로 이동된다.
    - 회원 수정을 클릭하면 로그인한 유저의 회원 정보를 수정할 수 있는 update페이지로 이동된다.
    - 회원 탈퇴를 클릭하면 정말 탈퇴할 건지 확인하는 alert창이 나타나는데, 그 창에서 취소를 누르면 창이 사라지고 확인을 누르면 계정이 삭제된 후 login 페이지로 이동된다.
    - 로그아웃 버튼을 클릭하면 로그아웃 처리가 된 후 login 페이지로 이동된다.
  - 로그아웃된 상태라면 dropdown box에는 Anonymous가 써있고 클릭 시 로그인, 회원가입이 나타난다.
    - 로그인을 클릭하면 login 페이지로 이동된다.
    - 회원가입을 클릭하면 signup 페이지로 이동된다.
  - 다크모드 버튼은 기본적으로 다크모드 활성화 라고 display되는데, 클릭하면 다크모드가 실행되고 버튼의 innertext가 다크모드 비활성화로 토글된다. 다시 클릭하면 원래대로 돌아온다.
    - 로직 설명 써줘



####  계정

- 유저 정보
  - User 모델은 AbstractUser를 상속받아 사용했다.
    - 기본 User에 유저끼리 팔로잉을 할 수 있도록 followings라는 ManyToManyField를 추가해 주었다.
    - following은 유저가 유저 자신을 참조하는 방식이므로 'self'인자를 포함했고  symmetrical=False로 설정하였다.
    - lovings는 매칭에 사용되는 필드로 ManyToManyField로 상대 유저와 자신과의 매칭 정보를 포함한다.
    - 이외에도 age, gender, phone_number 필드를 추가하여 매칭 성공 시 해당 필드를 공개할 수 있도록 활용하였다.
- 유저 생성
    - UserCreationForm을 상속받아 CustomUserCreationForm을 활용했다.
    - widget을 통해 placeholder를 추가해 디자인적으로 깔끔하도록 하였다.
- 유저 수정
    - UserChangeForm을 상속받아 CustomUserChangeForm을 활용했다.
    - email, 이름, 전화번호 등의 정보를 수정할 수 있도록 하였다.
- 유저 인증
    - AuthenticationForm을 상속받아 CustomAuthenticationForm을 활용하였다.
    - UserCreationForm과 마찬가지로 label과 widget을 설정해 주었다.
- 영화 친구 매칭
    - 친구신청
      - 상대로부터 영화 친구 요청이 올 경우 수락, 거절을 위한 알람 공간이 생성된다.
      - 상대가 나에게 요청을 보낸 경우 나의 user.lovers에 상대가 포함되고 내가 수락을 누를 경우 상대의 uers.lovers에 내가 추가되어 이를 기반으로 매칭 성공 목록에 비동기로 표시 된다.
      - 거절을 누를 경우 나의  users.lovers에서 상대가 삭제되고 해당 알람 공간은 비동기로 삭제된다.
    - 매칭 성공
      - 상대의 lovers와 나의 lovers에 서로가 모두 포함되어 있으면 매칭이 성공된 경우 이므로 매칭 성공 목록에 표시된다.
      - 해당 카드에는 기존에 확인할 수 없던 상대의 전화번호와 이메일을 포함한 정보가 표시되고 프로빌로 연결된 버튼이 포함된다.
    - 매칭 추천
      - 매칭 추천은 나와 영화 취향이 같은 사람에게 영화 친구 신청 요청을 보낼 수 있는 버튼을 포함한 카드가 생성된다.
      - 영화 친구 신청 버튼을 클릭하면 상대방의 lovers에는 내가 포함되고 상대방이 수락을 누를 경우 나의 매칭 성공에 상대방의 정보를 포함한 정보 카드가 생성된다.
- 프로필
  - user
    - user와 OneToOneField를 설정해 각각의 유저가 한개의 프로필을 갖도록 하였다.
    - 프로필의 image 필드에는 프로필 사진을 설정할 수 있도록 하였다.
       - 이미지는 300, 300 사이즈 이상일 시 300으로 맞춰 표시되도록 하였다.
       - 기본 이미지는 media/sample.png 이고 유저들이 변경한 프로필 사진들은 /media/static/에 저장된다.
- login
   - 회원가입 시 작성했던 사용자 이름과 비밀번호 입력창과 제출버튼, 가입하기 버튼으로 이루어져있다.
     - 올바른 사용자 이름과 비밀번호를 입력한 후 제출버튼을 클릭하면 로그인 된 상태로 movies:index 페이지로 이동된다.
     - 하단의 가입하기 버튼을 클릭하면 회원가입을 진행할 수 있는 signup 페이지로 이동된다.
- update
   -  user의 정보를 변경할 수 있는 페이지이다.
   -  사용자 이름, 나이, 성별, 이메일 주소, 전화번호, 자기소개, 비밀번호 링크, 이미지 변경이 가능하다.
      -  비밀번호 링크를 클릭하면 change_password 페이지로 이동한다.
      -  Image 항목의 파일선택을 클릭하여 사진을 고르면 프로필 이미지를 변경할 수 있다.
      -  이외의 항목들은 signup에서의 내용과 동일하다.
- change_password
   -  회원 정보 변경 시 비밀번호 변경 폼으로 이동하는 링크를 통해서만 접속할 수 있다.
   -  기존 비밀번호, 새 비밀번호, 새 비밀번호 확인 으로 구성되어있다.
      -  기존 비밀번호에는 signup에서 작성한 비밀번호를 작성한다.
      -  새 비밀번호에는 변경하고자 하는 비밀번호를 작성한다.
         -  항목 하단에 지켜야할 비밀번호 규칙이 명시되어있고, 어길 시 변경이 불가능하다.
      -  새 비밀번호 확인에는 변경하고자 하는 새 비밀번호와 동일한 번호를 작성한다.
   -  하단의 변경 버튼을 클릭하면 비밀번호 변경이 완료되고, 취소 버튼을 클릭하면 변경이 취소된다.
- signup
   - 유저가 회원가입을 할 수 있는 페이지이다.
   - 사용자 이름, 비밀번호, 비밀번호확인, 나이, 성별, 이메일주소, 전화번호, 자기소개항목, 등록버튼으로 이루어져있다.
     - 사용자 이름에는 로그인 시 입력할 id (username)을 입력한다.
     - 비밀번호 에는 사용할 비밀번호를 입력한다.
     - 비밀번호 확인에는 위 비밀번호와 동일한 번호를 입력한다.
       - 다르게 작성한다면 회원가입 진행이 불가능하다.
     - 나이에는 정수로 본인의 나이를 입력한다.
     - 성별은 textchoice로, 남성과 여성 중 선택할 수 있다.
     - 이메일 주소에는 이메일 주소를 입력한다.
       - 이메일의 형식을 갖추지 않으면 회원가입 진행이 불가능하다.
     - 전화번호에는 전화번호를 입력한다.
       - 올바른 전화번호의 형식을 갖추지 않으면 회원가입 진행이 불가능하다.
     - 자기소개에는 본인을 소개하는 글을 작성하면 된다.
     - 상기 모든 사항을 제대로 입력한 뒤 등록 버튼을 클릭하면 회원가입이 완료되고 로그인 페이지로 이동된다.
   - 최하단에 위치한 로그인하러 가기 를 클릭하면 login 페이지로 이동할 수 있다.
- profile
   - 프로필 페이지 최상단에는 다음과 같은 항목들이 표시된다.
     - 프로필 이미지 : default이미지가 나타나며, 본인의 프로필인 경우에는 사진 하단에 사진변경 버튼이, 타인의 프로필이면 사진 하단에 팔로우 버튼이 나타난다.
       - 사진 변경 버튼을 클릭하면 update페이지로 이동하여 원하는 사진으로 변경이 가능하다.
       - 팔로우 버튼을 클릭하면 해당 user를 팔로우 할 수 있고, 다시 클릭하면 언팔로우된다.
     - 팔로잉 : 해당 user가 팔로우 하고있는 user의 수가 나타난다.
     - 팔로워 : 해당 user를 팔로우 하고있는 user의 수가 나타난다.
     - 좋아요한 게시글 수 : 해당 user가 좋아요한 게시글의 수가 나타난다.
     - 작성한 댓글 수 : 해당 user가 작성한 댓글의 수가 나타난다.
   - 최상단 아래로는 다음과 같은 항목들이 display된다.
     - 자기소개
       - signup에서 작성했던 자기소개가 나타나고, 그 아래로 이름, 성별, 최애 장르가 나타난다.
       - 최애 장르에 대한 알고리즘은 아래의 영화/index/user가 좋아하는 장르의 영화 에 명시되어있다.
     - 좋아하는 영화
       - Select 페이지에서 user가 좋아요를 선택한 영화들의 poster가 display된다.
       - 각 영화의 poster를 클릭하면 해당 영화의 detail 페이지로 이동할 수 있다.
     - 영화 친구 신청
       - 프로필, 수락, 거절 버튼을 포함한 배너가 생성된다.
       - 수락, 거절 버튼 클릭시 요청에 따라 매청 성공 카드가 생성되거나 해당 배너가 소멸된다.
     - 매칭 성공 목록
       - 본인과 상대가 서로의 lovers에 포함되어 있는 경우 표시될 수 있도록 설정하였다.
       - 이 경우 기존에 볼 수 없던 전화번호와 이메일 주소를 포함한 카드가 생성된다.
     - 영화 파트너 찾기
       - 나와 영화 취향이 비슷한 사람들을 추천해준다.
       - 영화 친구 신청 클릭시 상대방의 프로필의 영화 친구 신청 배너에 본인의 요청이 표시된다.



#### 영화

- 영화 정보
  - TMDB API를 사용하여 python 코딩을 통해 ㅇㅇㅇㅇ개의 영화 정보를 받아 json파일로 저장했다. 이 때 저장된 영화 정보의 장르 데이터가 pk로 되어있었기 때문에 추가로 같은 방법을 사용하여 영화장르 데이터도 json파일에 추가하여 저장했다.
  - TMDB API에서 제공하는 popular, now playing등의 실시간 영화 추천 정보를 받아오기 위해 axios를 활용하였다.
- 영화 모델은 아래와 같이 구성했다.
  - Genre 
    - json화한 장르데이터를 담기 위한 모델로, 구성은 아래와 같다.
      - genre_id : 영화데이터의 genre의 pk를 담기 위한 필드이다.
      - name : 각 pk의 이름을 담기 위한 필드이다.
  - Movie
    - json화한 영화데이터를 담기 위한 모델로, 구성은 아래와 같다.
      - genres : 영화 장르 필드이고, Genre 모델과 M:N 관계를 가진다.
      - like_users : 해당 영화를 like 한 user목록으로, User 모델과 M:N 관계를 가진다.
      - poster_path : 영화 포스터의 url을 담기 위한 필드이다.
      - overview : 영화의 요약 줄거리를 담기 위한 필드이다.
      - release_date : 영화 개봉일을 담기 위한 필드이다.
      - movie_id : 영화데이터에서 영화의 id값을 담기 위한 필드이다.
      - title : 영화 제목을 담기 위한 필드이다.
      - popularity : 영화 관객 수를 담기 위한 필드이다.
      - runtime : 영화의 총 상영시간을 담기 위한 필드이다.
      - vote_average : 영화의 평점을 담기 위한 필드이다.  
- select
  - 해당 페이지는 유저가 회원 가입 후 바로 연결되고, 이후엔 로그인 상태로 navbar의 select버튼을 통해 이동할 수 있다.
  - database에 담긴 영화 중 popularity가 높은 40개의 영화 중 유저가 맘에드는 영화들을 선택할 수 있다.
  - 영화선택과 취소를 자유롭게 할 수 있고, 선택된 영화는 흐리게 표시되어 시각적으로 구분할 수 있다.
  - 선택된 영화들의 정보는 개인 프로필 페이지에서 확인할 수 있으며 추천 영화를 선별하기 위한 장르 데이터 분석에도 반영된다.
  - 영화 선택을 중단하고 싶으면 스크롤을 따라다니는 end select 버튼을 클릭해 언제든 중단할 수 있다.


- index
  - movie app의 메인 페이지에서는 인기 영화, 현재 상영작, 상영 예정작, 높은 평점, user가 좋아요 한 영화, user가 좋아하는 장르의 영화, 랜덤 영화를 display한다. 각 구현 내용은 아래와 같다.
    - 인기 영화
      - api와 axios를 이용한 비동기 통신으로 tmdb로부터 실시간으로 trending 영화들의 목록을 받아온다.
    - 현재 상영작
      - api와 axios를 이용한 비동기 통신으로 tmdb로부터 실시간으로 now_playing 영화들의 목록을 받아온다.
    - 상영 예정작
      - api와 axios를 이용한 비동기 통신으로 tmdb로부터 실시간으로 upcoming 영화들의 목록을 받아온다.
    - 높은 평점
      - api와 axios를 이용한 비동기 통신으로 tmdb로부터 실시간으로 top rated 영화들의 목록을 받아온다.
    - user가 좋아요 한 영화
      - 회원가입 후 select에서 user가 직접 like 한 영화들의 목록이 display된다. 해당 페이지는 상단 navbar의 Select 항목을 통해 언제든지 다시 이동이 가능하고 또한 좋아요 취소 및 다른 영화에 대한 좋아요를 통해 목록을 상시 변경할 수 있다.
    - user가 좋아하는 장르의 영화
      - select 페이지에서 본인이 좋아요 누른 영화의 json 데이터에는 해당 영화의 장르가 pk값으로 저장되어있다.  각 pk값과 pk_cnt를 딕셔너리로 만든 뒤 user가 like한 모든 영화들의 데이터를 순회하면서 각 pk가 얼마나 많이 중복되었는지를 체크한 뒤 value(pk_cnt)가 가장 높은 key(pk)를 pk로 갖는 장르를 포함한 영화 중 12개를 뽑아 display한다.
    - 랜덤 영화
      - 원래는 db의 모든 영화를 보여주도록 구현했었으나, 데이터 양이 너무 많아 그 중 랜덤으로 몇 개의 영화를 추출하여 display 하는 로직으로 변경하였다.
      - json화하여 load해둔 모든 영화데이터 중 랜덤으로 12개의 영화를 뽑아 display한다.
- detail
  - detail 페이지는 database가 아니라 실시간으로 가져온 영화에 대한 정보를 표시해야 할 수도 있기 때문에 유저가 특정 영화를 클릭 시 detail 페이지에서 다시 axios를 활용해 영화 정보를 불러왔다.
  - tmdb api에서 특정 영화의 detail정보를 가져오기 위해서는 해당 영화의 id가 필요하기 때문에 detail 페이지로 전달된 영화의 id 정보를 javascript로 넘겨주어 활용하였다.
  - 특정 영화에 대해 포스터 url이 존재하지 않는 경우 '포스터 준비중'이라는 자체 이미지를 표시하였다.



#### 커뮤니티

- model
   - Review 모델은 다음의 field를 가진다.
      - title : 게시글의 제목을 담기 위한 필드이다.
      - movie_title : 게시글을 작성하려는 관련 영화 제목을 담기 위한 필드이다.
      - rank : user가 주는 영화의 평점을 저장할 필드이다.
      - content : 게시글의 내용을 담기 위한 필드이다.
      - created_at : 게시글 생성 시점을 담기 위한 필드이다.
      - updated_at : 게시글 수정 시점을 담기 위한 필드이다.
      - user : 해당 게시글을 작성한 User이고, User모델과 N : 1관계를 가진다.
      - like_users : 해당 게시글에 좋아요를 누른 User목록이고, User모델과 M : N관계를 가진다.

   - Comment 모델은 다음의 field를 가진다.
      - review : 댓글을 단 Review이고, Review모델과 N : 1 관계를 가진다.
      - user : 댓글을 작성한 User이고,  User모델과 N : 1 관계를 가진다.
      - content : 댓글의 내용을 담기 위한 필드이다.
      - like_users : 댓글에 좋아요를 누른 User들의 목록이고, User모델과 M : N 관계를 가진다.
- index
   - index페이지에서는 현재 작성되어 있는 게시글들을 확인할 수 있다.
   - 게시글들은 아래로 쌓이면서 가장 나중에 작성된 게시물이 최상단에 나타나도록 배치했다.
   - 각 게시글 마다 좌측 하단에 클릭이 가능한 좋아요 버튼이 있고, 다시 클릭하면 취소된다.
   - index에서는 게시글의 작성자, 작성시간, 관련 영화 및 게시글 제목을 확인할 수 있다.
     - 작성자의 이름을 클릭하면 작성자의 profile 페이지로 이동할 수 있다.
   - 각 게시글마다 우측 하단에 클릭이 가능한 Detail 버튼이 있고, 클릭 시 해당 게시글의 세부 페이지로 이동할 수 있다. 
- create
   - 게시글을 새로 생성할 수 있는 페이지
   - 항목은 상기의 Review 모델의 항목과 동일하다(created_at, updated_at, user, like_users 제외)
   - 작성한 게시글 수는 개인 프로필에서 확인할 수 있다.
- detail
   - index 페이지에서 한 게시글의 detail 버튼을 클릭 시 이동할 수 있다.
   - detail은 게시글 영역과 댓글 영역이 존재한다.
   - 게시글영역에는 작성자 이름, 관련 영화 제목, 게시글 제목, 작성 시간, 최종 수정 시간, 게시글 내용이 있다.
     - 작성자 이름을 클릭하면 작성자의 profile 페이지로 이동할 수 있다.
     - 게시글 작성자가 본인의 게시글의 detail 페이지로 들어가면 게시글 수정 버튼, 게시글 삭제 버튼이 나타난다.
       - 게시글 수정 버튼을 클릭하면 게시글의 각 항목을 수정할 수 있는 페이지로 이동할 수 있다.
       - 게시글 삭제 버튼을 클릭하면 게시글을 삭제할 수 있다.
   - 댓글 영역은 count()를 사용해 몇 개의 댓글이 달렸는지를 확인할 수 있는 문구와 그 아래로 모든 댓글이 나타나도록 구성했다.
     - 각 댓글에는 클릭이 가능한 좋아요 버튼이 있고, 다시 클릭하면 취소된다.
     - 본인이 작성한 댓글의 경우엔 댓글 삭제 버튼이 있고, 클릭하면 댓글을 삭제할 수 있다.
- update
   - 본인 게시글의 detail페이지에서 게시글 수정 버튼을 클릭하여 이동할 수 있는 페이지이다.
   - 게시글을 작성할때와 같은 항목들을 display하며, 아무것도 입력하지 않은 상태일 땐 원래 내용이 적혀있다.
   - 하단의 수정 버튼을 클릭하면 수정사항이 적용되고, 취소 버튼을 클릭하면 수정 작업이 취소된다.
- delete
   - 본인이 작성한 게시글의 detail페이지에서 게시글 삭제 버튼을 클릭하면 삭제 작업이 실행되도록 연결되어있는 버튼이다.




## 프로젝트 후기

### 임상빈

sexy

### 손승환

멋있음



어떤주제햇는지 서비스목표는이거다 이런걸구현햇고 계획한거 이정돈데 이만큼 채웟다

또는 ~~한기능들을 구현햇다

어떻게 협업햇고 누가이거를햇고 어떠한성과를낼수있었다

이걸통해서 무엇을 배웟는지

깃헙 잘쓸수잇게됏다 브랜치잘쓸수잇게됐다 숙제할땐복붙해서냈는데 직접해보니 난멀었다ㅋㅋ

난 준비가 된거같다 사회로나가야겟다 등등



코드를 먼저 보여주는건 비효율적

코드베이스보다는 어떤주제로 뭘했는지 시각화해서 보여주는게 좋음

캡처하는거 good -> 시연할때 안되는경우가 있을수있음. 이때 캡처본이라도 보여주면 덜억울함

 
