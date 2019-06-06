function tacoInfo() {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    // currentTacoNum = 0;
    document.getElementById("sample_para_text").innerText = "You have requested 30 tacos!";

    socket.on('tacoUpdate', function(message) {
        currentTacoNum = message;
        document.getElementById("sample_para_text").innerText = "You have requested " + currentTacoNum + " tacos!";
    });
}