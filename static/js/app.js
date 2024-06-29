

var select = document.getElementById('inputState');
const setSubTotal = document.getElementById('subtotal');
var input2 = document.getElementById('gen')
var inputTotal = document.getElementById('subtotal')

select.addEventListener('focus',function(){
    input2.value= 0;
    inputTotal.value =0;
})

select.addEventListener('change',
    function item(){
        var selectedOption = this.options[select.selectedIndex];
        //console.log(selectedOption.value + ':' + selectedOption.text);
        let precio = selectedOption.id;
        console.log(precio);
        
        subTotal(precio)
    }
);

function subTotal(precio){
    
    const tt= document.getElementById("gen");
    tt.addEventListener('input',function(){
    let num=tt.value
    console.log(num);
    setSubTotal.value = Math.round((precio * num)*100)/100;
    });
    

}


