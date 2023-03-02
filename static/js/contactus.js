// get form and the submit button
var form = document.querySelector('.contact-form');
var submitButton = form.querySelector('button[type="submit"]');

// after submit success, give a message
form.addEventListener('submit', function(event) {
    event.preventDefault();

    // avoid to submit again
    submitButton.disabled = true;

    // submit form and action 发送表单数据并接收响应
    fetch(event.target.action, {
        method: event.target.method,
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: new URLSearchParams(new FormData(event.target)).toString()
    })
    .then(function(response) {
        // success message
        form.innerHTML = '<p class="success-message">Your message has been sent successfully!</p>';
    })
    .catch(function(error) {
        // error message
        form.innerHTML = '<p class="error-message">An error occurred. Please try again later.</p>';
    });
});
