var Illumine = {
    init : function() {
        Illumine.customSelect();
        Illumine.createReviewSlider();
        Illumine.createDoctorSlider();
        Illumine.resizeNewsLine();
        $('a.videoPlay').click(function() {
            $('#myModal').modal('toggle');
            return false;
        });
        $('.customCheckBox').click(Illumine.customCheckbox);
        
    },
    
    customCheckbox : function() {
        if($(this).hasClass('checked')) {
            $(this).removeClass('checked');
            $(this).find('input[type="checkbox"]').removeAttr('checked');
        } else {
            $(this).addClass('checked');
            $(this).find('input[type="checkbox"]').attr('checked', 'checked');
        }
    },
    
    resizeNewsLine : function() {
      $('.newsArticle .left .border').height($('.newsArticle .text').height() - ($('.newsArticle .author').height()) + 10  );
      $('.newsArticle .comments .left .border').height($('.newsArticle .comments .text .info').height() - 50 );
    },
    
    createReviewSlider : function() {
        var slideWidth = $('.bottomSection .left ul li').width();
        var slideCount = $('.bottomSection .left ul li').length;
        var ulWidth = slideCount * slideWidth;
        $('.bottomSection .left ul').width( ulWidth );
        
        $('.bottomSection .left .controls.prev').click(function() {
            var element = $(this);
            element.addClass("disabled");
            var marginLeft = parseInt($('.bottomSection .left ul').css('marginLeft').replace("px", ''));
            if(marginLeft <= (-slideWidth)) {
                $('.bottomSection .left ul').animate({
                    "marginLeft" : (marginLeft+slideWidth)+"px"
                }, {
                    duration : 500,
                    queue : false,
                    complete : function() {
                        element.removeClass("disabled")
                    }
                });
        }
        return false;
        });
    $('.bottomSection .left .controls.next').click(function() {
        var element = $(this);
        element.addClass("disabled");
        var marginLeft = parseInt($('.bottomSection .left ul').css('marginLeft').replace("px", ''));
        if((-marginLeft) <= (ulWidth - slideWidth)) {
            $('.bottomSection .left ul').animate({
                "marginLeft" : (-slideWidth)+"px"
            }, {
                duration : 500,
                queue: false,                
                complete : function() {
                    element.removeClass("disabled");
                }
            } );
    }
    return false;
    });
},
    
createDoctorSlider : function() {
    var slideWidth = $('.doctorSlider .coverFlow').width();
    var slideCount = $('.doctorSlider .coverFlow ul li').length;
    $('.doctorSlider .coverFlow ul li').width(slideWidth);
    var ulWidth = slideCount * slideWidth;
    $('.doctorSlider .coverFlow ul').width( ulWidth );
        
    $('.doctorSlider .controls.left').click(function() {
        var element = $(this);
        element.addClass("disabled");
        var marginLeft = parseInt($('.doctorSlider .coverFlow ul').css('marginLeft').replace("px", ''));
        if(marginLeft <= (-slideWidth)) {
            $('.doctorSlider .coverFlow ul').animate({
                "marginLeft" : (marginLeft+slideWidth)+"px",
                "queue" : false
            }, {
                duration : 500,
                queue : false,
                complete : function() {
                    element.removeClass('disabled');
                }
            } );
        }
        return false;
    });
    $('.doctorSlider .controls.right').click(function() {
        var element = $(this);
        element.addClass("disabled");
        var marginLeft = parseInt($('.doctorSlider .coverFlow ul').css('marginLeft').replace("px", ''));
        if((-marginLeft) <= (ulWidth - slideWidth)) {
            $('.doctorSlider .coverFlow ul').animate({
                "marginLeft" : (-slideWidth)+"px"
            }, {
                duration : 500,
                queue : false,
                complete : function() {
                    element.removeClass('disabled');
                } 
            } );
        }
        return false;
    });
},
    
customSelect : function() {
    $('.customSelect input').click(function() {
        $('.customSelect .options').hide();
        $(this).next().next().toggle();
        var ref = $(this);
        $(this).next().next().hover(function(){},function(){
            $(this).hide();
        })
        $(this).next().next().find("a").click(function() {
            ref.val($(this).text());
            ref.next().next().hide();
            return false;
        });
        return false;
    });
    $('.customSelect button').click(function() {
        $('.customSelect .options').hide();
        $(this).next().toggle();
        var ref = $(this);
        $(this).next().hover(function(){},function(){
            $(this).hide();
        })
        $(this).next().find("a").click(function() {
            ref.prev().val($(this).text());
            ref.next().hide();
            return false;
        });
        return false;
    });
        
}
}

$(document).ready(function() {
    Illumine.init();
    $("a.disabled").click(function(){
        return false;
    });
    $(function() {
        $('input, textarea').placeholder();
       });
    $('#mainNav .pull-left').mobileMenu({
         defaultText: 'Navigate to',
         className: 'visible-phone',
             subMenuDash: '&ndash;'
    });
});

$(window).resize(function() {
    Illumine.createReviewSlider();
    Illumine.createDoctorSlider();
    Illumine.resizeNewsLine();
});