function retrieveMap(){
  // console.log("hello");
  let lat = document.getElementById('latitude').value;
  let lon = document.getElementById('longitude').value;
  let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  // console.log(csrf);

  let body = {
    lat: lat,
    lon: lon,
    csrfmiddlewaretoken: csrf,
  }

  fetch('/', {
        method: 'post',
        credentials: 'include',
        headers: {
            'Content-Type': 'text/plain',
            'X-CSRFToken' : csrf,
        },
        credentials: 'same-origin',
        body: JSON.stringify(body)
    }).then((res) => {
        return res.json();
    }).then((data) => {
      var mapProp= {
        center:new google.maps.LatLng(parseFloat(data.lat), parseFloat(data.lon)),
        zoom:12,
      };
      var map = new google.maps.Map(document.getElementById("map"),mapProp);
      
      var marker = new google.maps.Marker({
          // The below line is equivalent to writing:
          // position: new google.maps.LatLng(-34.397, 150.644)
          position: {lat: parseFloat(data.lat), lng: parseFloat(data.lon)},
          map: map
        });
      console.log(data);
    })
}
