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

insert into personas
values (16, 'Harry Styles', 26, 1.88, 'Masculino', 'Acuario', 'Heterosexual', 'Verdes', 'Blanca', 60000);

insert into personas
values (17, 'Natalie Portman', 38, 1.60, 'Femenino', 'Geminis', 'Heterosexual', 'Cafe claro', 'Blanca', 80000);

insert into personas
values (18, 'Chris Hemsworth', 36, 1.91, 'Maculino', 'Leo', 'Heterosexual', 'Azules', 'Blanca', 100000);

insert into personas
values (19, 'Zendaya', 23, 1.78, 'Femenino', 'Virgo', 'Heterosexual', 'Cafe oscuro', 'Morena', 200000);

insert into personas
values (20, 'Michael B Jordan', 32, 1.82, 'Masculino', 'Acuario', 'Heterosexual', 'Cafe oscuro', 'Negra', 50000);

insert into personas
values (21, 'Zac Efron', 32, 1.73, 'Masculino', 'Libra', 'Heterosexual', 'Azul', 'Blanca', 60000);

insert into personas
values (22, 'Alicia Vikander', 31, 1.65, 'Femenino', 'Libra', 'Heterosexual', 'Cafe Oscuro', 'Clara', 60000);

insert into personas
values (23, 'Kristen Stewart', 29, 1.66, 'Femenino', 'Aries', 'Homosexual', 'Verde', 'Blanca', 80000);

insert into personas
values (24, 'Ellen Page', 32, 1.55, 'Femenino', 'Piscis', 'Homosexual', 'Cafe claro', 'Blanca', 30000);

insert into personas
values (25, 'Michelle Rodriguez', 41, 1.65, 'Femenino', 'Cancer', 'Homosexual', 'Cafe oscuro', 'Morena', 40000);

insert into personas
values (26, 'Ricky Martin', 48, 1.88, 'Masculino', 'Capricornio', 'Homosexual', 'Cafe claro', 'Clara', 100000);

insert into personas
values (27, 'Michael Fassbender', 42, 1.83, 'Masculino', 'Aries', 'Heterosexual', 'Azul', 'Blanca', 50000);

insert into personas
values (28, 'Tom Hiddleston', 38, 1.88, 'Masculino', 'Acuario', 'Heterosexual', 'Azul', 'Blanca', 90000);

insert into personas
values (29, 'Tom Holland', 23, 1.70, 'Masculino', 'Geminis', 'Heterosexual', 'Cafe oscuro', 'Blanca', 20000);

insert into personas
values (30, 'Jennifer Lawrence', 29, 1.75, 'Femenino', 'Leo', 'Heterosexual', 'Azul', 'Blanca', 20000);

insert into personas
values (31, 'Felicity Jones', 36, 1.60, 'Femenino', 'Libra', 'Heterosexual', 'Verde', 'Blanca', 80000);

insert into personas
values (32, 'Leonardo Di Caprio', 45, 1.83, 'Masculino', 'Escorpio', 'Heterosexual', 'Azul', 'Blanca', 10000);

insert into personas
values (33, 'Brad Pitt', 56, 1.80, 'Masculino', 'Sagitario', 'Heterosexual', 'Azul', 'Blanca', 60000);

insert into personas
values (34, 'Orlando Bloom', 43, 1.80, 'Masculino', 'Capricornio', 'Heterosexual', 'Cafe oscuro', 'Blanca', 80000);

insert into personas
values (35, 'Shakira', 43, 1.57, 'Femenino', 'Acuario', 'Heterosexual', 'Cafe oscuro', 'Clara', 100000);

insert into personas
values (36, 'Rihanna', 31, 1.73, 'Femenino', 'Piscis', 'Heterosexual', 'Verde', 'Morena', 200000);

select * from personas;