/*verificaçao de exclusao*/ 


$(document).ready(function(){
    var botaoD = $('.delete');
    var pesquisa =$('#pesquisa')
    var formpesquisa=$('#form-pesquisa')
    $(botaoD).on('click',function(e){
        e.preventDefault();
        var dellink=$(this).attr('href');
        var confirma=confirm('quer deletar esta tarefa');
        if(confirma){
            window.location.href=dellink;
        }

    });
    $(pesquisa).on('click',function(){
        formpesquisa.submit();

    });

});