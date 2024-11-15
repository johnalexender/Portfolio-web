// JavaScript to handle the active link indicator
document.addEventListener('DOMContentLoaded', function () {
  // Get all the navigation links
  const navLinks = document.querySelectorAll('.nav-link');

  // Function to remove the 'active' class from all links
  function removeActiveClass() {
    navLinks.forEach(link => {
      link.classList.remove('active');
    });
  }

  // Add click event to each nav link
  navLinks.forEach(link => {
    link.addEventListener('click', function () {
      // Remove 'active' class from all links
      removeActiveClass();

      // Add 'active' class to the clicked link
      link.classList.add('active');
    });
  });
});
