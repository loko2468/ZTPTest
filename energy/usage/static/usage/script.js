$ = document.querySelector.bind(document);
$$ = document.querySelectorAll.bind(document);


window.addEventListener('load',
function () {
    $$('.customer[data-customer_id]').forEach(x=>{
        x.onmouseover = function(){omoCustomer(x);};
        x.onmouseleave = function(){omoCustomer(x);};
    });
});


function showWinners(){
    $('.highest').classList.toggle('hidden');
}

 function omoCustomer(div){
    $$('.customer[data-customer_id="'+div.dataset.customer_id+'"]').forEach(x=>{
        x.classList.toggle('highlight');
    });


 }