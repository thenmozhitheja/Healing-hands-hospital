create database Healing_hands;
use  Healing_hands;

create table login(
login_id int auto_increment primary key,
email varchar(30),
User_password varchar(20)
);
insert into login(email,User_password)
values('user1@gmail.com','user001'),('user2@gmail.com','user002'),('user3@gmail.com','user003');
select* from login;

create table appointment(
appointment_id int auto_increment primary key,
UserName varchar(50),
email varchar(30) unique,
phone_number varchar(15) unique,
services varchar(20),
date_of_appointment date,
time_of_appointment time,
note text
);
insert into appointment(UserName,email,phone_number,services,date_of_appointment,time_of_appointment,note)
values('user1','user1@gmail.com','4269564444','cardiology','2026-07-23','11:00','General checkup'),('user2','user2@gmail.com','6957777779','neurology','2026-07-18','10:00','General checkup'),('user3','user3@gmail.com','5836467856','pediatrics','2026-07-20','11:30','General checkup');
select* from appointment;

create table contact(
contact_id int auto_increment primary key,
user_Name varchar(30),
email varchar(50) unique,
phone_number varchar(15) unique,
sub varchar(100), 
queries text
);
insert into contact(user_Name,email,phone_number,sub,queries)
values('user1','user101@gmail.com','5732648852','clarifying issue on medical insurance.','can you accept the medical insurance given by the goverment of TamilNadu.');
select* from contact;

create table register(
    Reg_id int auto_increment primary key,
    full_name varchar(50),
    email varchar(50) unique,
    User_password varchar(20)
);
insert into register(full_name,email,User_password)
values('user1','user1@gmail.com','user001'),('user2','user2@gmail.com','user002'),('user3','user3@gmail.com','user003');
select* from register;



