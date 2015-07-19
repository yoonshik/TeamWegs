function doPoll(){
    $.post('http://192.168.66.180:6543/check_camera', {'username':'yoonshik', 'password':'viasat'}, function(data) {
        console.log(data);
        setTimeout(doPoll,5000);
    });
}
