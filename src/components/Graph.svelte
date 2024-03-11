<script>
  import { fly, draw } from "svelte/transition";
  import { tweened } from "svelte/motion";
  import { cubicOut, cubicInOut, sineIn } from "svelte/easing";
  import { new_cities } from "../data/new_cities"
  import { loop_guard } from "svelte/internal";
  import * as d3 from 'd3';
  import Map from "./Map.svelte";
  import { onMount } from 'svelte';
  import * as d3Hexbin from "d3-hexbin";


  export let index, width, height, geoJsonToFit, projection;

  // let arcGenerator = d3.arc()
  //   .innerRadius(10)
  //   .outerRadius(100)
  //   .padAngle(.02)
  //   .cornerRadius(4);

  // let pieAngleGenerator = d3.pie().value(d => d.length);
  // let arc_data = [];

  // let arc_color = d3.scaleOrdinal()
  //   .range(["blue", "red", "green", "purple", "orange"]);

  // let recorded_mouse_position = { x: 0, y: 0 };
  // let hovered = -1; 

  // // Filtered data
  // let eventTypes = ["Explosions/Remote violence", "Battles", "Strategic developments", "Violence against civilians", "Protests"];
  // let filteredData = eventTypes.map(type => new_cities.features.filter(feature => feature.properties.event === type));

  // // Calculate data for the pie chart
  // $: {
  //   arc_data = pieAngleGenerator(filteredData.map(data => data.length));
  // }
  let svg;
  const tweenOptions = {
    delay: 0,
    duration: 10,
  };

  const tweenedX_UA = tweened(
    new_cities.features.map((new_cities) => projection(new_cities.geometry.coordinates)[0]),
    tweenOptions
  );

  const tweenedY_UA = tweened(
    new_cities.features.map((new_cities) => projection(new_cities.geometry.coordinates)[1]),
    tweenOptions
  );

  $: tweenedData_UA = new_cities.features.map((new_cities, i) => ({
    x: $tweenedX_UA[i],
    y: $tweenedY_UA[i],
    properties: new_cities.properties,
  }));

  $: {
    tweenedX_UA.set(new_cities.features.map((new_cities) => width / 2));
    tweenedY_UA.set(new_cities.features.map((city, i) => height / 2 + i * 20));


    tweenedX_UA.set(
      new_cities.features.map((new_cities) => projection(new_cities.geometry.coordinates)[0])
    );
    tweenedY_UA.set(
      new_cities.features.map((new_cities) => projection(new_cities.geometry.coordinates)[1])
    );
  }

  // Define your filter condition
  const filter_E = (feature) => {
    return (
      feature.properties.event === "Explosions/Remote violence"
    );
  };

  const filter_B = (feature) => {
    return (
      feature.properties.event === "Battles"
    );
  };

  const filter_S = (feature) => {
    return (
      feature.properties.event === "Strategic developments"
    );
  };

  const filter_V = (feature) => {
    return (
      feature.properties.event === "Violence against civilians"
    );
  };

  const filter_P = (feature) => {
    return (
      feature.properties.event === "Protests"
    );
  };

  // Filter the features
  $: UA_E = new_cities.features.filter(filter_E);
  $: UA_B = new_cities.features.filter(filter_B);
  $: UA_S = new_cities.features.filter(filter_S);
  $: UA_V = new_cities.features.filter(filter_V);
  $: UA_P = new_cities.features.filter(filter_P);

  // $: svg = d3.create("svg")
  //   .attr("viewBox", [0, 0, width, height])
  //   .attr("width", width)
  //   .attr("height", height)
  //   .attr("style", "max-width: 100%; height: auto;");
 

  // $: hexbin = d3Hexbin.hexbin()
  //     .extent([[0, 0], [width, height]])
  //     .radius(10);

  // $: bins = hexbin(new_cities.features.map(d => projection(d.geometry.coordinates)));
  // // $: color = d3.scaleSequential(d3.extent(bins, d => d.date), d3.interpolateSpectral);
  // $: radius = d3.scaleSqrt([0, d3.max(bins, d => d.length)], [0, hexbin.radius() * Math.SQRT2]);
  // $: {
  //   if (svg) {
  //     svg.append("g")
  //       .attr("transform", "translate(580,20)")
  //       .append(() => legend({
  //         color, 
  //         title: "Median opening year", 
  //         width: 260, 
  //         tickValues: d3.utcYear.every(5).range(...color.domain()),
  //         tickFormat: d3.utcFormat("%Y")
  //       }));
  //   }
  // }
