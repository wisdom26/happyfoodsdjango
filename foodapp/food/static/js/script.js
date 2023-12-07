document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevents default form submission
  
    // Get input values
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
  
    // Check if username and password are correct (Example: Username: "user", Password: "password")
    if (username === 'user' && password === 'password') {
      // If correct, redirect or perform further actions (e.g., navigate to a new page)
      window.location.href = 'dashboard.html'; // Redirect to dashboard page
    } else {
      // If incorrect, display error message
      document.getElementById('error-message').innerText = 'Invalid username or password. Please try again.';
    }
  });