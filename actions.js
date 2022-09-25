function openForm(id) {
    document.getElementById(id).style.display = "block";
  }
  
  function closeForm(id) {
    document.getElementById(id).style.display = "none";
  }

/* button for plus and minus AND */
  window.onload=function(){
    var minusBtn = document.getElementById("minus"),
        plusBtn = document.getElementById("plus"),
        numberPlace = document.getElementById("numberPlace"),
        submitBtn = document.getElementById("submit"),
        number = 0, /// number value
        min = 0, /// min number
        max = 100; /// max number
        
    minusBtn.onclick = function(e){
        e.preventDefault();
        if (number>min){
           number = number-1; /// Minus 1 of the number
           numberPlace.innerText = number ; /// Display the value in place of the number
        }
        if(number == min) {        
            numberPlace.style.color= "red";
            setTimeout(function(){numberPlace.style.color= "black"},500)
        }
        else {
          numberPlace.style.color="black";            
           }
                
    }
    plusBtn.onclick = function(e){
        e.preventDefault();
        if(number<max){
           number = number+1;
           numberPlace.innerText = number ; /// Display the value in place of the number
        }     
        if(number == max){
               numberPlace.style.color= "red";
               setTimeout(function(){numberPlace.style.color= "black"},500)
        }
           
        else {
               numberPlace.style.color= "black";
               
        }
     
           
/* BRUTE FORCE BUTTON */

/* */

    }
    submitBtn.onclick = function(){
        alert("you choice : " + number);
    }
    
}

