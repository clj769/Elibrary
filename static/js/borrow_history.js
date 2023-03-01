$(function() {
	$('form').submit(function(event) {
		event.preventDefault();
		const userId = $('#user_id').val();
		$.ajax({
            method: 'GET',
            url: `/borrow_history?user_id=${userId}`,
            success: function (data) {
                $('#result_table_body').empty();
                for (const record of data.records) {
                    const row = `
						<tr>
							<td>${record.username}</td>
							<td>${record.booktitle}</td>
							<td>${record.borrowdate}</td>
							<td>${record.returndate}</td>
						</tr>
					`;
                    $('#result_table_body').append(row);
                }
            },
            error: function () {
                alert('Error, no result');
            }
        });
  });
});

