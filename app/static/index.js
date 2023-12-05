function validateForm() {
  // You can replace this with the actual input fields in your form
  var title = document.forms["form"]["title"].value;
  var date = document.forms["form"]["date"].value;
  var time = document.forms["form"]["time"].value;
  var location = document.forms["form"]["location"].value;

  if (title === "" || date === "" || time === "" || location === "") {
      document.getElementById("errorMessage").innerHTML = "All feilds must be filled out";
      document.getElementById("errorMessage").style.display = "block";
      return false;
  }

  document.getElementById("errorMessage").style.display = "none";
  return true;
}

function scrollToTop() {
  // Scroll to the top of the page smoothly
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}
