function updateAPI (method,url,payload,cb) {
    let xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.onload = function () {
        let data
        if(xhr.responseText) { 
            data = JSON.parse(xhr.responseText)
        } else {
            data = null
        }
        cb(data,xhr)
    }
    xhr.send(
        JSON.stringify(payload)
    )
}


function uploadFile (url,payload,cb) {
    let xhr = new XMLHttpRequest()
    xhr.open("POST", url)
    // xhr.setRequestHeader('Content-type', 'multipart/form-data')

    xhr.onload = function () {
        let data
        if(xhr.responseText) { 
            data = JSON.parse(xhr.responseText)
        } else {
            data = null
        }
        cb(data,xhr)
    }
    xhr.send(
        payload
    )
}
