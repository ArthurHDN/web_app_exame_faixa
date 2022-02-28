CREATE USER 'root'@'%' IDENTIFIED BY 'didyn'; GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;

CREATE DATABASE IF NOT EXISTS didynDB;
USE didynDB;

CREATE TABLE IF NOT EXISTS escola(
  id_escola INT(11) UNIQUE AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  endereco VARCHAR(255),
  PRIMARY KEY (id_escola)
);

CREATE TABLE IF NOT EXISTS aluno(
  id_aluno INT(11) UNIQUE AUTO_INCREMENT,
  id_escola INT(11) NOT NULL,
  nome VARCHAR(255) NOT NULL,
  gub INT(11) NOT NULL,
  professor VARCHAR(255),
  PRIMARY KEY (id_aluno),
  FOREIGN KEY (id_escola) REFERENCES escola(id_escola) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS avaliacao(
  id_avaliacao INT(11) UNIQUE AUTO_INCREMENT,
  id_aluno INT(11),
  mestre VARCHAR(255),
  sagui INT(11),
  sonkisul INT(11),
  balkisul INT(11),
  sibon_donjak_1 INT(11),
  sibon_donjak_2 INT(11),
  comb_tec_1 INT(11),
  comb_tec_2 INT(11),
  comb_tec_3 INT(11),
  taeguk_1 INT(11),
  taeguk_2 INT(11),
  taeguk_3 INT(11),
  matchuho_kyorugui INT(11),
  kyorugui INT(11),
  kyopa INT(11),
  avalicao_periodica INT(11),
  avalicao INT(11),
  PRIMARY KEY (id_avaliacao),
  FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno) ON DELETE CASCADE 
);
