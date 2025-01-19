drop table if exists `data-analytics1-437123.avocado_data.avocado_prices3`;
create table `data-analytics1-437123.avocado_data.avocado_prices3` as
(select * from `avocado_data.avocado_prices_temp`); 