"use strict";

class Judge {
    constructor() {
        this.sentences = []
        this.current = ''
    }

    init() {
        $('#add_sentence')[0].onclick = judge.send_sentence
        judge.download_sentences()
    }

    send_sentence() {
        let slang = $('#slang')[0].checked
        let noscience = $('#noscience')[0].checked
        let complicated = $('#complicated')[0].checked
        let nocontent = $('#nocontent')[0].checked
        let current = judge.current
        let result = {
            'current': current,
            'slang': slang,
            'noscience': noscience,
            'complicated': complicated,
            'nocontent': nocontent,
        }
        post('/judge/sentence/send', result, function () {
            judge.next_sentence()
            judge.clear_selection()
        })
    }

    next_sentence() {
        if (judge.sentences.length == 0) {
            this.download_sentences()
            return
        }
        judge.current = judge.sentences.pop()
        $('#sentences')[0].innerHTML = judge.current
    }

    clear_selection() {
        $('#complicated')[0].checked = false
        $('#nocontent')[0].checked = false
        $('#noscience')[0].checked = false
        $('#slang')[0].checked = false
    }

    download_sentences() {
        $('#sentences')[0].innerHTML = 'Downloading...'
        rpc('/judge/sentence/next', function (response) {
            judge.sentences = response.sentences
            judge.next_sentence()
        })
    }


}

const judge = new Judge()

$(document).ready(function () {
    judge.init()
})
