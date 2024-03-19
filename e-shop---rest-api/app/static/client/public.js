function loadProduct () {
    // AJAX
    xhr = new XMLHttpRequest()
    xhr.open("GET", "/products")
    xhr.onload = function () {
        response = xhr.responseText
        data = JSON.parse(response)
        
        productContainer.innerHTML = `

            <div class="card col-12 col-lg-6 text-center" >
                <img src="${data[0]["image"]}" class="card-img-top" alt="${data[0]["name"]}">
                <div class="card-body">
                    <h1 class="card-title">${data[0]["name"]}</h1>
                    <p class="card-text">${data[0]["description"]}</p>

                    <div id="productStandardPrice">LOADING PRICE ...</div>

                    <button id="showOrderModalButton" type="button" class="btn btn-primary btn-lg" data-bs-toggle="modal" data-bs-target="#orderModal">
                      Order <i class="bi bi-arrow-up-right-circle-fill"></i>
                    </button>


                </div>
            </div>
        ` 

        // store the product id into the containr's attribute
        productContainer.setAttribute('data-product-id', data[0]["id"])

            // extracting the price
            xhr = new XMLHttpRequest()
            xhr.open("GET", `/money/${data[0].price_standard}`)
            xhr.onload = function () {
                response = xhr.responseText
                data = JSON.parse(response)
                productStandardPrice.innerHTML = `
                   ${data.amount} ${data.currency}
                `
            }
            xhr.send()

    }
    xhr.send()
}

function payOrder () {
    xhr = new XMLHttpRequest()
    xhr.open("GET", `/client/pay/${localStorage.getItem('order_id')}`)
    xhr.onload = function () {
        response = xhr.responseText
        data = JSON.parse(response)
        // console.log(data)
        window.open(data.url)
    }
    xhr.send()
}

function viewOrder () {
    xhr = new XMLHttpRequest()
    xhr.open("GET", `/client/orders/${localStorage.getItem('order_id')}`)
    xhr.onload = function () {
        response = xhr.responseText
        data = JSON.parse(response)
        let modalBody = document.getElementById('modalBody')
        modalBody.innerHTML = `
            <h2>Order Details</h2>
            <p>Your client id is ${data.client_id}</p>
            <button id="payButton" type="button" class="btn btn-primary" onclick="payOrder()">PAY</button>
        `
        // HW*: could add more details
        // HW*: check response status code = 200
    }
    xhr.setRequestHeader('Authorization', `Token ${localStorage.getItem('access')}`)
    xhr.send()
}

function orderProduct () {
    // read the product id from the cotainer
    let product_id = productContainer.getAttribute('data-product-id')

    let client_email = InputEmail.value
    let client_phone = InputPhone.value
    let client_delivery_wanted = deliveryCheck.checked
    let client_delivery_address = InputAddress.value

    let payload = {
        'client_email': client_email,
        'client_phone': client_phone,
        'client_delivery_wanted': client_delivery_wanted,
        'client_delivery_address': client_delivery_address,
    } 

    xhr = new XMLHttpRequest()
    xhr.open("POST", `/orders/${product_id}`)
    xhr.onload = function () {
        let data = JSON.parse(xhr.responseText)
        if (xhr.status == 201) {
            modalBody.innerHTML = `
                <h2>Order created successfully</h2>
            `
            localStorage.setItem('access',data.access)
            localStorage.setItem('order_id',data.id)
            let button = document.getElementById('orderButton')
            let buttonShow = document.getElementById('showOrderModalButton')
            button.innerHTML = 'View Order'
            buttonShow.innerHTML = 'View Order'
            button.onclick= null
            button.onclick = viewOrder
            buttonShow.onclick= null
            buttonShow.onclick = viewOrder

        }
    }
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.send(
        JSON.stringify(payload)
    )
}

loadProduct ()