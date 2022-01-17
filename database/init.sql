create table if not exists todo (
        id integer primary key autoincrement,
        title varchar(50) not null,
        description  varchar(255)
    );