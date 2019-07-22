function main(){
    // here is how long we pause between scrolling down
    let millisecondsToPause = 5 * 1000;
    // this counts how many pixels that have moved down on the screen
    // it currently set to how far it sees in the page -1 (for an additional pause at the end)
    let counter = document.documentElement.scrollHeight-1;
    
    let firstScroll = setInterval(function(){
        window.scrollBy(45, 0)
    }, 1)

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
            window.scrollBy(0, counter * -1)
            document.location.reload()
        } 
        }, 
        200);
}

main();