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
create table Carreras (
idCarrera int auto_increment not null,
noControl int (8),
Nombre varchar (50),
Siglas varchar (6),
    constraint pk_carreras primary key (idCarrera),
    constraint uk_nombre_carrera unique (nombre)
);
/*==============================================================*/
/* Table: Equipos                                               */
/*==============================================================*/
create table Equipos(
idProRes int not null,
idProPue int not null,
idEquipo int auto_increment not null,
Nombre varchar (40),
noControl1 int (8),
noControl2 int (8),
noContro3 int (8),
idDocentes int not null,
idCategorias int not null,
Puntos int (2),
    constraint pk_equipos primary key(idEquipo),
    constraint uk_nombre_equipo unique (nombre)
);
/*==============================================================*/
/* Table: Ediciones                                             */
/*==============================================================*/
create table Ediciones(
idEdicion int auto_increment not null,
idProPue int not null,
idProRes int not null,
Nombre varchar (40),
FechaRegistro date,
FechaEvento date,
	constraint pk_ediciones primary key (idEdicion),
    constraint uk_nombre_ediciones unique (nombre)
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