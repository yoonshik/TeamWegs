function doPoll(){
    payload = JSON.stringify({username:'yoonshik', password:'viasat'})
    $.post('/check_camera', payload, function(data) {
        console.log(data);
        setTimeout(doPoll,5000);
    });
}
