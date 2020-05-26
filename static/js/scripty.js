$(document).ready(function(){
    $.material.init();

    $(document).on("submit", "#register-form", function(e){
        e.preventDefault();
        var form = $('#register-form').serialize();
        $.ajax({
            url: '/postregistration',
            type: 'POST',
            data: form,
            success: function(response){
                console.log(response)
            }
        });
    });
    $(document).on("submit", "#login-form", function(e){
        e.preventDefault();

        var form = $(this).serialize();
        $.ajax({
           url: '/checklogin',
           type: 'POST',
           data: form ,
           success: function(res){
               if(res == 'error'){
                alert('Could not log in');
               }else{
                console.log("logged in as",res);
                location.href = '/';
               }
           }
        });
    });

    $(document).on('click', '#logout-link', function(e){
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function(res){
                if(res == 'success'){
                    location.href = '/login';
                } else{
                    alert("Something went wrong!");
                }
            }
        })
    });
    $(document).on('submit','#post-activity',function(e){
        e.preventDefault();
        form = $(this).serialize()

        $.ajax({
            url: '/postactivity',
            type: 'POST',
            data: form,
            success: function(post){
                console.log(post);
                if(post){
                    location.href = location.href
                }
            }
        });
    });
});
