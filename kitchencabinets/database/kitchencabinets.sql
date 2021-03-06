-- phpMyAdmin SQL Dump
-- version 3.3.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 24, 2013 at 02:52 PM
-- Server version: 5.1.63
-- PHP Version: 5.3.5-1ubuntu7.11

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `kitchencabinets`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--


DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_group_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
CREATE TABLE IF NOT EXISTS `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_message`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=40 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add log entry', 6, 'add_logentry'),
(17, 'Can change log entry', 6, 'change_logentry'),
(18, 'Can delete log entry', 6, 'delete_logentry'),
(19, 'Can add source', 7, 'add_source'),
(20, 'Can change source', 7, 'change_source'),
(21, 'Can delete source', 7, 'delete_source'),
(22, 'Can add thumbnail', 8, 'add_thumbnail'),
(23, 'Can change thumbnail', 8, 'change_thumbnail'),
(24, 'Can delete thumbnail', 8, 'delete_thumbnail'),
(28, 'Can add auth user', 10, 'add_authuser'),
(29, 'Can change auth user', 10, 'change_authuser'),
(30, 'Can delete auth user', 10, 'delete_authuser'),
(31, 'Can add auth user', 11, 'add_authuser'),
(32, 'Can change auth user', 11, 'change_authuser'),
(33, 'Can delete auth user', 11, 'delete_authuser'),
(34, 'Can add cart', 12, 'add_cart'),
(35, 'Can change cart', 12, 'change_cart'),
(36, 'Can delete cart', 12, 'delete_cart'),
(37, 'Can add item', 13, 'add_item'),
(38, 'Can change item', 13, 'change_item'),
(39, 'Can delete item', 13, 'delete_item');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=47 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `username`, `first_name`, `last_name`, `email`, `password`, `is_staff`, `is_active`, `is_superuser`, `last_login`, `date_joined`) VALUES
(1, 'admin', '', '', 'admin@toobler.com', 'pbkdf2_sha256$10000$O3p5ReODqp7H$NxjhrP9GmpADIAqiQnTbqioUviDCSlRNJOMbMMZAvlU=', 1, 1, 1, '2013-06-21 02:50:48', '2013-06-04 07:33:29'),
(3, 'test', 'test', '', '', 'pbkdf2_sha256$10000$O3p5ReODqp7H$NxjhrP9GmpADIAqiQnTbqioUviDCSlRNJOMbMMZAvlU=', 0, 1, 0, '2013-06-22 00:27:13', '2013-06-18 02:24:52'),
(14, 'toobler', '', '', 'sakeer1@toobler.com', 'sha1$d8f1f$df6d4acc5c563af5c6ef0544e506717b68bb1f3b', 1, 1, 1, '2013-06-24 00:27:01', '2013-06-21 03:58:03'),
(34, 'sakeer', 'sakeer', 'husain', 'sakeer@toobler.com', 'sha1$5b419$81ea6d6baa8e48eb0ccafac755318317fba664c2', 0, 1, 0, '2013-06-21 07:24:07', '2013-06-21 07:24:01'),
(45, 'shebeer', 'shebeer', 'ibrahim', 'bismi71188@gmail.com', 'sha1$e9157$dba2026f722349de5c78e2666f6a5518b189499d', 0, 1, 0, '2013-06-24 00:23:04', '2013-06-24 00:22:58');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_groups`
--


-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `auth_user_user_permissions`
--


-- --------------------------------------------------------

--
-- Table structure for table `cabinet`
--

DROP TABLE IF EXISTS `cabinet`;
CREATE TABLE IF NOT EXISTS `cabinet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cabinet_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cabinet_name` (`cabinet_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `cabinet`
--


-- --------------------------------------------------------

--
-- Table structure for table `carriers`
--

