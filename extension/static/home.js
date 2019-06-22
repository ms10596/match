document.getElementById("submit").addEventListener("click", myScript);

function myScript() {
    console.log("hereee");
    var url = 'http://127.0.0.1:5000/';
    var postData = {
        "txt": document.getElementsById("article").value
    };
    console.log(postData);
    var request = new XMLHttpRequest();
    request.onload = function () {
        var status = request.status;
        var data = request.responseText;
        console.log(data);
    }
    request.open("POST", url);
    request.setRequestHeader("Content-Type", "application/json");
    request.send(JSON.stringify(postData));

}