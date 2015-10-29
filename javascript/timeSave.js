// ==UserScript==
// @name         My Fancy New Userscript
// @namespace    http://your.homepage/
// @version      0.1
// @description  enter something useful
// @author       You
// @match        htt*://*.facebook.com/*
// @match        htt*://*.youtube.com/*
// @grant        none
// @require http://code.jquery.com/jquery-latest.js
// ==/UserScript==

function sayHello(p)
{
    var url = window.location;
    //if (@match == "https://www.facebook.com/"){
    alert("Then go do that, Whatever "+p +" means !!!");
    //alert("You entered   "+p);
        //document.write(url);
        //document.write(p);
    //}
}
function init()
{
    var pur = "";
    var url = window.location;
    //if (@match == "https://www.google.com/")
    //{
       pur = prompt("Hey, hi there. Why are you here today?");
    
      //  }
    //document.write(pur); 
    return pur;
}

function timer(p){
    var start = new Date().getTime();
    var count = 0;
    var end = 0;
    while (true){

        end = new Date().getTime();
        if (end-start >= 1000){
            sayHello(p);
            start = new Date().getTime();
            count += 1;
        }
        if (count >0){
            break;
        }
    }
    window.location.href = "http://google.com";
}
$(document).ready(function() {
p = init();
timer(p);
});
