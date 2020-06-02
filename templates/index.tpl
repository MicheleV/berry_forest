<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<body>

  <script type="text/javascript">

    function api_led(route){
      fetch(route)
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            return {'status' : 'The server does not look happy'}
          }
        })
        .then(data => console.log(data));
    }
  </script>

  <button type="button" id="yes" onclick="api_led('/green')">Green</button>
  <hr>
  <button type="button" id="no" onclick="api_led('/red')">Red</button>
  <hr>
  <button type="button" id="no" onclick="api_led('/greetings')">Greeetings</button>
  <hr>
  <button type="button" id="no" onclick="api_led('/temperature/external')">Room temperature</button>
  <hr>
  <button type="button" id="no" onclick="api_led('/temperature/internal')">Pi's temperature</button>
</body>
