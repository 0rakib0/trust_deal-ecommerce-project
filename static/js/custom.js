// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();

// owl carousel 

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 6
        }
    }
})


// my Custom functionality

$('#increas_quantity').click(function(){
    let qualtity = parseInt($('#quentity').val())
    $('#minus_quantity').prop('disabled', false);
    qualtity++;
    $('#quentity').val(qualtity)
    $('#item_quantity').val(qualtity)
})

$('#minus_quantity').click(function(){
    let qualtity = parseInt($('#quentity').val())

    if (qualtity > 1) { // Check if quantity is greater than 1
        qualtity--; // Decrement the quantity by 1
        $('#quentity').val(qualtity); // Set the updated quantity back to the input field
        $('#item_quantity').val(qualtity)
    }
    if (qualtity === 1) {
        $('#minus_quantity').prop('disabled', true);
    }
   
})