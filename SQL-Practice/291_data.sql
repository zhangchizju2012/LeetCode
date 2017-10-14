drop table if exists deliveries;
drop table if exists olines;
drop table if exists orders;
drop table if exists customers;
drop table if exists carries;
drop table if exists products;
drop table if exists categories;
drop table if exists stores;

create table stores (
  sid		int,
  name		text,
  phone		text,
  address	text,
  primary key (sid));
create table categories (
  cat           char(3),
  name          text,
  primary key (cat));
create table products (
  pid		char(6),
  name		text,
  unit		text,
  cat		char(3),
  primary key (pid),
  foreign key (cat) references categories);
create table carries (
  sid		int,
  pid		char(6),
  qty		int,
  uprice	real,
  primary key (sid,pid),	
  foreign key (sid) references stores,
  foreign key (pid) references products);
create table customers (
  cid		text,
  name		text,
  address	text,
  primary key (cid));
create table orders (
  oid		int,
  cid		text,
  odate		date,
  address	text,
  primary key (oid),
  foreign key (cid) references customers);
create table olines (
  oid		int,
  sid		int,
  pid		char(6),
  qty		int,
  uprice	real,
  primary key (oid,sid,pid),
  foreign key (oid) references orders,
  foreign key (sid) references stores,
  foreign key (pid) references products);
create table deliveries (
  trackingNo	int,
  oid		int,
  pickUpTime	date,
  dropOffTime	date,
  primary key (trackingNo,oid),
  foreign key (oid) references orders);

-- Data prepapred by Benjamin Lavin, blavin@ualberta.ca
-- Published on Sept 29, 2017

insert into stores values (10, 'Canadian Tire', '780-111-2222', 'Edmonton South Common');
insert into stores values (20, 'Walmart', '780-111-3333', 'Edmonton South Common');
insert into stores values (30, 'Loblaw City Market', '780-428-1945', 'Oliver Square');
insert into stores values (40, 'Shoppers Drug Mart', '780-426-7642', 'Edmonton City Centre');
insert into stores values (50, 'Shoppers Drug Mart', '780-474-8237', 'Kingsway Mall');
insert into stores values (60, 'Sears Department Store', '780-438-2098', 'Southgate Centre');
insert into stores values (70, 'Hudsons Bay', '780-435-9211', 'Southgate Centre');

insert into categories values ('dai', 'Dairy');
insert into categories values ('bak', 'Bakery');
insert into categories values ('pro', 'Produce');
insert into categories values ('ele', 'Electronics');
insert into categories values ('clo', 'Clothing and Apparel');
insert into categories values ('hom', 'Home Appliances');

insert into products values ('p10','4L milk 1%','ea', 'dai');
insert into products values ('p20','dozen large egg','ea', 'dai');
insert into products values ('p30','cheddar cheese (270g)','ea', 'dai');
insert into products values ('p40','white sliced bread','ea', 'bak');
insert into products values ('p50','dozen donuts','ea', 'bak');
insert into products values ('p60','red delicious apple','lb', 'pro');
insert into products values ('p70','gala apple','lb', 'pro');
insert into products values ('p80','baby carrots (454g)','ea', 'pro');
insert into products values ('p90','broccoli','lb', 'pro');
insert into products values ('p100','headphones','ea', 'ele');
insert into products values ('p110','8gb sdhc Card','ea', 'ele');
insert into products values ('p120','aaa batteries (8-pk)','ea', 'ele');
insert into products values ('p130','led hd tv, 32-in','ea', 'ele');
insert into products values ('p140','v-neck sweater','ea', 'clo');
insert into products values ('p150','cotton hoodie','ea', 'clo');
insert into products values ('p160','coffee maker','ea', 'hom');
insert into products values ('p170','toaster','ea', 'hom');
insert into products values ('p180','food mixer','ea', 'hom');

insert into carries values (10, 'p110', 75, 13.99);
insert into carries values (10, 'p120', 50, 12.99);
insert into carries values (10, 'p130', 20, 249.99);
insert into carries values (10, 'p160', 35, 24.99);
insert into carries values (10, 'p170', 40, 19.99);
insert into carries values (20, 'p10', 100, 4.70);
insert into carries values (20, 'p20', 80, 2.60);
insert into carries values (20, 'p30', 60, 3.79);
insert into carries values (20, 'p40', 120, 2.20);
insert into carries values (20, 'p50', 40, 4.00);
insert into carries values (20, 'p60', 100, 0.79);
insert into carries values (20, 'p70', 90, 1.15);
insert into carries values (20, 'p90', 0, 1.79);
insert into carries values (20, 'p100', 20, 11.79);
insert into carries values (30, 'p10', 90, 4.60);
insert into carries values (30, 'p30', 0, 3.75);
insert into carries values (30, 'p40', 100, 2.10);
insert into carries values (30, 'p50', 35, 5.99);
insert into carries values (30, 'p60', 98, 1.05);
insert into carries values (30, 'p70', 68, 1.25);
insert into carries values (30, 'p80', 40, 1.99);
insert into carries values (30, 'p90', 70, 1.79);
insert into carries values (30, 'p160', 30, 24.99);
insert into carries values (40, 'p10', 90, 4.75);
insert into carries values (40, 'p20', 70, 2.40);
insert into carries values (40, 'p30', 40, 3.89);
insert into carries values (40, 'p40', 89, 1.99);
insert into carries values (40, 'p60', 100, 0.79);
insert into carries values (40, 'p120', 35, 12.99);
insert into carries values (50, 'p10', 80, 4.75);
insert into carries values (50, 'p20', 80, 2.40);
insert into carries values (50, 'p30', 38, 3.89);
insert into carries values (50, 'p40', 84, 1.99);
insert into carries values (50, 'p120', 4, 12.99);
insert into carries values (60, 'p110', 50, 14.39);
insert into carries values (60, 'p120', 75, 13.99);
insert into carries values (60, 'p170', 50, 19.99);
insert into carries values (60, 'p100', 20, 13.49);
insert into carries values (70, 'p140', 32, 22.99);
insert into carries values (70, 'p150', 28, 54.99);
insert into carries values (70, 'p100', 9, 17.59);

