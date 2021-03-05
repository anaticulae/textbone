const API = '/api/v0'
const TIMEOUT = 3000

const rpc = function (url, callback, error = undefined) {
    let call = `${API}${url}`
    $.ajax(call, {
        dataType: 'json',
        success: function (response) {
            callback(response)
        },
        error: function (response) {
            if (error != undefined) {
                error()
            } else {
                console.log(`error: ${call}`);
            }
        }
    });
}

const request = function (url, params, callback, error = undefined) {
    let call = `${API}${url}`
    $.ajax(call, {
        method: "GET",
        dataType: "json",
        data: params,
        success: function (response) {
            callback(response)
        },
        error: function (response) {
            if (error != undefined) {
                error()
            } else {
                console.log(`error: ${call} ${params}`);
            }
        }
    });
}

const post = function (url, data, callback) {
    let call = `${API}${url}`
    $.ajax({
        type: 'POST',
        url: call,
        data: data,
        success: function (response) {
            callback(response)
        },
    })
}
