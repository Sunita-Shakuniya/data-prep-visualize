
        // Add this script to handle the button click event
        document.getElementById('reloadButton').addEventListener('click', function() {
          // Use JavaScript to make an asynchronous request to the reload_data view
          fetch('/reload_data/')
            .then(response => {
              if (response.ok) {
                // Reload the page if the request is successful
                location.reload();
              } else {
                console.error('Failed to reload data');
              }
            })
            .catch(error => {
              console.error('Error during reload:', error);
            });
        });



        function scrollToBottom() {
        // Get the reference to the scrollable div
        const scrollableDiv = document.getElementById('scrollableDiv');

        // Set scrollTop to scrollHeight to initially scroll to the bottom
        scrollableDiv.scrollTop = scrollableDiv.scrollHeight;
        }

        // Call scrollToBottom when the page loads or when content changes
        window.onload = scrollToBottom;

        // Attach scrollToBottom to the click event of the reload button
        const reloadButton = document.getElementById('reloadButton');
        reloadButton.addEventListener('click', function () {
            // Assuming you have a function to reload data, replace loadData() with your actual function
            loadData();

            // After reloading data, scroll to the bottom
            scrollToBottom();
        });

        // Example function to simulate loading data
        function loadData() {
            // Replace this with your actual logic to load more data
            // For example, you might use AJAX, Fetch API, etc.
            console.log('Loading data...');
        }