insert into customers values ('c10', 'Jack Abraham', 'CS Dept, University of Alberta');
insert into customers values ('c20', 'Joe Samson', '9632-107 Ave');
insert into customers values ('c30', 'John Connor', '111-222 Ave');
insert into customers values ('c40', 'Sam Tritzen', '9702-162 St NW');
insert into customers values ('c50', 'Bryanna Petrovic', '391 Richfield Rd');
insert into customers values ('c60', 'John Doe', '11 Knottwood Rd');
insert into customers values ('c70', 'Jane Donald', '8012-122 St SW');
insert into customers values ('c80', 'Erin Branch', '54 Elanore Dr');

insert into orders values (100, 'c10', datetime('now', '-3 hours'), 'Athabasca Hall, University of Alberta');
insert into orders values (110, 'c40', datetime('now', '-3 hours'), '9702-162 St NW');
insert into orders values (120, 'c20', datetime('now', '-4 hours'), '9632-107 Ave');
insert into orders values (130, 'c60', datetime('now', '-5 hours'), '31 Jackson Ave');
insert into orders values (140, 'c40', datetime('now', '-8 hours'), '9702-162 St NW');
insert into orders values (150, 'c40', datetime('now', '-2 days'), '9702-162 St NW');
insert into orders values (160, 'c50', datetime('now', '-3 days'), '391 Richfield Rd');
insert into orders values (170, 'c10', datetime('now', '-4 days'), 'Athabasca Hall, University of Alberta');
insert into orders values (180, 'c20', datetime('now', '-4 days'), '9632-107 Ave');
insert into orders values (190, 'c50', datetime('now', '-5 days'), '391 Richfield Rd');
insert into orders values (200, 'c70', datetime('now', '-5 days'), '90 Jonah Ave');
insert into orders values (210, 'c70', datetime('now', '-5 days'), '8012-122 St SW');
insert into orders values (220, 'c80', datetime('now', '-6 days'), '54 Elanore Dr');
insert into orders values (230, 'c30', datetime('now', '-8 days'), '111-222 Ave');

insert into olines values (100, 20, 'p20', 1, 2.8);
insert into olines values (110, 30, 'p70', 1, 1.25);
insert into olines values (110, 30, 'p80', 2, 1.99);
insert into olines values (120, 20, 'p10', 1, 4.7);
insert into olines values (120, 40, 'p20', 1, 2.4);
insert into olines values (120, 40, 'p30', 1, 3.89);
insert into olines values (130, 70, 'p150', 1, 54.99);
insert into olines values (140, 40, 'p60', 2, 0.79);
insert into olines values (140, 30, 'p90', 2, 1.79);
insert into olines values (150, 60, 'p110', 1, 14.39);
insert into olines values (160, 20, 'p70', 1, 1.15);
insert into olines values (160, 30, 'p80', 1, 1.99);
insert into olines values (170, 20, 'p100', 2, 11.79);
insert into olines values (180, 40, 'p60', 1, 1.05);
insert into olines values (180, 40, 'p120', 1, 12.99);
insert into olines values (180, 40, 'p40', 1, 1.99);
insert into olines values (190, 10, 'p50', 1, 4);
insert into olines values (190, 10, 'p10', 1, 4.7);
insert into olines values (200, 10, 'p130', 1, 249.99);
insert into olines values (210, 10, 'p120', 1, 12.99);
insert into olines values (220, 30, 'p110', 1, 4.6);
insert into olines values (230, 20, 'p50', 2, 4);

insert into deliveries values (1000,100,datetime(), null);
insert into deliveries values (1001,110,datetime('now', '-3 hours'), datetime('now'));
insert into deliveries values (1002,120,datetime('now','-4 hours'), datetime('now'));
insert into deliveries values (1003,130,datetime(), null);
insert into deliveries values (1004,140,datetime('now', '-5 hours'), datetime('now', '-4 hours'));
insert into deliveries values (1005,150,datetime('now', '-1 day'), null);
insert into deliveries values (1006,160,datetime('now', '-1 day'), null);
insert into deliveries values (1007,170,datetime(), datetime('now', '-3 hours'));
insert into deliveries values (1008,180,datetime(), null);
insert into deliveries values (1009,190,datetime(), datetime('now'));
insert into deliveries values (1010,200,datetime(), null);
insert into deliveries values (1011,210,datetime('now', '-2 days'), datetime('now', '-1 day'));
insert into deliveries values (1012,220,datetime('now', '-2 days'), null);
insert into deliveries values (1013,230,datetime('now', '-8 days'), null);
