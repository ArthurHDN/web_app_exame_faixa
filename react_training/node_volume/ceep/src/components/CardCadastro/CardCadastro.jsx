import React, { Component } from "react";
import "./style.css"

class CardCadastro extends Component{
    render(){
        return (
            <section className="card-cadastro">
                <header>
                    <h3>{this.props.titulo}</h3>
                </header>
                <p>{this.props.texto}</p>
            </section>
        );
    }
}

export default CardCadastro;
