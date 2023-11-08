$(document).ready(function () {
    const one = document.getElementById("e1");
    const two = document.getElementById("e2");
    const three = document.getElementById("e3");
    const four = document.getElementById("e4");
    const five = document.getElementById("e5");
  
    const form = document.querySelector(".rate-form");
    const csrf = document.getElementsByName("csrfmiddlewaretoken");
  
    const arr = [one, two, three, four, five];
  
    arr.forEach((element) => {
      element.addEventListener("click", (e) => {
        const rating = e.target.getAttribute("data-value");
        form.addEventListener("submit", (e) => {
          e.preventDefault();
          const id = e.target.id;
  
          $.ajax({
            type: "POST",
            url: "/add_rating/",
            data: {
              csrfmiddlewaretoken: csrf[0].value,
              movie_id: id,
              rating: rating,
            },
            success: function (response) {
              window.location.reload();
            },
            error: function (error) {
              alert(error.responseText)
            },
          });
  
        });
      });
    });
  });