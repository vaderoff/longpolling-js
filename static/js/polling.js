var block = document.getElementById('block');

function polling() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState != 4 || xhr.status != 200) return;
        block.innerHTML = JSON.parse(xhr.responseText).resp;
        setTimeout(polling, 1000);
    }
    xhr.timeout = 3000;
    xhr.open('GET', 'http://127.0.0.1:8080/api', true);
    xhr.send();
}

polling();