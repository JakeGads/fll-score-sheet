function main(){
    var millisecondsToPause = 5000;
    var counter = 0;

    

    var scroll = setInterval(function(){
        var now = new Date().getTime();
        while(now + millisecondsToPause > new Date().getTime()){}

        var height = document.documentElement.scrollHeight;

        if(counter <= height) {
            console.log("lowering round " + counter);
            window.scrollBy(0,50);
            counter += 50;
        }
        else{
            console.log("Resetting location and reloading the page");
            $("html, body").animate({ scrollTop : 0}, "fast");
            document.location.reload(true)
        } 
        }, 
        200);
}

main();