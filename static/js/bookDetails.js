// $(document).ready(function() {
//   $('#borrow-form').submit(function(event) {
//     event.preventDefault();
//
//     var bookId = $('#book-id').val();
//     var url = $('#borrow-form').data('url');
//
//
//     $.ajax({
//       type: 'POST',
//       url: url,
//       data: {
//         'book_id': bookId,
//         'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
//       },
//       success: function(data) {
//         alert(data.message);
//         // if (data.success) {
//         //   alert("Borrowed successfully.");
//         // } else {
//         //   alert("This book is currently out of stock.");
//         // }
//       },
//       error: function() {
//         alert('An error occurred while processing your request.');
//       }
//     });
//   });
// });



$(document).ready(function() {
      // Hide the "Read More" button if the text fits within the max-height


      // Toggle the text and button text on click
      $('.read-more').click(function() {
        $('.text').toggleClass('expanded');
        if ($('.text').hasClass('expanded')) {
          $('.read-more').text('Read Less');
        } else {
          $('.read-more').text('Read More');
        }
      });
    });

//author detail
$(document).ready(function() {
  $('.author-header').click(function() {
    $(this).parent().toggleClass('show');
  });
});

//review
$(document).ready(function() {
  $('.reviews-header').click(function() {
    $(this).parent().toggleClass('show');
  });
});

//
document.addEventListener("DOMContentLoaded", function() {
  var comments = document.querySelectorAll(".comment");

  comments.forEach(function(comment) {
    var body = comment.querySelector(".comment-body");
    var toggle = comment.querySelector(".comment-toggle");

    if (body.clientHeight < body.scrollHeight) {
      toggle.style.display = "inline";
    }

    toggle.addEventListener("click", function(e) {
      e.preventDefault();
      body.classList.toggle("expanded");

      if (body.classList.contains("expanded")) {
        toggle.textContent = "Show Less";
      } else {
        toggle.textContent = "Show More";
      }
    });
  });
});

