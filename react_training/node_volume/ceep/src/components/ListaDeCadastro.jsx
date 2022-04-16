import React, { Component } from "react"
import CardCadastro from "./CardCadastro/CardCadastro";

class ListaDeCadastro extends Component{

    // constructor(props){
    //     super(props)
    // }

    render(){
        return (
            <ul>
                {this.props.notas.map((nota, index) => {
                    return (
                        <li key = {index}>
                            <CardCadastro titulo={nota.titulo} texto={nota.texto}/>
                        </li>
                    )
                })}
            </ul>
        );
    }
}

export default ListaDeCadastro;
