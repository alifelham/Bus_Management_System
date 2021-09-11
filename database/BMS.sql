create database bus_management_system;
use bus_management_system;


create table bus(
bus_id varchar(25) primary key,
bus_type varchar(20),
schedule_day varchar(20),
seats tinyint,
mileage tinyint,
ticket_price smallint
);

create table user(
customer_id varchar(25) primary key,
full_name varchar(50),
password varchar(50),
phone_no varchar(11),
email varchar(50),
registration_time datetime,
CHECK (email like '%@%')
);

create table admin(
admin_id varchar(25) primary key,
password varchar(50),
privileges varchar(25)
);

create table location(
location_id varchar(25) primary key,
location_name varchar(25),
coordinates_N smallint,
coordinates_E smallint,
availability_status boolean
);

create table driver(
driver_id varchar(25) primary key,
driver_name varchar(50),
salary mediumint
);

create table reservation(
reservation_id int auto_increment,
customer_id  varchar(25),
bus_id varchar(25),
seat_count tinyint(25),
starting_location_id varchar(25),
destination_location_id varchar(25),
reservation_date datetime,
departure_time datetime,
primary key (reservation_id),
foreign key (customer_id) references user(customer_id)
on delete cascade on update cascade,
foreign key (bus_id) references bus(bus_id)
on delete cascade on update cascade,
foreign key (starting_location_id) references location(location_id)
on delete cascade,
foreign key (destination_location_id) references location(location_id)
);

create table payment(
payment_id int primary key auto_increment,
reservation_id int,
total_cost int,
foreign key (reservation_id) references reservation(reservation_id)
on delete cascade on update cascade
);

create table feedback(
feedback_id int primary key auto_increment,
customer_id varchar(25),
message text,
foreign key (customer_id) references user(customer_id)
);

create table driver_schedule(
driver_id varchar(25),
schedule_day varchar(20),
bus_id varchar(25),
primary key (driver_id, schedule_day),
foreign key(driver_id) references driver(driver_id),
foreign key(bus_id) references bus(bus_id)
);