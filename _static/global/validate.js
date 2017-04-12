/*
 * validate.js
 * Ankur Goswami, agoswam3@ucsc.edu
 * Validate emoji fields and normal text fields
 *
 * Rachel Chen, me@rachelchen.me
 * continue development
 */

var boolReduce = function(arr){
        var flag = true;
        // This .each() is jQuery specific. Using .reduce() directly will throw an error
        arr.each(function(index){
            if($(this).html() == "" && $(this).val() == ""){
                flag = false;
                return false;
            }
        });
        return flag;
    }

var validate = function(validatedFn, errorFn){
    var inputs = $(".form-control:not(.area, #arrive_time)");
    var emojiareas = $(".emojionearea-editor");
    var areInputsFilled = boolReduce(inputs);
    var areEmojisFilled = boolReduce(emojiareas);
    if(areInputsFilled && areEmojisFilled){
        validatedFn();
    } else {
        errorFn()
    }
}

var validated = function(){
    $(".disp").prop('disabled', false);
    $("#invalid-fields").hide();
}

var invalid = function(){
    $(".disp").prop('disabled', true);
    $("#invalid-fields").show();
}

$(document).ready(function(){
    $('*').keyup(function(){
        validate(validated, invalid);
    });
    $('.skip-button').click(function() {
        // reset input value
        $(".form-control:not(.area, #arrive_time)").each(function() {
            $(this).val('');
        })
        // reset message value
        $('.area')[0].emojioneArea.setText('');
        // manually validated
        validated()
        // help the user click because he/she is stupid
        $('.next-button')[0].click()
    })
});
