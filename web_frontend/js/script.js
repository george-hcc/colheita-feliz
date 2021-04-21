'use strict';

fetch("./first.json")
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        console.log(data);
    });


/*const request = new XMLHttpRequest();
    request.open('GET','https://colheita-feliz.herokuapp.com/api/get/status/1/week/');
    request.send();
    console.log(request.responseText);
    
    request.addEventListener('load',function(){
        console.log(this.responseText);
    })*/