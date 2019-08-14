const vote = document.querySelectorAll(".card");

for (let i = 0; i < vote.length; i++){
  //add eventListener to each element with a card class
  vote[i].addEventListener('click', function(){
    vote[i].style = '20px';
    vote[i].style.transform = 'rotate(360deg)';
    vote[i].style.transition = '1s all';
  });
}
