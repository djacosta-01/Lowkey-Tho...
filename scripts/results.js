'use strict';

const vote = document.querySelectorAll(".card");
let canVote = true;

for (let i = 0; i < vote.length; i++){
  console.log(vote[i]);
  vote[i].addEventListener('mouseenter', () => greyCheckOn(vote[i]));
  vote[i].addEventListener('mouseout', () => greyCheckOff(vote[i]));
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

function greyCheckOn(card){
    card.childNodes[1].style.display="block";
    console.log(card);
}

function greyCheckOff(card){
    card.childNodes[1].style.display="none";
    console.log(card);
}
