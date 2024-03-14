<script>
  import mapboxgl from "mapbox-gl";
  import { onMount } from "svelte";
  export let index;
  export let geoJsonToFit;


  mapboxgl.accessToken =
    "pk.eyJ1Ijoid3lzNjI5OSIsImEiOiJjbGtodDNrMnIwYmxwM2dxbDU3azZlZ3JiIn0.Hb3fx_PsGtyRh38lP1Nwcg";

  let container;
  let map;

  let zoomLevel;

  function updateZoomLevel() {
    const screenWidth = window.innerWidth;
    zoomLevel = screenWidth <= 600 ? 4 : 5.7; // Adjust these values as needed
  }

  function handleResize() {
    updateZoomLevel();
    map.setZoom(zoomLevel);
  }

  onMount(() => {
    updateZoomLevel();
    map = new mapboxgl.Map({
      container,
      style: "mapbox://styles/wys6299/clt7qstej00hs01o801l17nat",
      center: [31, 49],
      zoom: zoomLevel,
      attributionControl: true, // removes attribution from the bottom of the map
    });

    window.addEventListener("resize", handleResize);

    function hideLabelLayers() {
      const labelLayerIds = map
        .getStyle()
        .layers.filter(
          (layer) =>
            layer.type === "symbol" && /label|text|place/.test(layer.id)
        )
        .map((layer) => layer.id);

      for (const layerId of labelLayerIds) {
        map.setLayoutProperty(layerId, "visibility", "none");
      }
    }

    map.on("load", () => {
      hideLabelLayers();
      updateBounds();
      map.on("zoom", updateBounds);
      map.on("drag", updateBounds);
      map.on("move", updateBounds);
    });
  });
  
  function updateBounds() {
    const bounds = map.getBounds();
    geoJsonToFit.features[0].geometry.coordinates = [
      bounds._ne.lng,
      bounds._ne.lat,
    ];
    geoJsonToFit.features[1].geometry.coordinates = [
      bounds._sw.lng,
      bounds._sw.lat,
    ];
  }

  let isVisible = true;

</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://api.mapbox.com/mapbox-gl-js/v2.14.0/mapbox-gl.css"
  />
</svelte:head>

<div class="map" class:visible={isVisible} bind:this={container} />

<style>
  .map {
    width: 100%;
    height: 100vh; /* check problem when setting width */
    position: relative;
    opacity: 0;
    visibility: hidden;
    transition: opacity 2s, visibility 2s;
    outline: rgb(0, 0, 0) solid 3px;
  }

  .map.visible {
    opacity: 1;
    visibility: visible;
  }
</style>

