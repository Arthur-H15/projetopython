/*verificaçao de exclusao*/ 


$(document).ready(function(){
    var botaoD = $('.delete');
    $(botaoD).on('click',function(e){
        e.preventDefault();
        var dellink=$(this).attr('href');
        var confirma=confirm('quer deletar esta tarefa');
        if(confirma){
            window.location.href=dellink;
        }

    });

});