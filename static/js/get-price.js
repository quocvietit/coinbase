$(document).ready(function(){
    //connect to the socket server.
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    var numbers_received = [];

    //receive details from server
     socket.on('coinbasepro', function(msg) {
         console.log("Received number");
         $('#BTC_GBP_bid').html(msg.BTC_GBP_bid);
         $('#BTC_GBP_ask').html(msg.BTC_GBP_ask);
          $('#ETH_GBP_bid').html(msg.ETH_GBP_bid);
          $('#ETH_GBP_ask').html(msg.ETH_GBP_ask);
          $('#ETH_BTC_bid').html(msg.ETH_BTC_bid);
          $('#ETH_BTC_ask').html(msg.ETH_BTC_ask);
          $('#profit_rate1').html(msg.profit_rate1);
          $('#profit_rate2').html(msg.profit_rate2);
     });
});