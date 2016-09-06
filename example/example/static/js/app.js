$(function() {
  $('[data-toggle="tooltip"]').tooltip()
})

// Voting
var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});


$("#upvote-link, #downvote-link").click(function(e) {

  e.preventDefault();


  $.ajax({
    type: "POST",
    url: $(this).attr('href'),
    async: false,
    success: function(result) {
      $('#voting-box').html(result.message);
      console.log(result);
    },
    error: function(result) {
      $('#voting-box').html(result.message);
      console.log(result);
    }
  });

});
