# 요점 정리

## 개요

이 문서는 정보기기운용기능사 자격증 시험을 위한 네트워크 기기 운용 관련 상황 별 명령어를 정리한 문서이다.

## 본문

### Privileged Mode

#### 접근

라우터 또는 스위치에서 Privileged EXEC Mode 에 접근하는 방법은 다음과 같다.

Router> `enable`

Router#

### Configuration Mode

#### 접근

라우터 또는 스위치에서 Configuration Mode 에 접근하는 방법은 다음과 같다.

Router# `configure terminal`

Enter configuration commands, one per line. End with CNTL/Z.

Router(config)#

#### enable 암호 설정

라우터 또는 스위치의 관리자모드(Privileged Mode)로 접근하기 위한 암호를 설정하는 명령어는 다음과 같다.

평문으로 저장 : Router(config)# `enable password pass!!`

MD5 암호화하여 저장 : Router(config)# `enable secret pass!!`

### Line Configuration Mode

#### console

1.  접근

    라우터 콘솔 설정 모드에 접근하는 방법은 다음과 같다.

    Router(config)# `line console 0`

    Router(config-line)#

2.  히스토리 크기

    라우터 콘솔에서 입력했던 명령어를 7 개만 기억하도록 설정하는 명령어는 다음과 같다.

    Router(config-line)# `history size 7`

#### vty

##### 접근

라우터 가상 터미널 설정 모드에 접근하는 방법은 다음과 같다.

Router(config)# `line vty 0 4`

Router(config-line)#
