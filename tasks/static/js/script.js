/*verificaçao de exclusao*/ 


$(document).ready(function(){
    var baseUrl='http://localhost:8000'
    var botaoD = $('.delete');
    var pesquisa =$('#pesquisa');
    var formpesquisa=$('#form-pesquisa');
    var filter=$('#filter');
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
    $(filter).change(function(){
        var filter = $(this).val();
       

       
      
            window.location.href=baseUrl + '?filter='+ filter }
    )
    
});
