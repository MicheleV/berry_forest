<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
<body>

  <script type="text/javascript">
    const url = 'http://{{local_ip}}:8080/'

    function api_led(route){
      fetch(url + route)
        .then(response => response.json())
        .then(data => console.log(data));
    }
  </script>

  <button type="button" id="yes" onclick="api_led('green')">Green</button>
  <hr>
  <button type="button" id="no" onclick="api_led('red')">Red</button>
  <hr>
  <button type="button" id="no" onclick="api_led('greetings')">Greeetings</button>
  <hr>
  <button type="button" id="no" onclick="api_led('temperature/external')">Room temperature</button>
  <hr>
  <button type="button" id="no" onclick="api_led('temperature/internal')">Pi's temperature</button>
</body>
