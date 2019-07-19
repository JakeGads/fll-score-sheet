function main(){
    var millisecondsToWait = 1;
    var millisecondsToPause = 3000;
    var startTime = new Date().getTime();
    

    var scroll = setInterval(function(){
        var now = new Date().getTime();
        while(now + millisecondsToPause > new Date().getTime()){}
        console.log("lowering")
        window.scrollBy(0,50); 
        }, 
        200);
    var shouldpass = 0
    var elem = document.getElementById("TopOfPage")
    var reset = setInterval(function(){
        //$('html, body').animate({ scrollTop: 0 }, 'fast');
        if(shouldpass < 14){
            shouldpass = shouldpass + 1;
            console.log('Skipping Reset Request #' + shouldpass + ' of 14');
        }
        else{
            console.log('Resetting the view');
            $("html, body").animate({ scrollTop : 0}, "slow")
            document.location.reload(true);
        }
    },
    2400);
}

main();