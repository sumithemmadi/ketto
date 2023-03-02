CREATE DATABASE FundraiserDatabase;

CREATE TABLE `fundraisers`(
    `id` INT,
    `donated_amount` INT,
    `donated_amount_usd` INT,
    `donated_amount_local` INT,
    `name` VARCHAR(225),
    `iso_currency` VARCHAR(11),
    `donor_entity_details_id` INT,
    `is_anonymous` BOOLEAN
);

