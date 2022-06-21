window.onload=function() {


const showAnswerB = document.getElementsByClassName("showAnswerB")
const allAnswers = document.getElementsByClassName("answer")

let arr = new Array(showAnswerB.length)
arr.fill(0)

for (let i = 0; i < allAnswers.length; i++) {
	allAnswers[i].style.display = "none";
}

for (let i = 0; i < showAnswerB.length; i++) {
	showAnswerB[i].addEventListener("click", function() {
		if (arr[i] === 0) {
			allAnswers[i].style.display = "block";
			showAnswerB[i].textContent = "Hide answer"
			arr[i] = 1;
		} else if (arr[i] === 1) {
			allAnswers[i].style.display = "none";
			showAnswerB[i].textContent = "Show answer"
			arr[i] = 0;
		}
	});
}


}