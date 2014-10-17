CREATE TABLE registrar(
	email varchar(255) NOT NULL,
	password varchar(255) NOT NULL,
	bride varchar(255) NOT NULL,
	groom varchar(255) NOT NULL,
	PRIMARY KEY (email)
);


CREATE TABLE event(
	name varchar(255) NOT NULL,
	location varchar(255),
	event_date date NOT NULL,
	email varchar(255) NOT NULL,
	PRIMARY KEY (name,email),
	FOREIGN KEY (email) REFERENCES registrar(email)
);


CREATE TABLE guest(
  	name varchar(255) NOT NULL,
  	rsvp enum('NO','YES','MAYBE') NOT NULL DEFAULT 'MAYBE',  
  	event varchar(255) NOT NULL,
  	registrar_email varchar(255) NOT NULL,
  	PRIMARY KEY (name, event,registrar_email),
  	FOREIGN KEY (event,registrar_email) REFERENCES event(name, email)
);

