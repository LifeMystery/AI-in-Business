document.addEventListener('DOMContentLoaded', () => {
  // Fetch data for charts
  fetch('/path/to/your/data.json')
    .then(response => response.json())
    .then(data => {
      // Data for Graph 1
      const ctx1 = document.getElementById('graph1').getContext('2d');
      new Chart(ctx1, {
        type: 'line', // or 'bar', 'pie', etc.
        data: {
          labels: data.graph1.labels,
          datasets: [{
            label: 'Graph 1 Data',
            data: data.graph1.values,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });

      // Data for Graph 2
      const ctx2 = document.getElementById('graph2').getContext('2d');
      new Chart(ctx2, {
        type: 'bar', // or 'line', 'pie', etc.
        data: {
          labels: data.graph2.labels,
          datasets: [{
            label: 'Graph 2 Data',
            data: data.graph2.values,
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    })
    .catch(error => console.error('Error loading the chart data:', error));

  // Fetch data for HTML updates
  fetch('../output.json')
    .then(response => response.json())
    .then(data => {
      // Update the HTML elements with JSON data
      document.getElementById('unemployed').textContent = `Predicted Unemployment Rate: ${data.predicted_unemployment_rate_nn}`;
      document.getElementById('cpi').textContent = `Predicted CPI: ${data.predicted_cpi_nn}`;
      document.getElementById('Percentage').textContent = `Overall Trend Percentage: ${data.overall_trend_percentage}`;
      document.getElementById('trend').textContent = `Overall Trend: ${data.overall_trend}`;
  
      // Update business tips
      const businessTipsElement = document.getElementById('businessT');
      businessTipsElement.innerHTML = 'Business Tips:<br>' + data.business_tips.map(tip => `<li>${tip}</li>`).join('');
    })
    .catch(error => console.error('Error fetching the HTML data:', error));
});
