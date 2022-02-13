$('.plus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/plus_cart",
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log(data)
            eml.innerText = data.quantity
            document.getElementById("amt").innerHTML = data.amount
            document.getElementById("Total").innerHTML = data.totalamount
        }
    })
})
$('.minus-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minus_cart",
        data: {
            prod_id: id
        },
        success: function(data) {
            console.log(data)
            eml.innerText = data.quantity
            if (eml.innerText <= 0) {
                document.getElementById(id).remove()

            }
            document.getElementById("amt").innerHTML = data.amount
            document.getElementById("Total").innerHTML = data.totalamount
        }
    })
})
$('.remove-cart').click(function() {
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/remove_cart",
        data: {
            prod_id: id
        },
        success: function(data) {
            document.getElementById(id).remove()
            document.getElementById("amt").innerHTML = data.amount
            document.getElementById("Total").innerHTML = data.totalamount

        }
    })
})