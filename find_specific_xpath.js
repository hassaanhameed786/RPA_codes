var xpath = '//*[@id="InvResultTableRN"]//tr';
var data = [];
var XPathResult = Array.from((function  * () {
    let iterator = document.evaluate(xpath, document, null, XPathResult.UNORDERED_NODE_ITERATOR_TYPE, null);
    let current = iterator.iterateNext();
    while (current) {
        yield current;
        current = iterator.iterateNext();
    }
    })());


if(XPathResult[1].querySelectorAll('td')[0].textContent == invoice){
    
    var Invoice_number = XPathResult[1].querySelectorAll('td')[0].textContent;
    var Invoice_Date   = XPathResult[1].querySelectorAll('td')[1].textContent;
    data.push(Invoice_number);
    data.push(Invoice_Date);
    
}

return data;

 



