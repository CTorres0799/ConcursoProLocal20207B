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
    constraint uk_nombre_usuarios unique(nombre)
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
TiempoEjecucion int not null,
puntaje int not null,
	constraint pk_problemasResueltos primary key (idProRes),
    constraint uk_idProPue_problemasResueltos unique(idProPue)
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
descripcion varchar (30),
	constraint pk_bancoProblemas primary key (idProblema),
    constraint uk_nombre_bancoProblemas unique(nombre)
);
/*==============================================================*/
/* Restricciones FK	alter													                                             */
/*==============================================================*/
alter table Actos add constraint Actos_Aulas_FK foreign key (idSala)
      references Salas (idSala);


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