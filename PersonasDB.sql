-id
-nombre
-edad
-estatura
-genero
-signo_zodiacal
-sexualidad
-color_ojos
-color_piel
-ingreso_mensual

CREATE TABLE personas (
  id INT NOT NULL,
  nombre VARCHAR(45) NULL,
  edad INT NULL,
  estatura FLOAT NULL,
  genero VARCHAR(45) NULL,
  signo VARCHAR(45) NULL,
  sexualidad VARCHAR(45) NULL,
  color_ojos VARCHAR(45) NULL,
  color_piel VARCHAR(45) NULL,
  ingreso FLOAT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;

insert into personas 
values (1,'Carlos Slim', 80, 1.73, 'Masculino', 'Acuario', 'Heterosexual', 'Cafe oscuro', 'Clara', 71000);

insert into personas
values (2,'Maria Aramburuzabala', 56, 1.65, 'Femenino', 'Tauro', 'Heterosexual', 'Verdes', 'Clara', 60000 );

insert into personas
values (3, 'Carlos Vela', 30, 1.77, 'Masculino', 'Piscis', 'Heterosexual', 'Cafe oscuro', 'Morena', 63000);

insert into personas
values (4, 'Deneva Cagigas', 24, 1.62, 'Femenino', 'Aries', 'Heterosexual', 'Cafe claro', 'Clara', 20000);

insert into personas
values (5, 'Erik Canales', 36, 1.70, 'Masculino', 'Escorpio', 'Heterosexual', 'Cafe claro', 'Clara', 30000);

insert into personas
values (6, 'Elizabeth Woolridge', 34, 1.70, 'Femenino', 'Cancer', 'Heterosexual', 'Verdes', 'Blanca', 65000);

insert into personas
values (7, 'Juanpa Zurita', 23, 1.80, 'Masculino', 'Aries', 'Heterosexual', 'Verdes', 'Blanca', 65000);

insert into personas
values (8, 'Mariand Castrejon', 26, 1.58, 'Femenino', 'Piscis', 'Heterosexual', 'Cafe oscuro', 'Clara', 75000);

insert into personas
values (9, 'Luis Arturo Villar', 28, 1.72, 'Masculino', 'Piscis', 'Heterosexual', 'Cafe oscuro', 'Blanca', 85000);

insert into personas
values (10, 'Miranda Ibanez', 25, 1.73, 'Femenino', 'Piscis', 'Heterosexual', 'Negros', 'Blanca', 60000);

insert into personas
values (11, 'Robin Schulz', 32, 1.82, 'Masculino', 'Tauro', 'Heterosexual', 'Cafe claro', 'Clara', 75000);

insert into personas
values (12,'Steven Morrissey', 60, 1.80, 'Masculino', 'Geminis', 'Asexual', 'Azules', 'Blanca', 61000);

insert into personas
values (13, 'Caitlyn Jenner', 70, 1.88, 'Mujer Transexual', 'Escorpio', 'Asexual', 'Cafe oscuro', 'Blanca', 40000);

insert into personas
values (14, 'Bella Thorne', 22, 1.73, 'Femenino', 'Libra', 'Pansexual', 'Cafe claro', 'Blanca', 45000);

insert into personas
values (15, 'Miley Cyrus', 27, 1.65, 'Femenino', 'Sagitario', 'Pansexual', 'Azules', 'Blanca', 100000);

select * from personas;