function tacoInfo(numTacos) {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    
    currentTacoNum = numTacos;
    document.getElementById("tacoHeading3").innerText = "You have requested " + currentTacoNum + " tacos!";

    socket.on('tacoUpdate', function(message) {
        currentTacoNum = message.numTacos;
        document.getElementById("tacoHeading3").innerText = "You have requested " + currentTacoNum + " tacos!";
    });
}