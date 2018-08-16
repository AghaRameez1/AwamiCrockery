var awamicrockery= {
    buttonfuntion: function(){
        $('.add').on('click',function () {
            // $('.addition').css('display','block');
            // $('.add').text('To add');
            var type='POST';
            var url = '/';
            var data= $(".data-entry").serialize();
                // 'first_name': $('#id_first_name').val(),
                // 'last_name': $('#id_last_name').val(),
                // 'price': $('#id_price').val(),
                // 'item_code': $('#id_item_code').val()
            NetworkModule.getData(url,type,data,function(response){
                if(response == 'success'){
                    alert('Sucessfully Added')
                }
                else{
                    alert('Failed')
                }

            })
        })
    },
    init:function(){
        this.buttonfuntion();
    }
};