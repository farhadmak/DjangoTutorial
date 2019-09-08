function retrieveMap(){
  console.log("hello");
  let lat = document.getElementById('latitude').value;
  let lon = document.getElementById('longitude').value;
  let csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;
  console.log(csrf);

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
      console.log(data);
    })
}
