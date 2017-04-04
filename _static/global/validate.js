/*
 * validate.js
 * Ankur Goswami, agoswam3@ucsc.edu
 * Validate emoji fields and normal text fields
 */

var validate = function(validatedFn, errorFn){
    var inputs = $(".form-control:not(.area, #arrive_time)");
    var emojiareas = $(".emojionearea-editor");
    var boolReduce = function(arr){
        var flag = true;
        arr.each(function(index){
            if($(this).html() == "" && $(this).val() == ""){
                flag = false;
                return false;
            }
        });
        return flag;
    }
    var areInputsFilled = boolReduce(inputs);
    var areEmojisFilled = boolReduce(emojiareas);
    if(areInputsFilled && areEmojisFilled){
        validatedFn();
    } else {
        errorFn()
    }

    // This is specific to emojiarea text fields.
    if(areEmojisFilled)
        $(".no-input").prop('disabled', true);
    else
        $(".no-input").prop('disabled', false);
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
    validate(validated, invalid);
    $('*').keyup(function(){
        validate(validated, invalid);
    });
});
