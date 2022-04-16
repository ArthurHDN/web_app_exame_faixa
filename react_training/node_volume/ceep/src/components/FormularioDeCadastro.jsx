import React, { Component } from "react";

class FormularioDeCadastro extends Component{
    constructor(props){
        super(props);
        this.titulo = "";
        this.texto = "";
    }

    handleMudancaTitulo(evento){
        this.titulo = evento.target.value
        console.log(this.titulo)
    }

    handleMudancaTexto(evento){
        this.texto = evento.target.value
        console.log(this.texto)
    }

    _criarNota(evento){
        evento.preventDefault();
        evento.stopPropagation();
        this.props.criarNota(this.titulo, this.texto);
    }

    render(){
        return (
            <form onSubmit={this._criarNota.bind(this)}>
                <input type="text" placeholder="Título" onChange={this.handleMudancaTitulo.bind(this)}/>
                <textarea placeholder="Escreva sua nota..." onChange={this.handleMudancaTexto.bind(this)} />
                <button>Criar Nota</button>
            </form>
        );
    }
}

export default FormularioDeCadastro;
