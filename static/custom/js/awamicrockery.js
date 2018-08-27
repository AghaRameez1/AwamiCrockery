var awamicrockery = {
    buttonfuntion: function () {
        $('.add').on('click', function () {
            $('.addition').css('display', 'block');
            $('.add').removeClass('add');
            $('.add').add('add2')
        });
        $('.add2').on('click', function () {
            $('.addition').css('display', 'none');

        })

    },
    addition: function () {
        var type = 'POST';
        var url = '/';
        var data = $(".data-entry").serialize();
        NetworkModule.getData(url, type, data, function (response) {
            if (response == 'success') {
                alert('Sucessfully Added')
            }
            else {
                alert('Failed')
            }

        })

    },
    search: function () {
        $('.search').on('click', function () {
            var type = 'GET';
            var url = '/search/';
            var data = $('#vendor_search').val();
            NetworkModule.getData(url, type, data, function (response) {
                if (response == 'success')
                    alert('Found');
                else {
                    alert('No data')
                }

            })
        })
    },
    init: function () {
        this.buttonfuntion();
        this.search()
    }
};