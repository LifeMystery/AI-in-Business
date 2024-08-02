// Fetch the locations JSON file and update the top locations
fetch('../locations.json')
  .then(response => response.json())
  .then(data => {
    const topLocations = data.top_locations;
    if (topLocations.length >= 2) {
      // Update the top location section with the top two locations
      document.getElementById('location-1').textContent = topLocations[0].name;
      document.getElementById('location-2').textContent = topLocations[1].name;
    } else if (topLocations.length === 1) {
      document.getElementById('location-1').textContent = topLocations[0].name;
      document.getElementById('location-2').textContent = 'N/A'; // or some other placeholder
    } else {
      document.getElementById('location-1').textContent = 'N/A';
      document.getElementById('location-2').textContent = 'N/A';
    }
  })
  .catch(error => console.error('Error fetching locations:', error));



  document.addEventListener('DOMContentLoaded', function() {
    const trendText = document.getElementById('trend-text');
    const newUserCountElement = document.getElementById('new-customers-count');
    const uptrendIcon = document.getElementById('uptrend-icon');
    const downtrendIcon = document.getElementById('downtrend-icon');

    // Fetch the locations JSON file and update the trend and percentage
    fetch('../locations.json')
      .then(response => response.json())
      .then(data => {
        const trend = data.trend;
        const percentage = data.percentage;
        const currentTotalUsers = data.current_total_users;

        // Update new user count
        newUserCountElement.textContent = currentTotalUsers.toLocaleString();

        // Determine if uptrend or downtrend and update the UI
        if (trend === 'up') {
            uptrendIcon.classList.remove('hidden');
            downtrendIcon.classList.add('hidden');
            trendText.textContent = `+${percentage}%`;
        } else if (trend === 'down') {
            downtrendIcon.classList.remove('hidden');
            uptrendIcon.classList.add('hidden');
            trendText.textContent = `-${percentage}%`;
        } else {
            uptrendIcon.classList.add('hidden');
            downtrendIcon.classList.add('hidden');
            trendText.textContent = 'No Change';
        }
      })
      .catch(error => console.error('Error fetching trend data:', error));
});

document.addEventListener('DOMContentLoaded', function() {
  // Fetch the JSON file
  fetch('../summary.json')
      .then(response => response.json())
      .then(data => {
          // Get the summary from the JSON data
          const summary = data.summary;

          // Find the paragraph element and update its text content
          const paragraph = document.querySelector('#articles p');
          paragraph.textContent = summary;
      })
      .catch(error => {
          console.error('Error fetching the JSON file:', error);
      });
});
