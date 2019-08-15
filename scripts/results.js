const vote = document.querySelectorAll(".card");
let canVote = true;
let button = document.querySelector('#grey-button');
for (let i = 0; i < vote.length; i++){
  //add eventListener to each element with a card class
  vote[i].addEventListener('mouseenter', function(){

    button = vote[i].childNodes[1];
    console.log(button)
    button.style.opacity = '1';
  })
  vote[i].addEventListener('mouseleave', function(){

    button = vote[i].childNodes[1];
    console.log(button.src)
    if(button.src != "http://localhost:8080/images/votebutton.png"){
      button.style.opacity = '0';
    }

  })

  vote[i].addEventListener('click', function(){
    vote[i].style = '20px';
    if (canVote === true) {
      vote[i].style.transform = 'rotate(360deg)';
      vote[i].style.transition = '1s all';
      vote[i].childNodes[1].src = "/images/votebutton.png"
      canVote = false;
    }
  });
}
