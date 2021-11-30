<h1>Ramzor ( Israeli COVID19 Monitoring System ) integration.</h1>

Original data source is https://corona.health.gov.il/ramzor/

<h2>Installation:</h2>

<h3>HACS installation:</h3>
<ul>
    <li>Open HACS</li>
    <li>Select  <b><i>"Integrations"</i></b></li>
    <li>Click on three dots, and select  <b><i>"Custom Repositories"</i></b></li>
    <li>Add this GitHub url (<a>https://github.com/dubilyer/ramzor_sensor</a>) and select <b><i>"Integration"</i></b> category </li>
    <li>Click  <b><i>"ADD"</i></b></li>
    <li><a href="#config">Update the configuration.yml</a></li>
</ul>
<h3>Manual installation</h3>
<ul>
    <li>Clone this project to your {config}/custom_components directory</li>
    <li><a href="#config">Update the configuration.yml</a></li>
    <li>Restart the HA</li>
</ul>

<h3 id=config>Configuration</h3>
<ul>
<li>Find your city code <a href="https://github.com/dubilyer/ramzor_sensor/tree/master/city_scrapper/cities.csv">here</a></li>
    <li>Add the following config tou your configuration.yml:
        <pre>
sensor:
    - platform: ramzor_sensor
      city: {your_city_code}
        </pre>
    Or just add the platform under the existing sensor tag if you already have one.
    </li>
</ul>

As a result you should have a sensor.grade in the device list with the % percent of infected in your city as a state.