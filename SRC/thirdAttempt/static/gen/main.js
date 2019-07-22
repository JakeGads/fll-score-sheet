function main(){
    // here is how long we pause between scrolling down
    let millisecondsToPause = 5 * 1000;
    // this counts how many pixels that have moved down on the screen
    // it currently set to how far it sees in the page -1 (for an additional pause at the end)
    let counter = document.documentElement.scrollHeight-1;

    let scroll = setInterval(function(){
        //re-ups the current time so that it can tell how long to wait
        let now = new Date().getTime();
        //the empty waiting while loop
        while(now + millisecondsToPause > new Date().getTime()){}

        // calculates the current height
        let height = document.documentElement.scrollHeight;

        if(counter <= height) {
            console.log("lowering round " + counter);
            window.scrollBy(0,50);
            counter += 50;
        }
        else{
            console.log("Resetting location and reloading the page");
            $("html, body").animate({ scrollTop : 0}, "fast");
            document.location.reload()
        } 
        }, 
        200);
}

main();