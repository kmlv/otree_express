/*
 * randomize.js
 * Ankur Goswami, agoswami3@ucsc.edu
 * Quick script to randomize table rows
 */

/*
* Given: Table with id randomizeTable
* Replace a random row after another random row rows.length number of times
*/
var randomize = function (){
    var rows = $("#randomizeTable > tbody > tr")
    for(var i = 0; i < rows.length; i++){
        // Pick a two spots in the table that are not the first row 
        var spot1 = Math.floor(Math.random() * rows.length + 1)
        var spot2 = Math.floor(Math.random() * rows.length + 1)
        var row1 = rows.eq(spot1)
        var row2 = rows.eq(spot2)
        // Put row1 after row2
        $(row1).after($(row2))
    }
}

$(document).ready(function(){
    randomize();
});