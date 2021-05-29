truncate table guides cascade;
truncate table sights cascade;
truncate table excursions cascade;
truncate table "SightsExcursions" cascade;

insert into guides values (1, 'Аркадий', 'Искаков', 'Муратович',
						   'История 20 века', 'Закончил вуз в Казахстане, проходил повышение квалификации в Москве', 12);
insert into guides values (2, 'Дмитрий', 'Куликов', 'Алексеевич',
						   'Эксперт по древней культуре', 'Закончил Саранский университет, работал в Москве в музее австралопитеков', 6);
insert into guides values (3, 'Никита', 'Гарасев', 'Витальевич',
						   'Гид-переводчик', 'Родился в Капотне, там не пригодился. Пригодился в Мытищах', 2);
insert into guides values (4, 'Александр', 'Сучков', 'Дмитриевич',
						   'Мастер 3 вещей', 'Ходит есть, лежать и носит шорты', 5);
insert into guides values (5, 'Никита', 'Павлов', 'Александрович',
						   'История всего', 'Бабушара', 6);
						   
insert into excursions values (1, 'У стен Московского Кремля', 'Что вас ожидает: Красная площадь, Александровский сад,
							   Древний московский «сити»', 5, 670);
insert into excursions values (2, 'Неизведанная Таганка', 'Мы отправимся гулять по той части Таганского района,
							   которая лежит за пределами Садового кольца. Вы полюбуетесь великолепным архитектурным ансамблем
							   Рогожской ямской слободы; увидите дом, где родился основатель современного театра — К.С. Станиславский;
							   рассмотрите величественный храм Святого Мартина Исповедника и побываете в том уголке Москвы, который получил
							   премию Королевского института британских архитекторов.', 2, 3000);

insert into sights values (1, 'Храм Василия Блаженного', '02-10-1552', 'Шатровый храм', 'Постник Яковлев', 'Православный \
                                                     храм на Красной площади в Москве, памятник русской архитектуры.');
insert into sights values (2, 'Памятник Петру 1', '02-02-1997', 'Памятник', 'Зураб Константинович Церетели', 'Один из самых \
						   высоких памятников в России. Общая высота памятника 98 метров, высота фигуры Петра 18 м.');

INSERT INTO public."SightsExcursions"(
	"sightsId", "excursionsId")
	VALUES (1, 2);
	
INSERT INTO public."SightsExcursions"(
	"sightsId", "excursionsId")
	VALUES (1, 1);

INSERT INTO public."SightsExcursions"(
	"sightsId", "excursionsId")
	VALUES (2, 1);
	
select * from excursions;
select * from sights;
select * from "SightsExcursions";
select * from "SelectedExcursions";
select * from schedule;
select * from users

drop table users cascade;
drop table excursions cascade;
drop table guides cascade;
drop table schedule cascade;
drop table sights cascade;
drop table "SightsExcursions" cascade;
drop table "SelectedExcursions" cascade;