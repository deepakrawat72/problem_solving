#
create table entries (
    name varchar(20),
    address varchar(20),
    email varchar(20),
    floor int,
    resources varchar(10)
);

insert into entries values ('A','Bangalore','A@gmail.com',1,'CPU'),
insert into entries values ('A','Bangalore','A1@gmail.com',1,'CPU');
insert into entries values ('A','Bangalore','A2@gmail.com',2,'DESKTOP');
insert into entries values ('B','Bangalore','B@gmail.com',2,'DESKTOP');
insert into entries values ('B','Bangalore','B1@gmail.com',2,'DESKTOP');
insert into entries values ('B','Bangalore','B2@gmail.com',1,'MONITOR');