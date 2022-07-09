window.onload=function() {

const sidebarHomeB = document.getElementById("sidebarHomeB")

sidebarHomeB.addEventListener("click", function() {
	window.location.href = "/";
})

document.getElementById("navAlgebra").style.display = "none";
document.getElementById("navGeometry").style.display = "none";
document.getElementById("navPrecalculus").style.display = "none";
document.getElementById("navCalculusI").style.display = "none";

const userSelection = document.getElementsByClassName('navB');
const algebraSelection = document.getElementsByClassName("navAlgebraB")
const geometrySelection = document.getElementsByClassName("navGeometryB")
const precalculusSelection = document.getElementsByClassName("navPrecalculusB")
const calculusISelection = document.getElementsByClassName("navCalculusIB")

for(let i = 0; i < userSelection.length; i++) {
  userSelection[i].addEventListener("mousemove", function() {
  	switch(i) {
    	case 1:
			document.getElementById("navAlgebra").style.display = "block";
			document.getElementById("navGeometry").style.display = "none";
			document.getElementById("navPrecalculus").style.display = "none";
			document.getElementById("navCalculusI").style.display = "none";
			break;
       	case 2:
	       	document.getElementById("navAlgebra").style.display = "none";
       		document.getElementById("navGeometry").style.display = "block";
       		document.getElementById("navPrecalculus").style.display = "none";
			document.getElementById("navCalculusI").style.display = "none";
			break;
       	case 3:
	       	document.getElementById("navAlgebra").style.display = "none";
       		document.getElementById("navGeometry").style.display = "none";
       		document.getElementById("navPrecalculus").style.display = "block";
			document.getElementById("navCalculusI").style.display = "none";
			break;
       	case 4:
	       	document.getElementById("navAlgebra").style.display = "none";
       		document.getElementById("navGeometry").style.display = "none";
       		document.getElementById("navPrecalculus").style.display = "none";
			document.getElementById("navCalculusI").style.display = "block";
			break;
       	default:
       		document.getElementById("navAlgebra").style.display = "none";
			document.getElementById("navGeometry").style.display = "none";
			document.getElementById("navPrecalculus").style.display = "none";
			document.getElementById("navCalculusI").style.display = "none";
       		break;
    }
  })
}

for (let i = 0; i < algebraSelection.length; i++) {
	algebraSelection[i].addEventListener("click", function () {
		switch(i){
			case 1:
				document.querySelector("#navAlgebra :nth-child(2)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 2:
				document.querySelector("#navAlgebra :nth-child(3)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 3:
				document.querySelector("#navAlgebra :nth-child(4)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 4:
				document.querySelector("#navAlgebra :nth-child(5)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 5:
				document.querySelector("#navAlgebra :nth-child(6)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 6:
				document.querySelector("#navAlgebra :nth-child(7)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 7:
				document.querySelector("#navAlgebra :nth-child(8)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 8:
				document.querySelector("#navAlgebra :nth-child(9)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			case 9:
				document.querySelector("#navAlgebra :nth-child(10)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/algebra/" + algebraSelection[i].textContent; break;
			default:
				;
		}
	})
}

for (let i = 0; i < geometrySelection.length; i++) {
	geometrySelection[i].addEventListener("click", function () {
		switch(i){
			case 1:
				document.querySelector("#navGeometry :nth-child(2)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 2:
				document.querySelector("#navGeometry :nth-child(3)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 3:
				document.querySelector("#navGeometry :nth-child(4)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 4:
				document.querySelector("#navGeometry :nth-child(5)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 5:
				document.querySelector("#navGeometry :nth-child(6)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 6:
				document.querySelector("#navGeometry :nth-child(7)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 7:
				document.querySelector("#navGeometry :nth-child(8)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 8:
				document.querySelector("#navGeometry :nth-child(9)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			case 9:
				document.querySelector("#navGeometry :nth-child(10)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/geometry/" + geometrySelection[i].textContent; break;
			default:
				;
		}
	})
}

for (let i = 0; i < precalculusSelection.length; i++) {
	precalculusSelection[i].addEventListener("click", function () {
		switch(i){
			case 1:
				document.querySelector("#navPrecalculus :nth-child(2)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 2:
				document.querySelector("#navPrecalculus :nth-child(3)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 3:
				document.querySelector("#navPrecalculus :nth-child(4)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 4:
				document.querySelector("#navPrecalculus :nth-child(5)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 5:
				document.querySelector("#navPrecalculus :nth-child(6)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 6:
				document.querySelector("#navPrecalculus :nth-child(7)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 7:
				document.querySelector("#navPrecalculus :nth-child(8)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 8:
				document.querySelector("#navPrecalculus :nth-child(9)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			case 9:
				document.querySelector("#navPrecalculus :nth-child(10)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/precalculus/" + precalculusSelection[i].textContent; break;
			default:
				;
		}
	})
}

for (let i = 0; i < calculusISelection.length; i++) {
	calculusISelection[i].addEventListener("click", function () {
		switch(i){
			case 1:
				document.querySelector("#navCalculusI :nth-child(2)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 2:
				document.querySelector("#navCalculusI :nth-child(3)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 3:
				document.querySelector("#navCalculusI :nth-child(4)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 4:
				document.querySelector("#navCalculusI :nth-child(5)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 5:
				document.querySelector("#navCalculusI :nth-child(6)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 6:
				document.querySelector("#navCalculusI :nth-child(7)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 7:
				document.querySelector("#navCalculusI :nth-child(8)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 8:
				document.querySelector("#navCalculusI :nth-child(9)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			case 9:
				document.querySelector("#navCalculusI :nth-child(10)").style.color = "#0645AD";
				window.location.href = document.location.origin + "/calculusI/" + calculusISelection[i].textContent; break;
			default:
				;
		}
	})
}

}
