<h1>Ramzor ( Israeli COVID19 Monitoring System ).</h1>

Original data source is https://corona.health.gov.il/ramzor/

<h2>Installation:</h2>

<ul>
    <li>Clone this project to your {config}/custom_components directory</li>
    <li>Find your city code <a href="https://github.com/dubilyer/ramzor_sensor/tree/master/city_scrapper/cities.csv">here</a></li>
    <li>Add the following config tou your configuration.yml:
        <pre>
sensor:
    - platform: ramzor_sensor
      city: {your_city_code}
        </pre>
    </li>
    <li>Restart the HA</li>
</ul>

As a result you should have a sensor.grade in the device list with the % percent of infected in your city as a state.