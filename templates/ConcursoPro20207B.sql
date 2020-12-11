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
   constraint uk_idProPue_categorias unique(nombre) 
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
    constraint uk_idCarrera_alumnos unique (idCarrera,idUsuario)
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
    constraint uk_idCarrera_problemaspropuestos unique(idEdicion,idProblema,idCategoria)
);

/*==============================================================*/
/* Table: Docentes                                               */
/*==============================================================*/

create table Docentes
(
idDocente int auto_increment not null,
escolaridad varchar(50),
especialidad varchar(50),
cedula int (8),
idCarrera int not null,
idUsuario int not null,
noControl int not null,
	constraint pk_docentes primary key (idDocente),
    constraint uk_cedula_docentes unique(cedula,noControl,idCarrera)
);
drop table Docentes;

/* -------------------------♠Pedro♠-----------------------------  */
/*==============================================================*/
/* Table: Carreras                                               */
/*==============================================================*/
create table Carreras (
idCarrera int auto_increment not null,
noControl int (8),
nombre varchar (50),
siglas varchar (6),
    constraint pk_carreras primary key (idCarrera),
    constraint uk_nombre_carrera unique (nombre,siglas)
);
/*==============================================================*/
/* Table: Equipos                                               */
/*==============================================================*/
create table Equipos(
idEquipo int auto_increment not null,
idProRes int not null,
idProPue int not null,
nombre varchar (40),
noControl1 int (8),
noControl2 int (8),
noControl3 int (8),
idDocentes int not null,
idCategorias int not null,
puntos int (2),
    constraint pk_equipos primary key(idEquipo),
    constraint uk_nombre_equipo unique (nombre,idCategorias,idProRes)
);
/*==============================================================*/
/* Table: Ediciones                                             */
/*==============================================================*/
create table Ediciones(
idEdicion int auto_increment not null,
idProPue int not null,
idProRes int not null,
nombre varchar (40),
fechaRegistro date,
fechaEvento date,
	constraint pk_ediciones primary key (idEdicion),
    constraint uk_nombre_ediciones unique (nombre,fechaEvento)
);
/*------------------- ØJoseLuisØ -------------------  */
/*==============================================================*/
/* Table: Usuarios                                               */
/*==============================================================*/
create table Usuarios
(
idUsuario int auto_increment not null,
nombre varchar(50),
sexo varchar(8),
telefono int not null,
email varchar (30),
estatus varchar (8),
tipo varchar (8),
password varchar (20),
	constraint pk_Usuarios primary key (idUsuario),
    constraint uk_nombre_usuarios unique(nombre,estatus,tipo)
);
/*==============================================================*/
/* Table: ProblemasResueltos                                    */
/*==============================================================*/
create table problemasResueltos
(
idProRes int auto_increment not null,
idProPue int not null,
idEquipo int not null,
tiempo int not null,
tiempoEjecucion int not null,
puntaje int not null,
	constraint pk_problemasResueltos primary key (idProRes),
    constraint uk_idProPue_problemasResueltos unique(idProPue,idEquipo)
);
/*==============================================================*/
/* Table: BancoProblemas                                        */
/*==============================================================*/
create table bancoProblemas
(
idProblema int auto_increment not null,
nombre varchar(50),
puntos varchar(8),
tiempoMaximo int not null,
descripcion varchar (120),
	constraint pk_bancoProblemas primary key (idProblema),
    constraint uk_nombre_bancoProblemas unique(nombre)
);
/*==============================================================*/
/* Restricciones FK	alter													                                             */
/*==============================================================*/
alter table docentes add constraint docentes_usuarios_FK foreign key (idUsuario)
      references usuarios (idUsuario);
      
alter table problemasResueltos add constraint problemasResueltos_ProblemasPropuestos_FK foreign key (idProPue)
      references ProblemasPropuestos (idProPue);


/*==============================================================*/
/* Creacion del Usuario para la conexion   y permisos           */
/*==============================================================*/
CREATE USER 'concursoprog_user'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON concursopro20207b.Categorias TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.Alumnos TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.ProblemasPropuestos TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.Docentes TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.Carreras TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.Equipos TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.Ediciones TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.Usuarios TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.problemasResueltos TO 'concursoprog_user'@'localhost';
GRANT ALL PRIVILEGES ON concursopro20207b.bancoProblemas TO 'concursoprog_user'@'localhost';