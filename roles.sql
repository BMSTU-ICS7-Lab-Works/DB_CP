select * from pg_user;
select * from pg_roles;

create user unlogged_user with password 'unlogged_user';
create user logged_user with password 'logged_user';
create user guide with password 'guide';

drop user unlogged_user;
drop user logged_user;
drop user guide;

create role unlogged_role;
drop role unlogged_role;
GRANT select on excursions to unlogged_role;
GRANT select on guides to unlogged_role;
GRANT select on schedule to unlogged_role;
GRANT select on sights to unlogged_role;
GRANT select on "SightsExcursions" to unlogged_role;
GRANT select on users to unlogged_role;

REVOKE select on excursions from unlogged_role;
REVOKE select on guides from unlogged_role;
REVOKE select on schedule from unlogged_role;
REVOKE select on sights from unlogged_role;
REVOKE select on "SightsExcursions" from unlogged_role;
REVOKE select on users from unlogged_role

GRANT unlogged_role TO unlogged_user;

create role logged_role;
drop role logged_role;

GRANT select on excursions to logged_role;
GRANT select on guides to logged_role;
GRANT select on schedule to logged_role;
GRANT select on sights to logged_role;
GRANT select on "SightsExcursions" to logged_role;
GRANT select on users to logged_role;
GRANT select on "SelectedExcursions" to logged_role;

GRANT insert on users to logged_role;
GRANT insert on "SelectedExcursions" to logged_role;

GRANT delete on users to logged_role;
GRANT delete on "SelectedExcursions" to logged_role;

GRANT update on users to logged_role;
GRANT update on "SelectedExcursions" to logged_role;

GRANT logged_role TO logged_user;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO logged_user;

create role guide_role;
drop role guide_role;

GRANT select on excursions to guide_role;
GRANT select on guides to guide_role;
GRANT select on schedule to guide_role;
GRANT select on sights to guide_role;
GRANT select on "SightsExcursions" to guide_role;
GRANT select on users to guide_role;
GRANT select on "SelectedExcursions" to guide_role;

GRANT insert on excursions to guide_role;
GRANT insert on schedule to guide_role;
GRANT insert on sights to guide_role;
GRANT insert on "SightsExcursions" to guide_role;
GRANT insert on users to guide_role;
GRANT insert on "SelectedExcursions" to guide_role;

GRANT delete on excursions to guide_role;
GRANT delete on schedule to guide_role;
GRANT delete on sights to guide_role;
GRANT delete on "SightsExcursions" to guide_role;
GRANT delete on users to guide_role;
GRANT delete on "SelectedExcursions" to guide_role;

GRANT update on excursions to guide_role;
GRANT update on schedule to guide_role;
GRANT update on sights to guide_role;
GRANT update on "SightsExcursions" to guide_role;
GRANT update on users to guide_role;
GRANT update on "SelectedExcursions" to guide_role;

GRANT guide_role TO guide;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO guide;
select pg_has_role('postgres', 'postgres');

set role only_read
set role postgres