DROP TABLE IF EXISTS `carriers`;
CREATE TABLE IF NOT EXISTS `carriers` (
  `id` int(11) NOT NULL,
  `carrier_name` varchar(45) DEFAULT NULL,
  `carrier_logo` blob,
  `carrier_status` set('active','inactive') DEFAULT 'inactive',
  `tax_id` int(11) DEFAULT NULL,
  `max_package_height` float DEFAULT NULL,
  `max_package_width` float DEFAULT NULL,
  `max_package_depth` float DEFAULT NULL,
  `max_package_weight` float DEFAULT NULL,
  `carrier_price` float DEFAULT NULL,
  `carrier_url` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_carriers_tax_idx` (`tax_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `carriers`
--


-- --------------------------------------------------------

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(45) DEFAULT NULL,
  `category_image` blob,
  `category_order` int(11) DEFAULT NULL,
  `category_status` set('active','inactive') DEFAULT 'active',
  PRIMARY KEY (`id`),
  UNIQUE KEY `category_name_UNIQUE` (`category_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `category_name`, `category_image`, `category_order`, `category_status`) VALUES
(4, 'automotive', NULL, 2, 'active');

-- --------------------------------------------------------

--
-- Table structure for table `codes`
--

DROP TABLE IF EXISTS `codes`;
CREATE TABLE IF NOT EXISTS `codes` (
  `id` int(11) NOT NULL,
  `code_group` varchar(45) DEFAULT NULL,
  `code_value` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `codes`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `django_admin_log`
--


-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'log entry', 'admin', 'logentry'),
(7, 'source', 'easy_thumbnails', 'source'),
(8, 'thumbnail', 'easy_thumbnails', 'thumbnail'),
(10, 'auth user', 'userman', 'authuser'),
(11, 'auth user', 'registration', 'authuser'),
(12, 'cart', 'cart', 'cart'),
(13, 'item', 'cart', 'item'),
(14, 'product', 'product', 'product');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3ff1fe95440b6e4a0350bc0c1232bb4c', 'NGFiZmNiZjg4YTBiMGIwNTY0MTA5NTQ5NTllMzczZWNhYTZjMTUyZTqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n', '2013-07-06 00:36:01'),
('45d2ed47411122ee3149cac01b2ac4dc', 'MmEyNWIyYTQ0NTE4NjExZmFjMzRiZmZmM2IzNjZkMGRlZjIzYzI0MDqAAn1xAShVCnRlc3Rjb29r\naWVVBndvcmtlZHECVRJfYXV0aF91c2VyX2JhY2tlbmRVKWRqYW5nby5jb250cmliLmF1dGguYmFj\na2VuZHMuTW9kZWxCYWNrZW5kVQ1fYXV0aF91c2VyX2lkigEOdS4=\n', '2013-07-08 02:23:45'),
('9gccw91w98plbozav6mf3y354evmw05g', 'ODY5YTk2ZmE2NDY0MTAzMmM4OGZhMTJmNzA3MTZiMDczYjVkMDYxYTqAAn1xAShVB0NBUlQtSURxAooBAVUNX2F1dGhfdXNlcl9pZIoBA1USX2F1dGhfdXNlcl9iYWNrZW5kVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHUu', '2013-07-06 05:09:14'),
('a79792e20f5d43ff6f42d806ee6ce43f', 'ZTVhODIyMzMyY2U0ODEyOTIyZDIxNDEwOTM3MWIxNTcxNTI4YTU3ZjqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n', '2013-07-08 02:37:00'),
('c4a0edc745ac41e21699819a48ea11c4', 'OGU1NjFkZjM2MjkzMzZjYjkzY2ZjZWUyODQxZGY2MmIxMTE3NWZhYTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQ51Lg==\n', '2013-07-05 03:59:00'),
('e6cd86c80ba65e564df3a2cb7126a7e3', 'ZTVhODIyMzMyY2U0ODEyOTIyZDIxNDEwOTM3MWIxNTcxNTI4YTU3ZjqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n', '2013-07-08 00:59:42'),
('esvyb7gfyjgq15bbcivwsj34n5o4cbkm', 'MjQxNWM3YjE0YzQ5MDk3ZGMwODVkMjkwOTI2ZmMwMWUxOGQ2YTE4MDqAAn1xAShYCgAAAHRlc3Rjb29raWVxAlgGAAAAd29ya2VkcQNVDV9hdXRoX3VzZXJfaWSKAQFVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmR1Lg==', '2013-06-19 07:24:38'),
('f2aab5e553b8bde66482579795ae8106', 'YjkwZWI3MWQ2YmRkNTAzYzMxMTExY2E0Y2Y2ZDIwZDBmOTU5NDc2MDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n', '2013-06-18 23:49:14'),
('hs6d732lxdne70m0np2gm4k5qbafmdt7', 'MjI5ODgwYTg4YTFjYmQzNTliNzZkOGNmYTc5YzY4ODZjMGVjNzQ4ODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2013-07-03 02:38:44'),
('xrxeb5sjno2r9i1gf43mtxei8pcei7uj', 'MjI5ODgwYTg4YTFjYmQzNTliNzZkOGNmYTc5YzY4ODZjMGVjNzQ4ODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2013-06-20 00:16:12'),
('xs3c1g5dczw38isokcr6l6dktjmr8eyi', 'MjI5ODgwYTg4YTFjYmQzNTliNzZkOGNmYTc5YzY4ODZjMGVjNzQ4ODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2013-07-03 02:29:55'),
('z8iuvbds879b4gi06iln4gpwxgpi0m7v', 'MjI5ODgwYTg4YTFjYmQzNTliNzZkOGNmYTc5YzY4ODZjMGVjNzQ4ODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2013-06-25 00:12:10'),
('zvolptratevok4x66z38ilm9vmda9vse', 'MjI5ODgwYTg4YTFjYmQzNTliNzZkOGNmYTc5YzY4ODZjMGVjNzQ4ODqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2013-06-19 07:26:03');

-- --------------------------------------------------------

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `django_site`
--


-- --------------------------------------------------------

--
-- Table structure for table `doors`
--

DROP TABLE IF EXISTS `doors`;
CREATE TABLE IF NOT EXISTS `doors` (
  `door_id` int(11) NOT NULL AUTO_INCREMENT,
  `door_name` varchar(45) DEFAULT NULL,
  `door_price` varchar(45) DEFAULT NULL,
  `estimated_time` int(11) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`door_id`),
  UNIQUE KEY `door_name_UNIQUE` (`door_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `doors`
--

INSERT INTO `doors` (`door_id`, `door_name`, `door_price`, `estimated_time`, `description`) VALUES
(1, 'trestr', '34.90', 0, ''),
(2, 'trest door', '45', 3, '');

-- --------------------------------------------------------

--
-- Table structure for table `door_colors`
--

DROP TABLE IF EXISTS `door_colors`;
CREATE TABLE IF NOT EXISTS `door_colors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `door_id` int(11) NOT NULL,
  `color_code` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `door_id` (`door_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=19 ;

--
-- Dumping data for table `door_colors`
--

INSERT INTO `door_colors` (`id`, `door_id`, `color_code`) VALUES
(12, 2, 'Red'),
(13, 2, 'Green'),
(14, 2, 'White'),
(15, 2, 'Pink'),
(16, 2, 'Yellow'),
(17, 1, 'White'),
(18, 1, 'Red');

-- --------------------------------------------------------

--
-- Table structure for table `drawers`
--

DROP TABLE IF EXISTS `drawers`;
CREATE TABLE IF NOT EXISTS `drawers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `drawer_name` varchar(45) DEFAULT NULL,
  `drawer_unit_price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `drawer_name` (`drawer_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `drawers`
--

INSERT INTO `drawers` (`id`, `drawer_name`, `drawer_unit_price`) VALUES
(1, 'bifold fittings12', 12);

-- --------------------------------------------------------

--
-- Table structure for table `drawer_upgrade`
--

DROP TABLE IF EXISTS `drawer_upgrade`;
CREATE TABLE IF NOT EXISTS `drawer_upgrade` (
  `id` int(11) NOT NULL,
  `drawer_upgrade_name` varchar(45) DEFAULT NULL,
  `drawer_upgrade_unit_price` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `drawer_upgrade`
--


-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_source`
--

DROP TABLE IF EXISTS `easy_thumbnails_source`;
CREATE TABLE IF NOT EXISTS `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storage_hash` (`storage_hash`,`name`),
  KEY `easy_thumbnails_source_3f0464e5` (`storage_hash`),
  KEY `easy_thumbnails_source_4da47e07` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `easy_thumbnails_source`
--


-- --------------------------------------------------------

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

DROP TABLE IF EXISTS `easy_thumbnails_thumbnail`;
CREATE TABLE IF NOT EXISTS `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `storage_hash` varchar(40) NOT NULL,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `storage_hash` (`storage_hash`,`name`,`source_id`),
  KEY `easy_thumbnails_thumbnail_3f0464e5` (`storage_hash`),
  KEY `easy_thumbnails_thumbnail_4da47e07` (`name`),
  KEY `easy_thumbnails_thumbnail_a34b03a6` (`source_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `easy_thumbnails_thumbnail`
--


-- --------------------------------------------------------

--
-- Table structure for table `features`
--

DROP TABLE IF EXISTS `features`;
CREATE TABLE IF NOT EXISTS `features` (
  `id` int(11) NOT NULL,
  `feature_name` varchar(45) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_features_product_idx` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `features`
--


-- --------------------------------------------------------

--
-- Table structure for table `hinges`
--

DROP TABLE IF EXISTS `hinges`;
CREATE TABLE IF NOT EXISTS `hinges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `hinges_name` varchar(45) DEFAULT NULL,
  `hinges_unit_price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hinges_name` (`hinges_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `hinges`
--

INSERT INTO `hinges` (`id`, `hinges_name`, `hinges_unit_price`) VALUES
(1, 'corner hinges', 200);

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
CREATE TABLE IF NOT EXISTS `images` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `image_url` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_images_product_idx` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `images`
--


-- --------------------------------------------------------

--
-- Table structure for table `image_mapping`
--

DROP TABLE IF EXISTS `image_mapping`;
CREATE TABLE IF NOT EXISTS `image_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `image_path` varchar(245) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `image_mapping`
--

INSERT INTO `image_mapping` (`id`, `product_id`, `image_path`, `description`) VALUES
(5, 31, '/static/uploads/product/31_CAPS.jpg', 'Top Cabinet'),
(6, 31, '/static/uploads/product/31_products.jpg', 'Bottom Cabinet');

-- --------------------------------------------------------

--
-- Table structure for table `lift_options`
--

DROP TABLE IF EXISTS `lift_options`;
CREATE TABLE IF NOT EXISTS `lift_options` (
  `id` int(11) NOT NULL,
  `lift_option_name` varchar(45) DEFAULT NULL,
  `lift_option_unit_price` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lift_options`
--


-- --------------------------------------------------------

--
-- Table structure for table `materials`
--

DROP TABLE IF EXISTS `materials`;
CREATE TABLE IF NOT EXISTS `materials` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `price` float NOT NULL,
  `description` text,
  `status` set('active','inactive') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=8 ;

--
-- Dumping data for table `materials`
--

INSERT INTO `materials` (`id`, `name`, `price`, `description`, `status`) VALUES
(7, 'glass', 56, ' Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for ''lorem ipsum'' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cabinet` varchar(100) DEFAULT NULL,
  `material_id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `sub_category_id` int(11) DEFAULT NULL,
  `product_name` varchar(45) DEFAULT NULL,
  `product_code` varchar(45) DEFAULT NULL,
  `short_description` longtext,
  `descriptions` longtext,
  `product_price` float DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  `min_height` float DEFAULT NULL,
  `max_height` float DEFAULT NULL,
  `height_scale` float DEFAULT NULL,
  `min_width` float DEFAULT NULL,
  `max_width` float DEFAULT NULL,
  `width_scale` float DEFAULT NULL,
  `min_depth` float DEFAULT NULL,
  `max_depth` float DEFAULT NULL,
  `depth_scale` float DEFAULT NULL,
  `is_hinges` varchar(4) NOT NULL DEFAULT 'No',
  `image` varchar(45) DEFAULT NULL,
  `is_door` varchar(4) DEFAULT 'No',
  `is_drawer` varchar(4) NOT NULL DEFAULT 'No',
  `video_url` varchar(200) DEFAULT NULL,
  `discount` float DEFAULT '0',
  `is_custom` varchar(4) NOT NULL DEFAULT 'No' COMMENT 'Yes, No',
  PRIMARY KEY (`id`),
  KEY `fk_product_category_idx` (`category_id`),
  KEY `fk_product_sub_category_idx` (`sub_category_id`),
  KEY `fk_product_tax_idx` (`tax_id`),
  KEY `material_id` (`material_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=35 ;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `cabinet`, `material_id`, `category_id`, `sub_category_id`, `product_name`, `product_code`, `short_description`, `descriptions`, `product_price`, `tax_id`, `min_height`, `max_height`, `height_scale`, `min_width`, `max_width`, `width_scale`, `min_depth`, `max_depth`, `depth_scale`, `is_hinges`, `image`, `is_door`, `is_drawer`, `video_url`, `discount`, `is_custom`) VALUES
(31, 'Standard Base Cabinet', 7, 4, NULL, 'My First  Product', '', '', 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry''s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n', 25000, NULL, 2, 8, 2, 10, 30, 10, 40, 44, 2, 'No', NULL, 'No', 'No', 'http://www.youtube.com/watch?v=IoLBLuhnCDI', 0, 'No'),
(32, 'Standard Base Cabinet', 7, 4, NULL, 'My test Product', '', '', '', 3500, NULL, 4, 4, NULL, 6, 12, 4, 20, 20, NULL, 'No', NULL, 'No', 'No', NULL, 0, 'No'),
(34, 'Standard Base Cabinet', 7, 4, NULL, 'My rare Product', '', '', '', 2500, NULL, 20, 40, 5, 6, 12, 3, 15, 25, 4, 'No', NULL, 'No', 'No', NULL, 0, 'No');

-- --------------------------------------------------------

--
-- Table structure for table `product_cabinet_construction`
--

DROP TABLE IF EXISTS `product_cabinet_construction`;
CREATE TABLE IF NOT EXISTS `product_cabinet_construction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `cabinet_construction_id` int(11) DEFAULT NULL,
  `size` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_cabinet_construction_1_idx` (`product_id`),
  KEY `fk_product_cabinet_construction_cabinet_id_idx` (`cabinet_construction_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `product_cabinet_construction`
--


-- --------------------------------------------------------

--
-- Table structure for table `product_doors`
--

DROP TABLE IF EXISTS `product_doors`;
CREATE TABLE IF NOT EXISTS `product_doors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `door_id` int(11) DEFAULT NULL,
  `pieces_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_doors_1_idx` (`product_id`),
  KEY `fk_product_doors_2_idx` (`door_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `product_doors`
--


-- --------------------------------------------------------

--
-- Table structure for table `product_drawers`
--

DROP TABLE IF EXISTS `product_drawers`;
CREATE TABLE IF NOT EXISTS `product_drawers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `drawer_id` int(11) DEFAULT NULL,
  `product_drawers_quantity` int(11) DEFAULT NULL,
  `product_drawer_total_price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_drawers_product_idx` (`product_id`),
  KEY `fk_product_drawers_drawer_idx` (`drawer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `product_drawers`
--


-- --------------------------------------------------------

--
-- Table structure for table `product_drawer_upgrade`
--

DROP TABLE IF EXISTS `product_drawer_upgrade`;
CREATE TABLE IF NOT EXISTS `product_drawer_upgrade` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `drawer_upgrade_id` int(11) DEFAULT NULL,
  `product_drawer_upgrade_quantity` int(11) DEFAULT NULL,
  `product_drawer_upgrade_total_price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_drawer_upgrade_product_idx` (`product_id`),
  KEY `fk_product_drawer_upgrade_1_idx` (`drawer_upgrade_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_drawer_upgrade`
--


-- --------------------------------------------------------

--
-- Table structure for table `product_hinges`
--

DROP TABLE IF EXISTS `product_hinges`;
CREATE TABLE IF NOT EXISTS `product_hinges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `hinges_id` int(11) DEFAULT NULL,
  `hinges_min` int(11) DEFAULT NULL,
  `hinges_max` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_hinges_hinges_idx` (`hinges_id`),
  KEY `fk_product_hinges_product_idx` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `product_hinges`
--


-- --------------------------------------------------------

--
-- Table structure for table `product_lift_options`
--

DROP TABLE IF EXISTS `product_lift_options`;
CREATE TABLE IF NOT EXISTS `product_lift_options` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `lift_option_id` int(11) DEFAULT NULL,
  `product_lift_option_quantity` float DEFAULT NULL,
  `product_lift_option_total_price` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_lift_options_product_idx` (`product_id`),
  KEY `fk_product_lift_options_lift_options_idx` (`lift_option_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_lift_options`
--


-- --------------------------------------------------------

--
-- Table structure for table `product_shipping`
--

DROP TABLE IF EXISTS `product_shipping`;
CREATE TABLE IF NOT EXISTS `product_shipping` (
  `id` int(11) NOT NULL,
  `product_id` int(11) DEFAULT NULL,
  `carrier_id` int(11) DEFAULT NULL,
  `product_shipping_width` float DEFAULT NULL,
  `product_shipping_height` float DEFAULT NULL,
  `product_shipping_weight` float DEFAULT NULL,
  `product_shipping_depth` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_product_shipping_product_idx` (`product_id`),
  KEY `fk_product_shipping_carrier_idx` (`carrier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_shipping`
--


-- --------------------------------------------------------

--
-- Table structure for table `shoping_cart`
--

DROP TABLE IF EXISTS `shoping_cart`;
CREATE TABLE IF NOT EXISTS `shoping_cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `shoping_cart`
--

INSERT INTO `shoping_cart` (`id`, `user_id`, `product_id`) VALUES
(1, 3, 31),
(2, 3, 31),
(3, 3, 31),
(4, 3, 31),
(5, 3, 34),
(6, 14, 31),
(7, 14, 31),
(8, 14, 31),
(9, 14, 31),
(10, 14, 31),
(11, 3, 31);

-- --------------------------------------------------------

--
-- Table structure for table `sub_category`
--

DROP TABLE IF EXISTS `sub_category`;
CREATE TABLE IF NOT EXISTS `sub_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `sub_category_name` varchar(45) DEFAULT NULL,
  `sub_category_status` set('active','inactive') DEFAULT 'inactive',
  PRIMARY KEY (`id`),
  KEY `fk_sub_category_code_status_idx` (`category_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

--
-- Dumping data for table `sub_category`
--


-- --------------------------------------------------------

--
-- Table structure for table `tax`
--

DROP TABLE IF EXISTS `tax`;
CREATE TABLE IF NOT EXISTS `tax` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tax_name` varchar(45) DEFAULT NULL,
  `tax_date` date DEFAULT NULL,
  `tax_status` set('active','inactive') DEFAULT 'inactive',
  `tax_rate` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tax_name` (`tax_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `tax`
--

INSERT INTO `tax` (`id`, `tax_name`, `tax_date`, `tax_status`, `tax_rate`) VALUES
(1, 'vat', '2013-06-18', 'inactive', 12.5),
(2, 'Professional Tax', '2013-06-18', 'active', 12.5),
(3, 'Sales Tax', '2013-06-18', 'inactive', 8);

-- --------------------------------------------------------

--
-- Table structure for table `tax_mapping`
--

DROP TABLE IF EXISTS `tax_mapping`;
CREATE TABLE IF NOT EXISTS `tax_mapping` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) NOT NULL,
  `tax_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_id` (`product_id`),
  KEY `tax_id` (`tax_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=75 ;

--
-- Dumping data for table `tax_mapping`
--

INSERT INTO `tax_mapping` (`id`, `product_id`, `tax_id`) VALUES
(70, 32, 1),
(71, 32, 2),
(72, 31, 1),
(73, 31, 2),
(74, 34, 2);

-- --------------------------------------------------------

--
-- Table structure for table `tax_rules`
--

DROP TABLE IF EXISTS `tax_rules`;
CREATE TABLE IF NOT EXISTS `tax_rules` (
  `id` int(11) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  `tax_id` int(11) DEFAULT NULL,
  `tax_rule_status` set('active','inactive') DEFAULT 'inactive',
  PRIMARY KEY (`id`),
  KEY `fk_tax_rules_category_idx` (`category_id`),
  KEY `fk_tax_rules_tax_idx` (`tax_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tax_rules`
--


--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_message`
--
ALTER TABLE `auth_message`
  ADD CONSTRAINT `user_id_refs_id_9af0b65a` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `carriers`
--
ALTER TABLE `carriers`
  ADD CONSTRAINT `fk_carriers_tax` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `door_colors`
--
ALTER TABLE `door_colors`
  ADD CONSTRAINT `door_colors_ibfk_1` FOREIGN KEY (`door_id`) REFERENCES `doors` (`door_id`);

--
-- Constraints for table `features`
--
ALTER TABLE `features`
  ADD CONSTRAINT `fk_features_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `images`
--
ALTER TABLE `images`
  ADD CONSTRAINT `fk_images_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `image_mapping`
--
ALTER TABLE `image_mapping`
  ADD CONSTRAINT `image_mapping_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `product`
--
ALTER TABLE `product`
  ADD CONSTRAINT `fk_product_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_sub_category` FOREIGN KEY (`sub_category_id`) REFERENCES `sub_category` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_tax` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `product_ibfk_1` FOREIGN KEY (`material_id`) REFERENCES `materials` (`id`);

--
-- Constraints for table `product_cabinet_construction`
--
ALTER TABLE `product_cabinet_construction`
  ADD CONSTRAINT `fk_product_cabinet_construction_cabinet_id` FOREIGN KEY (`cabinet_construction_id`) REFERENCES `cabinet` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_cabinet_construction_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product_doors`
--
ALTER TABLE `product_doors`
  ADD CONSTRAINT `fk_product_doors_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_doors_2` FOREIGN KEY (`door_id`) REFERENCES `doors` (`door_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product_drawers`
--
ALTER TABLE `product_drawers`
  ADD CONSTRAINT `fk_product_drawers_drawer` FOREIGN KEY (`drawer_id`) REFERENCES `drawers` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_drawers_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product_drawer_upgrade`
--
ALTER TABLE `product_drawer_upgrade`
  ADD CONSTRAINT `fk_product_drawer_upgrade_drawer_upgrade` FOREIGN KEY (`drawer_upgrade_id`) REFERENCES `drawer_upgrade` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_drawer_upgrade_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product_hinges`
--
ALTER TABLE `product_hinges`
  ADD CONSTRAINT `fk_product_hinges_hinges` FOREIGN KEY (`hinges_id`) REFERENCES `hinges` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_hinges_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product_lift_options`
--
ALTER TABLE `product_lift_options`
  ADD CONSTRAINT `fk_product_lift_options_lift_options` FOREIGN KEY (`lift_option_id`) REFERENCES `lift_options` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_lift_options_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `product_shipping`
--
ALTER TABLE `product_shipping`
  ADD CONSTRAINT `fk_product_shipping_carrier` FOREIGN KEY (`carrier_id`) REFERENCES `carriers` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_product_shipping_product` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `shoping_cart`
--
ALTER TABLE `shoping_cart`
  ADD CONSTRAINT `shoping_cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `shoping_cart_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sub_category`
--
ALTER TABLE `sub_category`
  ADD CONSTRAINT `fk_sub_category_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `tax_mapping`
--
ALTER TABLE `tax_mapping`
  ADD CONSTRAINT `tax_mapping_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`),
  ADD CONSTRAINT `tax_mapping_ibfk_2` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`);

--
-- Constraints for table `tax_rules`
--
ALTER TABLE `tax_rules`
  ADD CONSTRAINT `fk_tax_rules_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_tax_rules_tax` FOREIGN KEY (`tax_id`) REFERENCES `tax` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
