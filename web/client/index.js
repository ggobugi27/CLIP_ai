// Running a Python script:
// var PythonShell = require('python-shell');

// Load the IFrame Player API code asynchronously.
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/player_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Replace the 'ytplayer' element with an <iframe> and
// YouTube player after the API code downloads.

let listId = 'PL6XQGDZm1hq0lzlIgxn_3SrWSs42WSOFY'//bigbang
let videoId = 'MBNQgq56egk'//bigbang
var player;
function onYouTubePlayerAPIReady() {
  player = new YT.Player('ytplayer', {
  height: '360',
  width: '640',
  listType: 'playlist',
  list : listId,
  videoId: videoId
  });
}

let youtubeUrl;
let tempUrl;
setInterval(() => tempUrl = player.getVideoUrl(), 3000);


// if (tempUrl !== youtubeUrl) youtubeUrl = tempUrl;//******WRITE OFF OF THIS

// const fetchImages = () => 
//   fetch('/')

// setInterval(() => fetchImages(), 5000)

document.getElementById('clip-image').addEventListener('click', () => {
  console.log('current Video URL is : ', tempUrl)
  fetch('/api/video', {
    headers: {
      'Content-Type': 'application/json'
    },
    method: 'post',
    body: JSON.stringify({videoUrl: tempUrl})
  })
})

// function postData(url, data) {
//   // Default options are marked with *
//   fetch('/', {
//     method: 'get',
//     timeout: 5000
//   })
// }

// /*
//  * App State
//  */

// const state = {
//   videoUrl: tempUrl,
//   selectedAttractions: []

// const fullstackCoords = [-74.009, 40.705] // NY
// // const fullstackCoords = [-87.6320523, 41.8881084] // CHI

// const map = new mapboxgl.Map({
//   container: "map",
//   center: fullstackCoords,
//   zoom: 12, // starting zoom
//   style: "mapbox://styles/mapbox/streets-v10" // mapbox has lots of different map styles available.
// });

// const fetchAttractions = () =>
//   fetch("/api")
//     .then(result => result.json())
//     .catch(err => console.error(err));


// const itineraryData = (id) =>
//   fetch(`/api/itinerary/${id}`)
//     .then(result => result.json())
//     .catch(err => console.error(err));


// module.exports = {
//   itineraryData,
//   fetchAttractions
// };

// /*
//   * Populate the list of attractions
//   */

// api.fetchAttractions().then(attractions => {
//   state.attractions = attractions;
//   const { hotels, restaurants, activities } = attractions;
//   hotels.forEach(hotel => makeOption(hotel, "hotels-choices"));
//   restaurants.forEach(restaurant => makeOption(restaurant, "restaurants-choices"));
//   activities.forEach(activity => makeOption(activity, "activities-choices"));
// });

// const makeOption = (attraction, selector) => {
//   const option = new Option(attraction.name, attraction.id); // makes a new option tag
//   const select = document.getElementById(selector);
//   select.add(option);
// };

// /*
//   * Attach Event Listeners
//   */

// // what to do when the `+` button next to a `select` is clicked
// ["hotels", "restaurants", "activities"].forEach(attractionType => {
//   document
//     .getElementById(`${attractionType}-add`)
//     .addEventListener("click", () => handleAddAttraction(attractionType));
// });

// // Create attraction assets (itinerary item, delete button & marker)
// const handleAddAttraction = attractionType => {
//   const select = document.getElementById(`${attractionType}-choices`);
//   const selectedId = select.value;

//   // Find the correct attraction given the category and ID
//   const selectedAttraction = state.attractions[attractionType].find(
//     attraction => +attraction.id === +selectedId
//   );

//   // If this attraction is already on state, return
//   if (state.selectedAttractions.find(attraction => attraction.id === +selectedId && attraction.category === attractionType))
//     return;

//   //Build and add attraction
//   buildAttractionAssets(attractionType, selectedAttraction);
// };



// const buildAttractionAssets = (category, attraction) => {
//   // Create the Elements that will be inserted in the dom
//   const removeButton = document.createElement("button");
//   removeButton.className = "remove-btn";
//   removeButton.append("x");

//   const itineraryItem = document.createElement("li");
//   itineraryItem.className = "itinerary-item";
//   itineraryItem.append(attraction.name, removeButton);

//   // Create the marker
//   const marker = buildMarker(category, attraction.place.location);

//   // Adds the attraction to the application state
//   state.selectedAttractions.push({ id: attraction.id, category });

//   //ADD TO DOM
//   document.getElementById(`${category}-list`).append(itineraryItem);
//   marker.addTo(map);

//   // Animate the map
//   map.flyTo({ center: attraction.place.location, zoom: 15 });

//   removeButton.addEventListener("click", function remove() {
//     // Stop listening for the event
//     removeButton.removeEventListener("click", remove);

//     // Remove the current attrction from the application state
//     state.selectedAttractions = state.selectedAttractions.filter(
//       selected => selected.id !== attraction.id || selected.category !== category
//     );

//     // Remove attraction's elements from the dom & Map
//     itineraryItem.remove();
//     marker.remove();


//     // Animate map to default position & zoom.
//     map.flyTo({ center: fullstackCoords, zoom: 12.3 });
//   });
// };

// if (window.location.hash[0] === '#') {
//   let id = window.location.hash.slice(1);
//   api.itineraryData(id)
//   .then (itiner => {
//     itiner.hotels.forEach(hotel => buildAttractionAssets('hotels', hotel));
//     itiner.restaurants.forEach(restaurant => buildAttractionAssets('restaurants', restaurant));
//     itiner.activities.forEach(activity => buildAttractionAssets('activities', activity));
//   });
// }

// document.getElementById('save-button').addEventListener('click', () => {
//   console.log('our state', state)
//   fetch('/api/itineraries', {
//     headers: {
//       'Content-Type': 'application/json'
//     },
//     method: 'post',
//     body: JSON.stringify(state.selectedAttractions)
//   })
// })



