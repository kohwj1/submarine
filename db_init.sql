CREATE TABLE area
(
  areaId   TEXT    NOT NULL UNIQUE,
  regionId INTEGER NOT NULL,
  name     TEXT    NULL,
  reqRank  INTEGER NOT NULL,
  exp      INTEGER NOT NULL DEFAULT 0,
  distance INTEGER NULL,
  time     INTEGER NULL
);

CREATE TABLE navigation
(
  areaFrom TEXT    NOT NULL,
  areaTo   TEXT    NOT NULL,
  distance INTEGER NULL,
  time     INTEGER NULL
);

CREATE TABLE unlock
(
  areaFrom   TEXT NOT NULL,
  areaUnlock TEXT NOT NULL
);

CREATE TABLE region
(
  regionId INTEGER NOT NULL UNIQUE,
  name     TEXT    NULL
);

CREATE TABLE rewards
(
  areaId TEXT    NOT NULL,
  tier   INTEGER NOT NULL DEFAULT 0,
  itemId TEXT    NULL
);

CREATE TABLE items
(
  itemId TEXT NOT NULL UNIQUE,
  name   TEXT NULL
);

CREATE TABLE place
(
  id        INTEGER NULL,
  expansion TEXT    NULL,
  region    TEXT    NULL,
  name_ko   TEXT    NULL,
  name_en   TEXT    NULL,
  category  TEXT    NULL,
  isSpoiler INTEGER NULL
);

.mode csv
.import instance/area.csv area
.import instance/navigation.csv navigation
.import instance/unlock.csv unlock
.import instance/region.csv region
.import instance/rewards.csv rewards
.import instance/items.csv items
.import instance/place.csv place

.exit