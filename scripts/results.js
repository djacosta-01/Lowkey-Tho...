'use strict';

const vote = document.querySelectorAll(".card");
let canVote = true;
let button = document.querySelector('#grey-button');
for (let i = 0; i < vote.length; i++){
  //add eventListener to each element with a card class
  vote[i].addEventListener('mouseenter', function(){
    if (canVote === true) {
      button = vote[i].childNodes[1];
      console.log(button)
      button.style.opacity = '1';
    }
  })
  vote[i].addEventListener('mouseleave', function(){
    button = vote[i].childNodes[1];
    console.log(button.src);
    // button.src != "/images/votebutton.png"
    if(canVote===true){
      button.style.opacity = '0';
    }
  })

  vote[i].addEventListener('click', function(){
    vote[i].style = '20px';
    if (canVote === true) {
      // Update the score in the database
      fetch('/scores', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
          order: i + 1,
        })
      }).then(r => r.text()).then(text => {
        if (text === 'true') {
          vote[i].style.transform = 'rotate(360deg)';
          vote[i].style.transition = '1s all';
          vote[i].childNodes[1].src = "/images/votebutton.png";
          canVote = false;
          alert('Thanks! Vote Counted');
        } else {
          alert('Please wait until all players have submitted');
        }
      }).catch(e => console.log(e));
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
