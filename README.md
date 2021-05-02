# 2021se


## <작업환경 세팅 방법>

## 1. 가상환경 실행 및 구축

1. virtualenv 패키지 설치

    ```bash
    pip install virtualenv
    ```

2. 자신의 가상환경 'myenv' 만들기

    ```bash
    virtualenv myenv
    ```

3. 윈도우에서 가상환경 시작

    ```bash
    cd myenv\Scrips
    activate.bat
    ```

4. Shell 의 경로 앞에 (myenv)가 생기면 가상환경 실행 성공!

    ![4](https://user-images.githubusercontent.com/28949166/116814353-7ec03500-ab93-11eb-9b04-a38ed689fafe.png)


5. 장고 설치

    ```bash
    pip install Django
    python
    >>>import django
    >>>print(django.get_version())
    ```

    - 장고의 버전이 정상적으로 프린트 되면 설치 성공!
6. mysqlclient 설치

    ```bash
    pip install mysqlclient
    ```

7. 확인

다음은 릴리즈 하기 위해 구축해야할 가상환경들이다.

![7](https://user-images.githubusercontent.com/28949166/116814358-85e74300-ab93-11eb-851c-1bb7d67879f2.png)


본인 컴퓨터의 로컬에 위와 같은 가상환경이 잘 구축되었는지 확인한다.

```bash
pip freeze
```

## 2.MySQL 다운 로드 후 덤핑 파일 받기

1. MySQL workbench를 다운로드 받는다.
2. 새로운 SQL Model을 만든다. (Model안에 스키마를 만듦)
3. "shop"이라는 이름의 빈 스키마를 만든다.
4. 왼쪽에서 <Administration> 탭을 열고 Data Import/Restore 에 들어간다.
5. 덤프파일이 존재하는 위치를 지정해준다. (~\2021se\dump_files\dump_daeun_20210501) → 덤프파일이 업데이트 되면서 위치도 달라짐.
6. 오른쪽 아래의 Start Import 버튼을 누른다.

## 3. Migration

이때 Migration은 workbench의 <migration wizard>를 사용하는 것이 **아니다.**

1. cmd 창을 켜고 [manage.py](http://manage.py) 가 있는 위치로 이동한다.

    ```bash
    cd ~\2021se\shoppingMall
    ```

2. makemigrations 명령어를 실행한다.

    ```bash
    py manage.py makemigrations
    ```

    - <1045 오류 발생시 대처법> **1045, "Access denied for user 'admin'@'localhost'**

        이는 본인 mysql 의 아이디 비번과 settings.py의 유저와 비밀번호가 달라서 생기는 오류이다.

        ~\2021se\shoppingMall\shoppingMall\[settings.py](http://settings.py/) 의 DATABASES에서 USER, PASSWORD를 본인의 mysql 아이디, 비밀 번호로 바꾸어준다.

        ![3](https://user-images.githubusercontent.com/28949166/116814334-62bc9380-ab93-11eb-9131-9321622b07ce.png)


3. MySQL shell에서 'shop'데이터 베이스를 만들어준다.

    ```bash
    mysql -u root -p
    Enter password:(비밀번호 입력)

    mysql> create Database shop;
    mysql> ^Z
    ```

4. 마이그레이션 해준다.

    ```bash
    py manage.py migrate
    ```

## 4. Runserver

1. 서버를 실행시킨다.

    ```bash
    py manage.py runserver
    ```

2. [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 홈페이지에 들어간다.



## <Database Schema>
![슬라이드1](https://user-images.githubusercontent.com/28949166/114647559-435ee300-9d18-11eb-83fd-4b7f7372082a.JPG)
![슬라이드2](https://user-images.githubusercontent.com/28949166/114647574-48bc2d80-9d18-11eb-850a-e25b8d02af06.JPG)


