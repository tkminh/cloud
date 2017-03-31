CREATE TABLE user_master (
 contact_id integer PRIMARY KEY,
 email text NOT NULL UNIQUE,
 pwd text NOT NULL,
 first_name text,
 last_name text,
 mobile text,
 phone text,
 status int
);