</script>

<svg class="graph">
  <g class = "legend" stroke = "#000">
    <text x = "1070px" y = "105px" style = "font-size: 22" font-weight = bold> Explosions/Remote violence</text>
    <circle
    key = 1
    cx = 1050px
    cy = 100px
    fill = "blue"
    r = "15"
    on:click = {() => {
      UA_B = null;
      UA_S = null;
      UA_V = null;
      UA_P = null;
    }}
    />
    <text x = "1070px" y = "145px" style = "font-size: 22"> Battles</text>
    <circle
    key = 1
    cx = 1050px
    cy = 140px
    fill = "red"
    r = "15"
    on:click = {() => {
      UA_E = null;
      UA_S = null;
      UA_V = null;
      UA_P = null;
    }}
    />
    <text x = "1070px" y = "185px" style = "font-size: 22"> Strategic developments</text>
    <circle
    key = 1
    cx = 1050px 
    cy = 180px
    fill = "green"
    r = "15"
    on:click = {() => {
      UA_E = null;
      UA_B = null;
      UA_V = null;
      UA_P = null;
    }}
    />
    <text x = "1070px" y = "225px" style = "font-size: 22"> Violence against civilians</text>
    <circle
    key = 1
    cx = 1050px
    cy = 220px
    fill = "purple"
    r = "15"
    on:click = {() => {
      UA_E = null;
      UA_B = null;
      UA_S = null;
      UA_P = null;
    }}
    />
    <text x = "1070px" y = "265px" style = "font-size: 22"> Protests</text>
    <circle
    key = 1
    cx = 1050px
    cy = 260px
    fill = "orange"
    r = "15"
    on:click = {() => {
      UA_E = null;
      UA_B = null;
      UA_S = null;
      UA_V = null;
    }}
    />
    <text 
    key = 1
    x = "1050" 
    y = "347" 
    fill = 'black'
    style = "font-size: 22"
    on:click = {() => {
      UA_E = new_cities.features.filter(filter_E);
      UA_B = new_cities.features.filter(filter_B);
      UA_S = new_cities.features.filter(filter_S);
      UA_V = new_cities.features.filter(filter_V);
      UA_P = new_cities.features.filter(filter_P);
    }} 
    > Reset Filter</text>
</g>

{#each tweenedData_UA as new_cities, i}
    {#if new_cities.x && new_cities.y}
        <!-- Determine fill color based on event type -->
        {#if UA_E[i]}
            <circle cx={new_cities.x} cy={new_cities.y} r=5 fill="blue">
                <title>{new_cities.properties.city}</title>
            </circle>
        {/if}
        {#if UA_B[i]}
            <circle cx={new_cities.x} cy={new_cities.y} r=5 fill="red">
                <title>{new_cities.properties.city}</title>
            </circle>
        {/if}
        {#if UA_S[i]}
            <circle cx={new_cities.x} cy={new_cities.y} r=5 fill="green">
                <title>{new_cities.properties.city}</title>
            </circle>
        {/if}
        {#if UA_V[i]}
            <circle cx={new_cities.x} cy={new_cities.y} r=5 fill="purple">
                <title>{new_cities.properties.city}</title>
            </circle>
        {/if}
        {#if UA_P[i]}
            <circle cx={new_cities.x} cy={new_cities.y} r=5 fill="orange">
                <title>{new_cities.properties.city}</title>
            </circle>
        {/if}
    {/if}
  {/each}
</svg>


<style>
  .graph {
    width: 100%;
    height: 80vh;
    position: relative;
    outline: rgb(0, 94, 255) solid 7px;
  }

  .visualization {
    font: 25px sans-serif;
    margin: auto;
    text-align: middle;
  }

  /* dynamic classes for the tooltip */
  .tooltip-hidden {
    visibility: hidden;
    font-family: "Nunito", sans-serif;
    width: 200px;
    position: absolute;
  }

  .tooltip-visible {
    font: 25px sans-serif;
    font-family: "Nunito", sans-serif;
    visibility: visible;
    background-color: #f0dba8;
    border-radius: 10px;
    width: 200px;
    color: black;
    position: absolute;
    padding: 10px;
  }

  .legend circle[key = "1"]:hover{
      cursor: pointer;
      opacity: 0.60;
  }
  
  .legend text[key = "1"]:hover{
      cursor: pointer;
  }
</style>