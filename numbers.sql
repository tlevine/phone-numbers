CREATE TABLE IF NOT EXISTS "responses" (
  "country" TEXT NOT NULL,
  "d0" TEXT NOT NULL,
  "d1" TEXT NOT NULL,
  "d2" TEXT NOT NULL,
  "d3" TEXT NOT NULL,
  "d4" TEXT NOT NULL,
  "d5" TEXT NOT NULL,
  "d6" TEXT NOT NULL,
  "d7" TEXT NOT NULL,
  "d8" TEXT NOT NULL,
  "d9" TEXT NOT NULL,
  UNIQUE ("country","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9")
);

INSERT OR REPLACE INTO "responses" VALUES ('880','1','4','1','4','1','4','3','8','7','0');
INSERT OR REPLACE INTO "responses" VALUES ('880','4','4','1','4','1','4','4','7','6','7');
INSERT OR REPLACE INTO "responses" VALUES ('880','1','4','1','4','1','4','4','4','2','8');

SELECT count(*)
