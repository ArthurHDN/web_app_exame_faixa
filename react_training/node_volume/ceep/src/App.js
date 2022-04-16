import React, { Component } from 'react'
import FormularioDeCadastro from './components/FormularioDeCadastro';
import ListaDeCadastro from './components/ListaDeCadastro';

class App extends Component {

  constructor(){
    super();
    this.state = {
      notas:[]
    };
  }

  criarNota(titulo, texto){
    const novaNota = {titulo, texto};
    const novoArrayNotas = [...this.state.notas,novaNota]
    const novoEstado = {
      notas:novoArrayNotas
    }
    this.setState(novoEstado);
  }

  render() {
    return (
      <section>
        <h1>Meu app React</h1>
        <FormularioDeCadastro criarNota={this.criarNota.bind(this)}/>
        <ListaDeCadastro notas={this.state.notas}/>
      </section>
    );
  }
}

export default App;
