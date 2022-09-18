/*
Personal finance manager, takes in income, figures out "spare" money after necessities, allows user to allocate funds between "extra" expenses divided between lesure and equipment for activites(hobbies, personal projects). 
Assign dates from when it's possible to buy/spend on a luxury automatically. For activities an average spend with a typical ticket+drinks can be used for this unless a specific event is planned out.
Allow putting money into savings which will "delete" money from the funds pool. Alternatively money can be put towards a specific use and also removed from the pool (i.e. money for rent, travel/lesuire on a certain date).
User can temporarily allocate funds towards before finalising them allowing them to decide the best usecase for their spare funds.
For regular expenses such as bills and other necessities they can me auto deducted to create a predicted funds pool.A variation/bounds for this may be implimented too. 
For necessities individual items wont be implimented as it would be too much work for the user. The program is not designed to track each shopping item but rather to track leftover money for the more interesting things in life.
Equipment gets put into a list for each activity, identical expenses are grouped together by period of time selected.
*/

PRAGMA Foreign_Keys=True;

CREATE TABLE Variables (
	VarID INTEGER PRIMARY KEY,
	Name NOT NULL UNIQUE,
	Value
);

CREATE TABLE Income (
	InID INTEGER PRIMARY KEY,
	Name NOT NULL UNIQUE,
	Category TEXT, /* Job, Benefits */
	Amount REAL DEFAULT 0.00,
	PayInDate TEXT, /* YYYY-MM-DD GMT */
	ActID INTEGER REFERENCES Activity(ActID)
);

CREATE TABLE Activity (
	ActID INTEGER PRIMARY KEY,
	Name NOT NULL UNIQUE,
	Category TEXT, /* Work, Hobby, Lesiure, Necessity */
	Budget REAL DEFAULT 0.00,
	Priority INTEGER DEFAULT 0 /* 0 - Highest */
);

CREATE TABLE Expense (
	ExID INTEGER PRIMARY KEY,
	Name NOT NULL,
	Category TEXT, /* Travel, Ticket, Food&Drink */
	URL TEXT,
	Description TEXT,
	Cost REAL DEFAULT 0.00,
	PayOutDate TEXT, /* YYYY-MM-DD GMT */
	ActID INTEGER REFERENCES Activity(ActID)
);

CREATE TABLE Equipment (
	EqID INTEGER PRIMARY KEY,
	Name NOT NULL,
	Category TEXT, /* Tools, Acessories, Clothes */
	URL TEXT,
	Description TEXT,
	Cost REAL DEFAULT 0.00,
	PayOutDate TEXT, /* YYYY-MM-DD GMT */
	ActID INTEGER REFERENCES Activity(ActID)
);
