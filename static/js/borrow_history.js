function search() {
  // 获取用户输入的 ID
  var userId = document.getElementById("user_id").value;

  // 创建 XMLHttpRequest 对象
  var xhr = new XMLHttpRequest();

  // 设置请求的 URL
  xhr.open("GET", "/search/?user_id=" + userId);

  // 监听请求状态
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      // 解析服务器响应的数据
      var data = JSON.parse(xhr.responseText);

      // 根据返回的数据生成表格
      var table = document.createElement("table");
      var tr = document.createElement("tr");
      var headers = ["Username", "Book Title", "Borrow Date", "Return Date"];
      for (var i = 0; i < headers.length; i++) {
        var th = document.createElement("th");
        th.textContent = headers[i];
        tr.appendChild(th);
      }
      table.appendChild(tr);
      for (var i = 0; i < data.length; i++) {
        var record = data[i];
        var tr = document.createElement("tr");
        var td1 = document.createElement("td");
        td1.textContent = record.username;
        var td2 = document.createElement("td");
        td2.textContent = record.booktitle;
        var td4 = document.createElement("td");
        td4.textContent = record.borrow_date;
        var td5 = document.createElement("td");
        td5.textContent = record.return_date || "";
        tr.appendChild(td1);
        tr.appendChild(td2);
        tr.appendChild(td4);
        tr.appendChild(td5);
        table.appendChild(tr);
      }

      // 将表格添加到页面中
      var result = document.getElementById("result");
      result.innerHTML = "";
      result.appendChild(table);
    }
  };

  // 发送请求
  xhr.send();
}
