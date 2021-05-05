
const fucki= function (work){

const req= new XMLHttpRequest();
    req.open('GET','https://colheita-feliz.herokuapp.com/api/get/status/1/day/');
    req.send();

    req.addEventListener('load',function(){
        
        const data= JSON.parse(req.responseText)
        console.log(data);
        

    })
}