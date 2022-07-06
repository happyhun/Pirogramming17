let seconds = 0; // 초
let tenMillis = 0; // 밀리초

const appendTens = document.getElementById("tenMillis");
const appendSeconds = document.getElementById("seconds");
const recordList = document.querySelector(".record-list");
const allCheck = document.querySelector(".allCheck");
const del = document.querySelector(".del");

const buttonStart = document.getElementById("bt__start");
const buttonStop = document.getElementById("bt__stop");
const buttonReset = document.getElementById("bt__reset");

let intervalId;

buttonStart.onclick = function () {
  clearInterval(intervalId); // 반복중단 (start를 여러번 누르면 setInterval이 여러번 호출되어 속도가 빨라지므로 필요함)
  intervalId = setInterval(operateTimer, 10); // 10ms마다 operateTimer 호출
};

buttonStop.onclick = function () {
  clearInterval(intervalId);
  const li = document.createElement("li");
  const span = document.createElement("span");
  const input = document.createElement("input");
  input.setAttribute("type", "checkbox");
  input.setAttribute("class", "check");

  span.innerText =
    (seconds > 9 ? seconds : "0" + seconds) +
    ":" +
    (tenMillis > 9 ? tenMillis : "0" + tenMillis);
  li.appendChild(input);
  li.appendChild(span);
  recordList.append(li);
};

buttonReset.onclick = function () {
  // 반복중단 후 값 초기화
  clearInterval(intervalId);
  tenMillis = 0;
  seconds = 0;
  appendTens.textContent = "00";
  appendSeconds.textContent = "00";
};

function operateTimer() {
  // 출력할 시간을 계산한다
  tenMillis++;
  appendTens.textContent = tenMillis > 9 ? tenMillis : "0" + tenMillis; // 9보다 작으면 0을 붙여준다
  if (tenMillis > 99) {
    //100ms는 1초
    seconds++;
    appendSeconds.textContent = seconds > 9 ? seconds : "0" + seconds;
    tenMillis = 0;
    appendTens.textContent = "00";
  }
}

allCheck.onclick = function () {
  let list = document.querySelectorAll(".check");
  if (allCheck.checked) {
    for (let i = 0; i < list.length; i++) {
      list[i].checked = true;
    }
  } else {
    for (let i = 0; i < list.length; i++) {
      list[i].checked = false;
    }
  }
};

del.onclick = function () {
  let list = document.querySelectorAll(".check");
  for (let i = 0; i < list.length; i++) {
    if (list[i].checked) {
      list[i].parentElement.remove();
    }
  }
};
