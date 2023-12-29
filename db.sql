-- CREATE TABLES

CREATE TABLE nurse(
	 n_id int primary key,
	 name varchar(30) not null,
	 phone varchar(15) unique
);

CREATE TABLE doctor(
	 d_id int primary key,
	 name varchar(30) not null,
	 phone varchar(15) unique,
     email varchar(50),
     specialization varchar(20),
     nurse_id int ,
     foreign key (nurse_id) references nurse(n_id)
);

CREATE TABLE patient(
	 p_id int primary key,
	 name varchar(30) not null,
	 phone varchar(15) unique,
     gender varchar(6),
     street varchar(30),
     city varchar(20),
     age int
);

CREATE TABLE appointment(
	 a_id int primary key,
	 patient_id int not null,
     doctor_id int not null,
     a_datetime DATETIME not null,
     notes varchar(100),
     foreign key (patient_id) references patient(p_id),
     foreign key (doctor_id) references doctor(d_id)
);



-- SELECT ALL
select * from nurse;
select * from doctor;
select * from patient;
select * from appointment;



-- DELETE ALL ROWS AND TABLES
TRUNCATE TABLE appointment;
drop table appointment;

TRUNCATE TABLE doctor;
drop table doctor;

TRUNCATE TABLE patient;
drop table patient;

TRUNCATE TABLE nurse;
drop table nurse;



