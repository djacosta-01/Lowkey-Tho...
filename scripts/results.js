const vote = document.querySelectorAll(".card");
let canVote = true;

for (let i = 0; i < vote.length; i++){
  //add eventListener to each element with a card class

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
