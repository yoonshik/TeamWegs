function doPoll(){
    $.post('http://192.168.66.180:6543/check_camera', function(data) {
        alert(data);
        setTimeout(doPoll,5000);
    });
}
