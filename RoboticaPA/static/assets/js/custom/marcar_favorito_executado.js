function marcar_favorito(plano_aula, usuario) {
    $.ajax({
        url : "/plano-aula/marcar-favorito/"+plano_aula+"/"+usuario,
        method : "GET",
        success: function (returndata) {
            alterar_contador("thumbs_up", plano_aula, returndata)
            trocar_cor("thumbs_up", plano_aula, returndata);
        }
    });
}

function marcar_executado(plano_aula, usuario) {
    $.ajax({
        url : "/plano-aula/marcar-executado/"+plano_aula+"/"+usuario,
        method : "GET",
        success: function (returndata) {
            alterar_contador("play", plano_aula, returndata)
            trocar_cor("play", plano_aula, returndata);
        }
    });
}

function alterar_contador(tipo, id, returndata) {
    const str = "contador_" + tipo + "_" + id.toString()
    const elemento = document.getElementById(str)
    console.log('{{tipo}}')
    if (returndata == 0) {
        elemento.textContent = (parseInt(elemento.textContent) - 1).toString();
    }
    else {
        elemento.textContent = (parseInt(elemento.textContent) + 1).toString();
    }
}

function trocar_cor(tipo, id, returndata) {
    const str = "icon_" + tipo + "_" + id.toString()
    const elemento = document.getElementById(str)
    if (returndata == 0) {
        elemento.style = 'color: white;';
    }
    else {
        elemento.style = 'color: var(--bs-success); -webkit-text-stroke: 1px white;';
    }
}