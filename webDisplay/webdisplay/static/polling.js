function doPoll(){
    $.post('/check_camera', {'username':'yoonshik', 'password':'viasat'}, function(data) {
        console.log(data);
        setTimeout(doPoll,5000);
    });
}
