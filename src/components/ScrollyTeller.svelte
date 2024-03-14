<script>
  import Scroller from "@sveltejs/svelte-scroller";
  import Map from "./Map.svelte";
  import { geoMercator } from "d3-geo";
  import Graph from "./Graph.svelte";
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  import Graph2 from './graph2.svelte';
  import { fade } from 'svelte/transition';

  let count, index, offset, progress;
  let width, height;
  let data = [];
  let tempData = [];

  let geoJsonToFit = {
    type: "FeatureCollection",
    features: [
      {
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: [1, 0],
        },
      },
      {
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: [0, 1],
        },
      },
    ],
  };

  $: projection = geoMercator().fitSize([width, height], geoJsonToFit);

  onMount(async () => {
    const res = await fetch('gdp_co2_death.csv');
    const text = await res.text();
    tempData = d3.csvParse(text, d3.autoType);

    // Parse date fields and create a new 'date' variable
    data = tempData.map(d => ({
      ...d,
      date: new Date(d.Year, 0) // Assuming 'Year' is the name of your date field
    }));
  });
</script>

<Scroller
  top={0.0}
  bottom={1}
  threshold={0.5}
  bind:count
  bind:index
  bind:offset
  bind:progress
>
  <div 
      class="background"
      slot="background"
      bind:clientWidth={width}
      bind:clientHeight={height}
      >
    {#if index<1}
      <Map bind:geoJsonToFit {index}/>
    {/if}
    <div class="progress-bars">
      <p>current section: <strong>{index + 1}/{count}</strong></p>
      <progress value={count ? (index + 1) / count : 0} />

      <p>offset in current section</p>
      <progress value={offset || 0} />

      <p>total progress</p>
      <progress value={progress || 0} />
    </div>
  </div>

  <div class="foreground" slot="foreground">
    <section class='graph'>
      <h1>
        <strong style="color: black; font-family: 'Raleway',sans-serif; font-size: 62px; font-weight: 800; line-height: 72px; margin: 0 0 24px; text-align: center; text-transform: uppercase;">UKRAINE CONFLICTS</strong>
      </h1>
      <Graph {index} {width} {height} {geoJsonToFit} {projection} />
      <h2 class="blurb_head">
        The ongoing conflict in Ukraine has captured global attention since its inception. As we delve into the intricate details of this conflict, one thing becomes strikingly clear – behind every statistic lies a story of human suffering, resilience, and the relentless pursuit of peace. Join us as we unravel the layers of the Ukraine conflicts, exploring the data, events, and narratives that define this tumultuous chapter in modern history.
      </h2>
      
    </section>

    <section class="story">
      <h2 class='subheading'>
        Storytelling:
      </h2>
      <p class='blurb'>
        Our journey begins with a snapshot of the latest developments in the Ukraine conflict. From the bustling streets of Donetsk to the tranquil shores of Crimea, the region is a mosaic of violence, political upheaval, and humanitarian crisis. The conflict has left no corner untouched, with each day bringing new challenges and tragedies.
      </p>
    
      <p class='blurb'>
        In the Donetsk region, Russian forces assert their control, pushing further into Ukrainian territory with each advance. The villages of Stepove, Sieverne, and Lastochkyne now bear witness to the scars of war, their streets echoing with the cries of displaced families and the rumble of military convoys. Amidst these territorial gains, a stark reminder of the human cost emerges – drone footage captures the harrowing moment as Ukrainian servicemen, unarmed and outnumbered, face the ultimate betrayal at the hands of their adversaries.
      </p>
    
      <p class='blurb'>
        But the conflict is not confined to Donetsk alone. In the Zaporizhia region, the clash of arms continues unabated, a testament to the resilience of both Ukrainian forces and civilian populations caught in the crossfire. Further south, near Orikhiv and Huliaipole, the sounds of battle serve as a grim backdrop to everyday life, reminding residents that peace remains a distant dream.
      </p>
    
      <p class='blurb'>
        As the conflict spills over into neighboring regions, the toll on civilians becomes painfully clear. From Kharkiv to Kherson, innocent lives are lost in senseless acts of violence – shelling, airstrikes, and drone strikes claim victims indiscriminately, leaving communities shattered and futures uncertain. The week sees a staggering number of civilian casualties, a stark reminder of the human tragedy unfolding amidst the chaos of war.
      </p>
    
      <p class='blurb'>
        Yet amidst the darkness, there are glimmers of hope. Ukrainian forces strike back with precision and determination, targeting key military installations in Crimea and sending a message of defiance to their aggressors. In occupied territories, acts of resistance emerge – from suspected partisan attacks to symbolic acts of defiance, the spirit of resistance remains alive and well.
      </p>
    
      <p class='blurb'>
        As we reflect on the events of the past week, one thing becomes abundantly clear – the Ukraine conflict is far from over. But amidst the despair and destruction, there remains a flicker of hope – hope for peace, hope for justice, and hope for a future where the people of Ukraine can once again live in peace and prosperity.
      </p>

      <img src="tank.png" alt="Tank" style="display: block; margin: 0 auto;">
    </section>

    <section class='graph'>
      <h3 style='text-align:left;' class='subheading'>Investigating Decrease in Conflicts Since World War II</h3>
      <div style="margin: 0 auto; max-width: 950px;">
        <p style="text-align:left; font-size:23px; line-height:100%">
          Worldwide Conflict Trends
        </p>
      </div>
      <br>
      <Graph2 {data} />
      <div style="margin: 0 auto; max-width: 1000px;">
        <div style="margin: 0 auto; max-width: auto;">
          <h4 style="text-align:left;">Investigation Summary: Understanding the Decline in Conflict</h4>
          <p class='blurb'>
            Our investigation delves into the dataset of conflicts worldwide since World War II, with a particular focus on the ongoing Ukraine conflict. Through extensive research, we have analyzed historical data, scholarly articles, and reports to uncover trends and patterns in global conflicts.
            We have identified a significant decrease in conflicts since the end of World War II, reflecting changes in geopolitical dynamics, international diplomacy, and advancements in peacekeeping efforts.
            Despite this overall decline, the Ukraine conflict remains a pertinent topic of investigation, drawing attention to persisting tensions and challenges in the region.
          </p>
          <br>
          <p class='blurb'>
            Our investigation presents several challenges, including the integration of interactive features to enhance user engagement and understanding. We anticipate that visualizing the data effectively, particularly regarding the Ukraine conflict, will require careful consideration of layout, functionality, and storytelling techniques.
            Addressing these challenges will involve meticulous attention to detail and experimentation with various visualization methods to ensure a comprehensive and informative exploration of the dataset.
          </p>
        </div>
        <br>
      </div>
    </section>

    <section class='graph'>
      <h3 style='text-align:left;'class='subheading'>Takeaway</h3>
      <div style="margin: 0 auto; max-width: 1000px;">
        <div style="margin: 0 auto; max-width: auto;">
          <p class='blurb'>
            The key takeaway from our project is the importance of effectively visualizing complex datasets to understand the severity and trends of conflicts in specific locations over time. By utilizing a map to pinpoint areas of heightened conflict and a time flow circle chart to illustrate the fluctuations in conflict numbers, we aim to provide insight into the dynamics of these conflicts.
          </p>
          <br>
          <p class='blurb'>
            Our project emphasizes the challenges and complexities involved in importing and presenting data accurately. We encountered difficulties in handling datasets and implementing visualization functions, particularly with the flexibility of D3.js. Despite encountering errors and spending significant time troubleshooting, we ultimately succeeded in creating visualizations that convey the intended message.
          </p>
          <br>
          <p class='blurb'>
            However, we acknowledge that the complexity of the layout and functionality may present obstacles in the learning process. It requires a deep understanding of the momentum and algorithms behind each visualization function to ensure accurate representation. Despite these challenges, our project demonstrates the importance of perseverance and adaptability in navigating through complex data visualization tasks.
          </p>
        </div>
      </div>
    </section>
  </div>
</Scroller>

<style>
  .background {
      width: 100%;
      height: 100vh;
      position: relative;
  }

  .foreground {
      width: 100%;
      opacity: 1;
      margin: 0 auto;
      height: auto;
      position: relative;
  }

  .progress-bars {
      position: absolute;
      background: rgba(170, 51, 120, 0.2); /* 40% opaque */
      visibility: hidden;
  }

  section {
      height: 700vh;
      background-color: rgba(255, 255, 255, 0); /* 20% opaque */
      border-radius: 25px;
      text-align: center;
      color: rgb(0, 0, 0);
      padding: 1em;
      margin: 0 0 2em 0;
  }

  .story{
    height: 110vh;
  }

  .graph {
      height: 100vh;
  }

  .subheading {
    color: black; 
    font-family: 'Raleway',sans-serif; 
    font-size: 30px; 
    font-weight: 800; 
    line-height: 72px; 
    margin: 0 0 24px; 
    text-align: left; 
    text-transform: uppercase;
  }

  .blurb {
      font-family: 'Nunito', sans-serif;
      text-align: left;
      font-size: 18px;
      font-weight: 300;
      line-height: 1.5;
      padding: 0 20px; /* Add some padding to the sides for better readability */
      margin: 0 auto; 
      max-width: 1000px;
  }

  .blurb_head{
    font-family: 'Nunito', sans-serif;
    text-align: left;
    font-size: 18px;
    font-weight: 300;
    line-height: 1.5;
    padding: 0 20px; /* Add some padding to the sides for better readability */
    margin: 0 auto; 
    max-width: 1000px;
    background-color: rgba(255, 255, 255, 0.6);
    border-radius: 25px;
  }
  </style>
