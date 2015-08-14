function SearchPage(){
    var SEARCH_API = 'http://192.168.1.8:5003/api/v1/search';

    var WEB_ROOT = $('#web-root').val(),
        CSS = $('#css').val(),
        JS = $('#js').val(),
        EJS_TEMPLATES = $('#ejs-templates').val();

    // var access_token = "b7U1SxVox6VAM2173OsHwv_3tdpStzBPrrFs-8ZYQkBu1u-A5ER7qNrRZusZU0bpSlGMFrV1k_wUdGR5hUcETw==";
    // var access_token = $('#access_token').val();
    var access_token = null;

    var userTemplate = null,
        outfitTemplate = null;

    function sendAjax(url, method, data, type){
        $.ajax({
            url: url,
            type: method,
            data: data,
            dataType:"json",
            success: function(response){
                if ( response && response.data.total > 0){
                    if (type == "user"){
                        var users = response.data.hits;

                        renderUsers(users);
                    }
                    if (type == "outfit"){
                        var outfits = response.data.hits;
                        renderOutfits(outfits);
                    }

                }
            },
            complete: function(){

            }
        });
    }

    function login(username, password){
        $.ajax({
            url: "http://192.168.1.8:5000/api/v1/users/login",
            type: "POST",
            data: {username: username, password: password},
            dataType:"json",
            success: function(response){
                if ( response ){
                    if (response.error_code == 0){
                        access_token = response.access_token;
                        $(".user-profile").show();
                        $(".signin").hide();
                        $("#login_fail").hide();
                        $('#loginModal').modal('hide');
                    }else{
                        $("#login_fail").show();
                    }
                }else{
                    $("#login_fail").show();
                }
            },
            error: function(error){
                $("#login_fail").show();
            },
            complete: function(){

            }
        });
    }

    function renderUsers(users){
        userTemplate = userTemplate || new EJS({ url: EJS_TEMPLATES + '/user.search.ejs'});
        var userHtml = userTemplate.render({ data: {'users': users}});

        $('.blog-main').html(userHtml);
    };

    function renderOutfits(outfits){
        outfitTemplate = outfitTemplate || new EJS({ url: EJS_TEMPLATES + '/outfit.search.ejs'});
        var outfitHtml = outfitTemplate.render({ data: {'outfits': outfits}});

        $('.blog-main').html(outfitHtml);
    };

    function get_item_by_name(arr, name){
        for(var i = 0; i < arr.length; i++){
            if (arr[i].name == name){
                return arr[i];
            }
        }

        return null;
    }

    function autoCompleteSearch(){
        var result = new Array();
        $( "#user-search" ).autocomplete({
            source: function( request, response ) {
                var query = $("#user-search").val();
                var url = SEARCH_API + "/people?access_token=" + access_token + "&user_name=" + query;
                console.log(query);
                console.log(access_token);
                $.ajax({
                    url: url,
                    type: "POST",
                    dataType: "json",
                    data: {
                        //q: query
                    },
                    success: function( data ) {
                        console.log(data.data.hits);
                        if (data.data.hits.length > 0){
                            var res = new Array();
                            result = data.data.hits;
                            for (var i = 0; i < data.data.hits.length; i++){
                                res.push(data.data.hits[i].name);
                            }
                            response( res );
                        }
                    }
                });
            },
            minLength: 1, //Set length word to start search
            select: function( event, ui ) {
                item = get_item_by_name(result, ui.item.value);
                var renderData = [];
                renderData.push(item);
                renderUsers(renderData);
            },
            open: function() {
                $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
            },
            close: function() {
                $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
            }
        });

        $( "#outfit-search" ).autocomplete({
            source: function( request, response ) {
                var query = $("#outfit-search").val();
                var url = SEARCH_API + "/outfits/name?access_token=" + access_token + "&outfit_name=" + query;
                $.ajax({
                    url: url,
                    type: "POST",
                    dataType: "json",
                    data: {
                        //q: query
                    },
                    success: function( data ) {
                        console.log(data.data.hits);
                        if (data.data.hits.length > 0){
                            var res = new Array();
                            result = data.data.hits;
                            for (var i = 0; i < data.data.hits.length; i++){
                                res.push(data.data.hits[i].name);
                            }
                            response( res );
                        }
                    }
                });
            },
            minLength: 1, //Set length word to start search
            select: function( event, ui ) {
                item = get_item_by_name(result, ui.item.value);
                var renderData = [];
                renderData.push(item);
                renderOutfits(renderData);
            },
            open: function() {
                $( this ).removeClass( "ui-corner-all" ).addClass( "ui-corner-top" );
            },
            close: function() {
                $( this ).removeClass( "ui-corner-top" ).addClass( "ui-corner-all" );
            }
        });
    }

    function bindEvent(){
        /*$(document).delegate('.search-action .user-search', 'keyup', function(){
            var query = $(this).val();
            var url = SEARCH_API + "/people?access_token=" + access_token + "&user_name=" + query;
            var data = {};

            sendAjax(url, "POST", data, "user");
        });

        $(document).delegate('.search-action .outfit-search', 'keyup', function(){
            var query = $(this).val();
            var url = SEARCH_API + "/outfits/name?access_token=" + access_token + "&outfit_name=" + query;
            var data = {};

            sendAjax(url, "POST", data, "outfit");
        });*/

        $(document).delegate('#login_btn', 'click', function(){
            var username = $("#login_username").val();
            var password = $("#password").val();

            login(username, password);
        });

        $(document).ready(function(){
            $(document).on('click','.signup-tab',function(e){
                e.preventDefault();
                $('#signup-taba').tab('show');
            });

            $(document).on('click','.signin-tab',function(e){
                e.preventDefault();
                $('#signin-taba').tab('show');
            });

            $(document).on('click','.forgetpass-tab',function(e){
                e.preventDefault();
                $('#forgetpass-taba').tab('show');
            });
        });
    }


    bindEvent();
    autoCompleteSearch();
}

$(document).ready(function(){
    new SearchPage();
});