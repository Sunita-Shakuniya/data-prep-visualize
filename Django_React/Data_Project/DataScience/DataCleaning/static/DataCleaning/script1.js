$("form").on("change", ".file-upload-field", function(){ 
    $(this).parent(".file-upload-wrapper").attr("data-text",  $(this).val().replace(/.*(\/|\\)/, '') );
});

// for upload script
fileInput.addEventListener("change", e => {
    let selectedFile = e.target.files[0];
    if (selectedFile) {
        uploadFile(selectedFile);
    }
});

function uploadFile(file) {
    // Create FormData object and append the selected file
    let formData = new FormData();
    formData.append('file', file);

    // Send the file to the server using AJAX
    fetch('/handle_uploaded_file/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken'), // Replace with the actual cookie name used for CSRF
        },
    })
    .then(response => response.json())
    .then(data => {
        // Handle the server response if needed
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if the cookie name matches the expected format
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



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