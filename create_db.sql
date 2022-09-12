drop table if exists subscriptions;

create table if not exists subscriptions (
	id SERIAL primary key,
	user_id VARCHAR (255) not null,
	status BOOLEAN not null default (true),
	is_admin BOOLEAN not null default (false)
);

drop table if exists cities;

create table if not exists cities (
	id SERIAL primary key,
	city_name VARCHAR (50) not null
);

drop table if exists links;

create table if not exists links (
	id SERIAL primary key,
	link VARCHAR (255) not null
);

drop table if exists networks;

create table if not exists networks (
	id SERIAL primary key,
	network_name VARCHAR (50),
	link_id bigint,
	foreign key (link_id) references links(id) on
update
	cascade on
	delete
		restrict
);

drop table if exists cinemas;

create table if not exists cinemas (
	id SERIAL primary key,
	cinema_name VARCHAR (50) not null,
	city_id bigint not null,
	network_id bigint,
	link_id bigint,
	foreign key (city_id) references cities(id) on
update
	cascade on
	delete
		restrict,
		foreign key (network_id) references networks(id) on
		update
			cascade on
			delete
				restrict,
				foreign key (link_id) references links(id) on
				update
					cascade on
					delete
						restrict
);

drop table if exists movies;

create table if not exists movies (
	id SERIAL primary key,
	movie_name VARCHAR (255) not null,
	imdb_rating float,
	kinopoisk float,
	description VARCHAR (255)
);

drop table if exists in_theatres;

create table if not exists in_theatres(
	id SERIAL primary key,
	movie_id bigint not null,
	cinema_id bigint not null,
	foreign key (movie_id) references movies(id) on
update
	cascade on
	delete
		restrict,
		foreign key (cinema_id) references cinemas(id) on
		update
			cascade on
			delete
				restrict
);

drop table if exists media_types;

create table if not exists media_types (
	id SERIAL primary key,
	media_type VARCHAR(50),
	created_at timestamp default CURRENT_TIMESTAMP
);

drop table if exists media;

create table if not exists media(
	id SERIAL primary key,
    media_type_id BIGINT not null,
    movie_id BIGINT not null,
  	body text,
    filename VARCHAR(255),
    filesize INT,
	metadata JSON,
    created_at timestamp default CURRENT_TIMESTAMP,
    foreign key (movie_id) references movies(id),
    foreign key (media_type_id) references media_types(id)
);

	
drop table if exists photo_albums;

create table if not exists photo_albums(
	id SERIAL primary key,
	album_name VARCHAR (50),
	movie_id bigint not null,
	foreign key (movie_id) references movies(id) on
update
	cascade on
	delete
		restrict
);

drop table if exists photos;

create table if not exists photos (
	id SERIAL primary key,
	ph_album_id BIGINT not null,
	media_id BIGINT not null,
	foreign key (ph_album_id) references photo_albums(id) on
update
	cascade on
	delete
		restrict,
		foreign key (media_id) references media(id) on
		update
			cascade on
			delete
				restrict
);

