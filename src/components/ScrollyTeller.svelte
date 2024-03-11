<script>
  import Scroller from "@sveltejs/svelte-scroller";
  import Map from "./Map.svelte";
  import { geoMercator } from "d3-geo";
  import Graph from "./Graph.svelte";
  import { onMount } from 'svelte';
  import * as d3 from 'd3';
  import Graph2 from './graph2.svelte';

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
        <strong>UKRAINE CONFLICTS</strong>
      </h1>
      <h2 class="subheading">
        The ongoing conflict in Ukraine has captured global attention since its inception. As we delve into the intricate details of this conflict, one thing becomes strikingly clear – behind every statistic lies a story of human suffering, resilience, and the relentless pursuit of peace. Join us as we unravel the layers of the Ukraine conflicts, exploring the data, events, and narratives that define this tumultuous chapter in modern history.
      </h2>
      <Graph {index} {width} {height} {geoJsonToFit} {projection} />
    </section>

    <section>
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
    </section>

    <section class='graph'>
      <h3>Topic: Story telling about the Ukraine Conflicts progress</h3>
      <div style="margin: 0 auto; max-width: 950px;">
        <p style="text-align:left; font-size:23px; line-height:100%">
          World Deaths from Conflicts
        </p>
      </div>
      <br>
      <Graph2 {data} />

      <div style="margin: 0 auto; max-width: 1000px;">
        <div style="margin: 0 auto; max-width: auto;">
          <h4 style="text-align:left;">Write Up: What have you done so far? </h4>
          <p style="text-align:left;">
            We have conducted extensive research on the Ukraine conflicts, gathering data, articles, and reports to gain a comprehensive understanding of the topic.
            We have identified key events, milestones, and developments in the Ukraine conflicts, organizing them into a chronological timeline.
            We have started designing the layout and structure of our interactive web page, envisioning how we will present the information to users.
            We have begun prototyping different visualization techniques, including timeflow charts, maps, and textual narratives, to effectively communicate the progression of the conflicts.
          </p>
          <br>
          <h4 style="text-align:left;">What will be the most challenging of your project to design and why? </h4>
          <p style="text-align:left;">
            we anticipate that integrating the scrollytelling feature will pose the greatest challenge. Scrollytelling involves synchronizing the narrative progression with the user's scrolling actions, creating a seamless storytelling experience. This feature requires precise coordination between text, visuals, and user interactions, ensuring that the content unfolds in a coherent and engaging manner. Additionally, implementing map visualizations with Mapbox presents its own set of challenges, particularly regarding the layout and functionality when the foreground elements are absent. We anticipate that troubleshooting and resolving these issues will require careful attention to detail and experimentation with different design approaches. Despite these challenges, we are committed to delivering a compelling and informative Explorable Explanation on the Ukraine conflicts, leveraging innovative storytelling techniques and data visualization methods.
          </p>
        </div>
        <br>
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
      visibility: visible;
  }

  section {
      height: 50vh;
      background-color: rgba(0, 0, 0, 0.2); /* 20% opaque */
      text-align: center;
      color: black;
      padding: 1em;
      margin: 0 0 2em 0;
  }

  .graph {
      height: 110vh;
  }

  .subheading {
      font-family: 'Nunito', sans-serif;
      font-size: 1.5em; /* Adjust the font size as needed */
      font-weight: 400;
      line-height: 1.5;
      color: black;
      background-color: #f0f0f0; /* Background color of your choice */
      padding: 20px;
  }

  .blurb {
      font-family: 'Nunito', sans-serif;
      text-align: left;
      font-size: 1em;
      font-weight: 300;
      line-height: 1.5;
      padding: 0 20px; /* Add some padding to the sides for better readability */
  }
  </style>
