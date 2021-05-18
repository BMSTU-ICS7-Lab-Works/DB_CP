select * from pg_user;
select * from pg_roles;

create role reader;
GRANT select on excursions to reader;

GRANT reader TO unlogged_user;


--select pg_has_role('postgres', 1);


create user unlogged_user with password 'unlogged_user'

create role editor;
GRANT select on users to editor;
GRANT select on SightsExcursions to editor;
GRANT select on SightsExcursions to editor;

GRANT reader TO logged_user;
GRANT editor TO logged_user;
create user logged_user with password 'logged_user'

GRANT select on dtp to reader
REVOKE select on dtp FROM reader;

drop user reader;

select * from dtp
insert into dtp values (10, 2, 'крушение', '1998-06-17', '21:50')

set role reader
set role postgres