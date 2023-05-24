CREATE TABLE `clubs`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NULL,
  `country_id` int NULL,
  `foundation_date` date NULL,
  `value` float NULL,
  `stadium` varchar(255) NULL,
  `squad_size` int NULL,
  `average_age` float NULL,
  `national_players` int NULL,
  `current_transfer_record` float NULL,
  `foreigners` int NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `clubs_season`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `club_id` int NULL,
  `season_id` int NULL,
  `competition_id` int NULL,
  `rank` int NULL,
  `matches` int NULL,
  `win` int NULL,
  `draw` int NULL,
  `loss` int NULL,
  `goals_scored` int NULL,
  `goals_conceded` int NULL,
  `players_avg_age` int NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `competitions`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `country_id` int NOT NULL,
  `name` varchar(255) NULL,
  `teams_number` int NULL,
  `market_value` float NULL,
  `players_numbers` int NULL,
  `avg_age` float NULL,
  `foreigners` int NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `national`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `players`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NULL,
  `birth_date` date NULL,
  `age` int NULL,
  `height` double NULL,
  `current_club_id` int NULL,
  `club_joined` date NULL,
  `contract_expires` date NULL,
  `birth_place` varchar(255) NULL,
  `citizenship` varchar(255) NULL,
  `position` varchar(255) NULL,
  `national_id` int NULL,
  `current_value` float NULL,
  `agent` varchar(255) NULL,
  `foot` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `players_season`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `player_id` int NULL,
  `season_id` int NULL,
  `club_id` int NULL,
  `squad` int NULL,
  `appearance` int NULL,
  `point_per_goal` int NULL,
  `goals` int NULL,
  `assits` int NULL,
  `own_goals` int NULL,
  `yellow_card` int NULL,
  `second_yellow_card` int NULL,
  `red_card` int NULL,
  `penalty_goals` int NULL,
  `goals_conceded` int NULL,
  `clean_sheets` int NULL,
  `minutes_per_goal` int NULL,
  `minutes_played` int NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `seasons`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `start_date` date NULL,
  `end_date` date NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `transfers`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `player_id` int NOT NULL,
  `origin_club_id` int NOT NULL,
  `destination_club_id` int NOT NULL,
  `season_id` int NOT NULL,
  `market_value` int NULL,
  `fee` int NULL,
  PRIMARY KEY (`Id`)
);

