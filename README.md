<h1>Ramzor ( Israeli COVID19 Monitoring System ) integration.</h1>

Original data source is https://corona.health.gov.il/ramzor/

<h4><i>! Attention, please make sure that you didn't miss the <a href=#config>configuration step</a> to configure city. Default one is Tel Aviv</i></h4>

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
<li>Find city codes <a href="https://github.com/dubilyer/ramzor_sensor/tree/master/city_scrapper/cities.csv">here</a></li>
    <li>Add the following config tou your configuration.yml:
        <pre>
sensor:
    - platform: ramzor_sensor
      cities: 
        - {city_code_1}
        - {city_code_2}
            . . .
        - {city_code_3}
        </pre>
    Or just add the platform under the existing sensor tag if you already have one.
    </li>
</ul>

As a result you should have a couple of sensors with the following naming convention:
 <pre>
    sensor.grade_{city_code_1}
    sensor.color_{city_code_1}
 </pre>

<h3 id=config>UI representation</h3>

I really love the idea of using it with `custom:button-card` (https://github.com/custom-cards/button-card).

That's an example of the config:

<pre>
  - type: custom:button-card
    icon: mdi:virus
    name: |
      [[[
        return `<span style="font-size: 3em; color:${states['sensor.color_2640'].state}">${states["sensor.grade_2640"].state}%</span>`;
      ]]]
    styles:
      icon:
        - color: |
            [[[
              return states["sensor.color_2640"].state;
            ]]]
</pre>

As a result having a percentage info and an icon colored in the corona state color:

![](https://github.com/dubilyer/ramzor_sensor/blob/multi_city/card.png?raw=true)
