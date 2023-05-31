CREATE TABLE `clubs`  (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NULL,
  `country_id` varchar(255) NULL,
  `foundation_date` varchar(255) NULL,
  `value` float NULL,
  `stadium` varchar(255) NULL,
  `squad_size` int NULL,
  `average_age` float NULL,
  `national_players` int NULL,
  `current_transfer_record` float NULL,
  `foreigners` int NULL,
  `season` int NULL,
  `league_id` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `clubs_season`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `club_id` varchar(255) NULL,
  `season` int NULL,
  `competition_id` varchar(255) NULL,
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
  `id` varchar(255) NOT NULL,
  `country_id` varchar(255) NULL,
  `name` varchar(255) NULL,
  `teams_number` int NULL,
  `market_value` float NULL,
  `players_numbers` int NULL,
  `avg_age` float NULL,
  `foreigners` int NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `national`  (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `players`  (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NULL,
  `birth_date` varchar(255) NULL,
  `age` int NULL,
  `height` float NULL,
  `current_club_id` varchar(255) NULL,
  `club_joined` varchar(255) NULL,
  `contract_expires` varchar(255) NULL,
  `birth_place` varchar(255) NULL,
  `citizenship` varchar(255) NULL,
  `position` varchar(255) NULL,
  `national_id` varchar(255) NULL,
  `current_value` float NULL,
  `agent` varchar(255) NULL,
  `foot` varchar(255) NULL,
  `shirt_number` int NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `players_season`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `player_id` varchar(255) NULL,
  `season` int NULL,
  `club_id` varchar(255) NULL,
  `squad` int NULL,
  `appearance` int NULL,
  `point_per_goal` float NULL,
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
  `age` int NULL,
  `position` varchar(255) NULL,
  `height` int NULL,
  `current_international` varchar(255) NULL,
  `agent` varchar(255) NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `transfers`  (
  `Id` int NOT NULL AUTO_INCREMENT,
  `player_id` varchar(255) NULL,
  `origin_club_id` varchar(255) NULL,
  `destination_club_id` varchar(255) NULL,
  `season` varchar(255) NULL,
  `market_value` float NULL,
  `fee` float NULL,
  PRIMARY KEY (`Id`)
);

