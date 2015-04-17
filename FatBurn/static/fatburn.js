/**
 * Created by boates on 4/16/2015.
 */

$(document).ready(function ($) {
    $('.test1').click(function(){
      $(this).addClass('active');
      $(this).parent().children('li').not(this).removeClass('active');
    });
});