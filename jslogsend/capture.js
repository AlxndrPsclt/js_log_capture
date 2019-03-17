(function(){
  var url = "http://127.0.0.1:5000/send_log";
  var method = "POST";
  var shouldBeAsync = true;

  var oldLog = console.log;
  console.log = function (message, obj) {
    var request = new XMLHttpRequest();

  request.onreadystatechange = function() {
  };

    request.open(method, url, shouldBeAsync);

    request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
    //request.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    // Or... request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");

    // Actually sends the request to the server.
    request.send(JSON.stringify(obj));
    oldLog.apply(console, arguments);
  };
})(); 
