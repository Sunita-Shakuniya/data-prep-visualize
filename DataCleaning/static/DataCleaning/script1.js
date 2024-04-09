
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


        document.addEventListener('DOMContentLoaded', function() {
          // Select the dropdown buttons and dropdown contents
          var dropdownBtn1 = document.querySelector('.dropbtn');
          var dropdownContent1 = document.querySelector('.dropdown-content');
          var dropdownBtn2 = document.querySelector('.dropbtn1');
          var dropdownContent2 = document.querySelector('.dropdown-content1');
          var performButton = document.querySelector('.operationbtn');
      
          // Function to toggle dropdown visibility
          function toggleDropdown(dropdownContent) {
              dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
          }
      
          // Function to check if both dropdowns are selected
          function checkDropdowns() {
              var isDropdown1Selected = dropdownContent1.value !== '';
              var isDropdown2Selected = dropdownContent2.value !== '';
              performButton.style.display = isDropdown1Selected && isDropdown2Selected ? 'block' : 'none';
          }
      
          // Event listener for when the dropdown button 1 is clicked
          dropdownBtn1.addEventListener('click', function(event) {
              event.preventDefault(); // Prevent the default behavior of reloading the page
              toggleDropdown(dropdownContent1); // Toggle the visibility of the dropdown content 1
              checkDropdowns(); // Check if both dropdowns are selected
          });
      
          // Event listener for when the dropdown button 2 is clicked
          dropdownBtn2.addEventListener('click', function(event) {
              event.preventDefault(); // Prevent the default behavior of reloading the page
              toggleDropdown(dropdownContent2); // Toggle the visibility of the dropdown content 2
              checkDropdowns(); // Check if both dropdowns are selected
          });
      
          // Event listener for when an option is selected in the dropdown content 1
          dropdownContent1.addEventListener('change', function() {
              var selectedOption = dropdownContent1.options[dropdownContent1.selectedIndex];
              dropdownBtn1.textContent = selectedOption.textContent;
              toggleDropdown(dropdownContent1); // Hide the dropdown content after selecting an option
              checkDropdowns(); // Check if both dropdowns are selected
          });
      
          // Event listener for when an option is selected in the dropdown content 2
          dropdownContent2.addEventListener('change', function() {
              var selectedOption = dropdownContent2.options[dropdownContent2.selectedIndex];
              dropdownBtn2.textContent = selectedOption.textContent;
              toggleDropdown(dropdownContent2); // Hide the dropdown content after selecting an option
              checkDropdowns(); // Check if both dropdowns are selected
          });
      
          // Hide the dropdown contents initially
          dropdownContent1.style.display = 'none';
          dropdownContent2.style.display = 'none';
          performButton.style.display = 'none'; // Hide the perform button initially
      });
      