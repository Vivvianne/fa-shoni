$(document).ready(function() {
    var stickyNavTop = $("#header").offset().top;
    var stickyNav = function(){
    var scrollTop = $(window).scrollTop(); 
    if (scrollTop > stickyNavTop) { 
        $("#header").addClass('sticky');
    } else {
        $("#header").removeClass('sticky'); 
    }
};
    stickyNav();
    $(window).scroll(function() {
        stickyNav();
    });
    var cartDisplay = $("#cart-info");
    var addCart = $("#food1-cart");
    var cartItems = [1,2,3,4,5,6,7,8,9];
    var cartNumber = 0;
    cartItems.forEach(function(cartItem){
        $(".addcart"+cartItem+"").click(function(){
            cartNumber += 1;
            var title = $(".title"+cartItem+"").text();
            var price = $(".price"+cartItem+"").text();
            $("#cart-items").text(cartNumber);
            $(".cart-full").append("<div class='row' id='item"+cartNumber+"'><div class='col-md-4 cart-display'><h2 class='item-title' id='title"+cartNumber+"'>"+title+"</h2></div><div class='col-md-4 cart-display'><p class='item-price' id='price"+cartNumber+"'>"+price+"</p></div><div class='col-md-4 cart-display'><i class='fa fa-trash' id='del"+cartNumber+"'></i></div></div>")
            $("#del"+cartNumber+"").click(function(){
                $("#item"+cartNumber+"").hide();
                cartNumber -= 1;
                $("#cart-items").text(cartNumber);
            }); 
        });
    });
    $(".fa-shopping-cart").click(function(){
        $(".cart-full").toggle();
    });
    var categories = [1,2,3,4];
    categories.forEach(function(category){
        if(category === 1){
            $("#category"+category+"").click(function(){        
                $("div.active").removeClass("active");
                $("section.active").hide();
                $("section.active").removeClass("active");
                $("#category-"+category+"").show();
                $("#category-"+category+"").addClass("active");
                $("#category"+category+"").addClass("active");
            });
        }else if(category === 2){
            $("#category"+category+"").click(function(){        
                $("div.active").removeClass("active");
                $("section.active").hide();
                $("section.active").removeClass("active");
                $("#category-"+category+"").show();
                $("#category-"+category+"").addClass("active");
                $("#category"+category+"").addClass("active");
            });
        }else if(category === 3){
            $("#category"+category+"").click(function(){        
                $("div.active").removeClass("active");
                $("section.active").hide();
                $("section.active").removeClass("active");
                $("#category-"+category+"").show();
                $("#category-"+category+"").addClass("active");
                $("#category"+category+"").addClass("active");
            });
        }else{
            $("#category"+category+"").click(function(){        
                $("div.active").removeClass("active");
                $("section.active").hide();
                $("section.active").removeClass("active");
                $("#category-"+category+"").show();
                $("#category-"+category+"").addClass("active");
                $("#category"+category+"").addClass("active");
            });
        } 
    });
});