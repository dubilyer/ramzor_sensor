<h1>Ramzor ( Israeli COVID19 Monitoring System ).</h1>

Original data source is https://corona.health.gov.il/ramzor/

<h2>Installation:</h2>

<ul>
    <li>Clone this project to your {config}/custom_components directory</li>
    <li>Find your city code in city_scrapper/cities.csv</li>
    <li>Add the following config tou your configuration.yml:
        <code>
            sensor:
                - platform: ramzor_sensor
                  city: {your_city_code}
        </code>
    </li>
    <li>Restart the HA</li>
</ul>

As a result you should have a sensor.grade in the device list with the % percent of infected in your city as a state.