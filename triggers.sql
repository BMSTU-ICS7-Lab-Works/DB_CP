CREATE FUNCTION trigger_create_excursion () RETURNS trigger AS 
$$
	BEGIN
		if ((SELECT count(*) from excursions where excursions.price = NEW.price) <= 0) then
			return NULL;
		else
    		return NEW;
		end if;
END;
$$ LANGUAGE  plpgsql;

CREATE TRIGGER createExcursion
BEFORE INSERT ON excursions FOR EACH ROW
EXECUTE PROCEDURE trigger_create_excursion ()


CREATE FUNCTION trigger_create_sight () RETURNS trigger AS 
$$
	BEGIN
		if ((SELECT count(*) from sights where NEW.build_date <= CURRENT_DATE and sights.id <> NEW.id) > 0) then
			return NULL;
		else
    		return NEW;
		end if;
END;
$$ LANGUAGE  plpgsql;

CREATE TRIGGER createSight
BEFORE INSERT ON sights FOR EACH ROW
EXECUTE PROCEDURE trigger_create_sight ();

drop trigger createSight on sights;
