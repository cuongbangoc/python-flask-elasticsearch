function SearchPage(){
    var SEARCH_API = 'http://192.168.1.8:5003/api/v1/search';

    var WEB_ROOT = $('#web-root').val(),
        CSS = $('#css').val(),
        JS = $('#js').val(),
        EJS_TEMPLATES = $('#ejs-templates').val();

    var access_token = "zkeILPduduZzouKdHy6nIsxYSc7B9HhDLWOTUrScz6hRsqW0qTqe6i24vma8dJimqXMs6RR22kTTobBijzSfpg==";

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

    function bindEvent(){
        $(document).delegate('.search-action .user-search', 'keyup', function(){
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
        });
    }

    bindEvent();
}

$(document).ready(function(){
    new SearchPage();
});