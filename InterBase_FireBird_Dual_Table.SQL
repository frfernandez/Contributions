/*==========================================================================

Português Brasileiro/Español/English
Desenvolvedor/Desarrollador/Developer: Fernando Roberto Fernández
Projeto/Proyecto/Project: Sample
Bancos de Dados/Base de Datos/Database: InterBase/FireBird

Português Brasileiro
Muitos desenvolvedores quando precisam utilizar um tabela semelhante a Dual do Oracle acabam utilizando a RDB$Database.
Esse é um erro terrível, pois essa tabela traz informações do banco de dados em uso e isso leva tempo fazendo o comando de seleção mais lento.
Para a solução desse problema nada melhor do que criar um procedimento armazenado que retorne um valor fixo em uma coluna simulada.
A idéia é ter ao final um objeto de banco de dados com as mesmas características da tabela Dual do Oracle.

Español
Muchos desarrolladores cuando necesitan una tabla semejante a la Dual del Oracle terminan utilizando la RDB$Database.
Ese es un error terríble, pués esa tabla trae informaciones de la base de datos en uso y eso llega tiempo haciendo el comando de selección mas lento.
Para la solución de este problema lo mejor es crear un procedimiento almacenado que retorne un valor fijo en una columna simulada.
La idea es tener al final un objecto de base de datos con las mismas características de la tabla del Oracle.

English
When a lots of developers need a table similar to Oracle's Dual they use the RDB$Database.
This is a huge mistake because this table bring used database informations and it spend time doing the selection command slow.
For the solution of this problem the best decision is create a stored procedure to return a flat value in a simulated column.
The idea at the end is to have a database object with the some Oracle table characterists

==========================================================================*/

Set Term !! ;

/*========================================================================*/

Create Or Alter Procedure Dual
Returns (Dummy Char(1))
As
begin
  Dummy = 'X';
  Suspend;
end !!

Commit !!

/*========================================================================*/

Grant Execute On Procedure Dual To Publics !!

Commit !!

/*========================================================================*/

Set Term ; !!
Exit;

/*========================================================================*/
