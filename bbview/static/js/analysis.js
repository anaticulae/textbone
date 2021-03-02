"use strict";

class Analysis {
    constructor() {
    }

    init() {
        $('#generate')[0].onclick = update_plots
        $('#documents_all')[0].onclick = documents_select_all
        $('#operation_all')[0].onclick = operations_select_all
        // $('#findings_all')[0].onclick = findings_select_all
    }
}

const analysis = new Analysis()

const update_plots = function () {
    let data = documents_selected()

    request('/analysis/documents', data, function (response) {
        // TODO: NOT VERY SMART
        $('#plots')[0].innerHTML = 'loading...'
        setTimeout(() => {
            $('#plots')[0].innerHTML = ''
            response.plots.forEach(function (item) {
                let raw = `<img src="/plots/${item}" class="plot"> `
                $('#plots').append(raw)
            })
        }, 500)
    })
}

const documents_selected = function () {
    let documents = $.map($('input.documents:checked'), s => s.id)
    let operations = $.map($('input.operations:checked'), s => s.id)
    let data = {
        'documents': documents,
        'operations': operations,
    }
    return data
}

const select_all = function () {
    // HACK
    $(this).attr("checked", false)
    $(this).click()
    $(this).attr("checked", true)
}

const documents_select_all = function () {
    $('input.documents').each(select_all)
}

const operations_select_all = function () {
    $('input.operations').each(select_all)
}

// const findings_select_all = function () {
//     $('input.findings').each(select_all)
// }

$(document).ready(function () {
    analysis.init()
})
