function main(){
    var millisecondsToPause = 5000;
    var counter = 0;
    var scroll = setInterval(function(){
        var now = new Date().getTime();
        while(now + millisecondsToPause > new Date().getTime()){}

        if($(window).scrollTop() + $(window).height() != $(document).height()) {
            console.log("lowering round " + counter)
            window.scrollBy(0,50);
            counter += 1;
        }
        else{
            console.log("Resetting location and reloading the page")
            $("html, body").animate({ scrollTop : 0});
            document.location.reload(true);
        } 
        }, 
        200);
}

function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight
    );
}

main();