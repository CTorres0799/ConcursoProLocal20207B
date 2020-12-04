create database ConcursoPro20207B;
use ConcursoPro20207B

/* -----------------------Cristian----------------------------  */
/*==============================================================*/
/* Table: Categorias                                               */
/*==============================================================*/

create table Categorias 
( 
idCategoria int auto_increment not null,
nombre varchar(30),
semestreLimite char(2),
idProPue int,
   constraint pk_categorias primary key (idCategoria),
   constraint uk_idProPue_categorias unique(idProPue) 
);

/*==============================================================*/
/* Table: Alumnos                                               */
/*==============================================================*/

create table Alumnos 
(
NoControl int not null,
semestre char(2),
idUsuario int not null,
idCarrera int not null,
idProRes int not null,
	constraint pk_alumnos primary key (NoControl),
    constraint uk_idCarrera_alumnos unique(idCarrera)
);

/*==============================================================*/
/* Table: ProblemasPropuestos                                   */
/*==============================================================*/

create table ProblemasPropuestos 
(
idProPue int auto_increment not null,
globo varchar(15),
idProblema int not null,
idEdicion int not null,
idCategoria int not null,
	constraint pk_problemaspropuestos primary key (idProPue),
    constraint uk_idCarrera_problemaspropuestos unique(idProblema)
);

/*==============================================================*/
/* Table: Docentes                                               */
/*==============================================================*/

create table Docentes
(
idDocente int auto_increment not null,
escolaridad varchar(4),
especialidad varchar(40),
cedula int (8),
idCarrera int not null,
idUsuario int not null,
noControl int not null,
	constraint pk_docentes primary key (idDocente),
    constraint uk_cedula_docentes unique(cedula)
);

/* -------------------------♠Pedro♠-----------------------------  */
/*==============================================================*/
/* Table: Carreras                                               */
/*==============================================================*/

/*==============================================================*/
/* Table: Equipos                                               */
/*==============================================================*/
create table Equipos(
idProRes int not null,
idProPue int not null,
idEquipo int auto_increment not null
);
/*==============================================================*/
/* Table: Ediciones                                             */
/*==============================================================*/
create table Ediciones(
idEdicion int auto_increment not null
);
/*------------------- ØJoseLuisØ -------------------  */
/*==============================================================*/
/* Table: Usuarios                                               */
/*==============================================================*/

/*==============================================================*/
/* Table: ProblemasResueltos                                    */
/*==============================================================*/

/*==============================================================*/
/* Table: BancoProblemas                                        */
/*==============================================================*/