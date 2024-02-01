/*
SQLyog Ultimate v13.1.7 (64 bit)
MySQL - 10.6.12-MariaDB-1:10.6.12+maria~deb11 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

CREATE TABLE IF NOT EXISTS `ovh-domain` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `domain` varchar(256) NOT NULL,
  `expiration_date` date NOT NULL,
  `expiration_day` smallint(6) NOT NULL,
  `admin` varchar(32) NOT NULL,
  `billing` varchar(32) NOT NULL,
  `tech` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
)