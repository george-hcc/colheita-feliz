
var myChart;
console.log(myChart);

//Button Html generator//


const renderButtons = function (data,deviceName,deviceId,unit){
  var lastElementValue = data.status[data.status.length-1].value;
  const html =` 
  <button class="graphButton${deviceId}">
            <p>${deviceName} </p>
            <p> ${lastElementValue}${unit}</p>
            <canvas id="myChart${deviceId}" ></canvas>
  </button>
        `;

        document.querySelector(".buttonsDiv").insertAdjacentHTML("beforeend", html);
}
//Function that reads/saves the json and plots a graph with his datas

const grabButton = function (deviceName,deviceId,unit){

    const request= new XMLHttpRequest();
    request.open('GET',`https://colheita-feliz.herokuapp.com/api/get/status/${deviceId}/week/`);
    request.send();

    request.addEventListener('load',function(){

        const data= JSON.parse(request.responseText)
        
        

        var value= data.status.map(function(elem){
            return elem.value;
            
        })
        var measurement_timestamp= data.status.map(function(elem){
      
            return elem.measurement_timestamp;
        })


renderButtons(data,deviceName,deviceId,unit);

document.querySelector(`.graphButton${deviceId}`).addEventListener('dblclick',function(){
 myChart.destroy();
});
document.querySelector(`.graphButton${deviceId}`).addEventListener('click',function(){

  if(myChart != null){
    console.log('destroy');
    myChart.destroy();
    myChart=null;
 }    
 else{
   myChart = new Chart(document.getElementById(`myChart${deviceId}`).getContext("2d"), {
      type: 'line',
      data: {
        labels: measurement_timestamp,
        datasets: [{ 
            data: value,
            label: deviceName,
            borderColor: "#180cbd",
            backgroundColor: "#180cbd",
            fill: false
          }]
          },
      options: {
        title: {
          display: true,
  
        },
        responsive: true,
        maintainAspectRatio: true,
        scales:{ 
          y: {
          ticks: {
          }
      },
      x: {
        ticks: {
  
        }
    }
    }
      }
     
    
  })
} 
  
    })
  
})

}




//Function responsible for reading the number of devices from a person, the name and data type of those device
const grabDevice = function (deviceNum){
const reqDevices= new XMLHttpRequest();
    reqDevices.open('GET',`https://colheita-feliz.herokuapp.com/api/get/devices/${deviceNum}/`);
    reqDevices.send();

    reqDevices.addEventListener('load',function(){

      const dataDevices= JSON.parse(reqDevices.responseText)
        
      var deviceId= dataDevices.devices.map(function(elem){
        return elem.device_id;
          
      })
      console.log(deviceId)

      var deviceName= dataDevices.devices.map(function(elem){
        return elem.name;
        
      })
      console.log(deviceName)

      var unit= dataDevices.devices.map(function(elem){
          return elem.unit;
            
        })
      console.log(unit)

      var lastData= dataDevices.devices.map(function(elem){
      
          return elem.last_data;
        })
        console.log(lastData)

      //Creates a variable with the lenght of id numbers
      const deviceIdLenght=deviceId.length
      console.log(deviceIdLenght);

      //Calls the function for creating the graphs and buttons for each device
        for(i=0;i<=deviceIdLenght-1;i++){
          grabButton(deviceName[i],deviceId[i],unit[i])
          console.log(i);

        }
      })}

grabDevice('1')