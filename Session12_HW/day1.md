# 1. JavaScript Drum Kit

## 1.1. HTML

### 1.1.1. [data-](https://tonks.tistory.com/147)

---

'data- '속성은 모든 태그에 적용할 수 있는 글로벌 속성이다. 기본적으로 제공되는 속성이 아닌, 나만의 새로운 속성을 추가할 때 사용된다. 기본적으로 속성만 입력했을 때는 ""처럼 빈 문자열이 기본값이다.  
_피아노 에서는 keypress 이벤트에 쓸 함수에 사용할 data-press 속성과 keyup이벤트에 쓸 함수에 사용할 data-key속성을 이용해 새로운 속성값을 부여할 수 있었다._

## 1.2. CSS

### 1.2.1. transform: scale();

---

scale(가로, 세로),, 하나만 쓰면 가로세로 공통 적용
확대하는 효과!

### 1.2.2. border-color + box-shadow

---

이 피아노에서 border-color 와 box-shadow 에 동일한 색상을 부여하여 자연스럽게 강조되는 효과를 준다 . 기본 li 태그의 속성중 transition all .12s 가 있기에 더 자연스럽게 확장되는 느낌이다.

## 1.3. Javascript

### 1.3.1. addEventListener

---

`target.addEventListener(type, listener..);`
type 반응할 [이벤트 유형](https://developer.mozilla.org/ko/docs/Web/Events)을 나타냄, listener 지정된 타입의 이벤트 발생시 알림을 받는 객체

#### 1.3.2 keypress/ keyup

---

keypress : 키가 눌린 상태일 때 (연속적으로 실행됨)  
keyup : 키 누름이 해제될 때  
keydown : 키가 눌렸을 때 (불연속)  
_강의에서는 keydown을 이용해 구현했지만 키가 눌리는 동안 계속해서 소리가 나기를 원하는 것이 내 목표였기 때문에 keypress와 keydown 으로 바꿔 구현함_

#### 1.3.3 querySelector 사용시 class 가져오기

---

아래 예제처럼 정말 강력한 선택자도 사용할 수 있습니다. 예제의 결과는 클래스가 "user-panel main"인 `<div>(<div class="user-panel main">)` 안의, 이름이 "login"인 `<input>` 중 첫 번째 요소입니다.

> `var el = document.querySelector("div.user-panel.main input[name=login]");`

내 코드에서 쓰인 예시로는  
`` const audio = document.querySelector(`audio[data-press="${e.keyCode}"]`); `` 이다.
