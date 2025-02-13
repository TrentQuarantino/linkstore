// Example: Listen for browser action click (icon click) - alternative to popup
chrome.action.onClicked.addListener(tab => {
  // ... (Code to send data, similar to popup.js, but without the button click listener)
  
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    const currentTab = tabs[0];
    const dataToSend = {
      url: currentTab.url,
      title: currentTab.title,
      // Add other data you want to collect...
      //customData: "Some additional information",
    };
    console.log(dataToSend)
    //alert(JSON.stringify(dataToSend))
    // 2. Send data to the server using Fetch API
    const serverUrl = 'http://localhost:8888/from_chrome'; // Replace with your server URL

    fetch(serverUrl, {
      method: 'POST',
      mode: 'no-cors',
      //headers: {
        //'Content-Type': 'application/json', // Important for JSON data
        //'Access-Control-Allow-Origin': '*'
      //},
      body: JSON.stringify(dataToSend) // Convert data to JSON string
    })
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json(); // If your server sends back JSON
    })
    .then(responseData => {
      console.log('Data sent successfully:', responseData);
      // Optionally, update the popup UI to show success
    })
    .catch(error => {
      console.error('Error sending data:', error);
      // Optionally, update the popup UI to show the error
    });
  }); 

});

// Example: Periodic data sending (e.g., every hour)
//setInterval(() => {
  // ... (Code to collect and send data)
//}, 1000); // 3600000 milliseconds = 1 hour
//<a href="https://www.flaticon.com/free-icons/download" title="download icons">Download icons created by Pixel perfect - Flaticon</a>