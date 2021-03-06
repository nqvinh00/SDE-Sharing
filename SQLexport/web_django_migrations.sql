-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: web
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-03-25 03:22:33.930041'),(2,'auth','0001_initial','2020-03-25 03:22:34.222893'),(3,'admin','0001_initial','2020-03-25 03:22:35.137701'),(4,'admin','0002_logentry_remove_auto_add','2020-03-25 03:22:35.360080'),(5,'admin','0003_logentry_add_action_flag_choices','2020-03-25 03:22:35.382229'),(6,'contenttypes','0002_remove_content_type_name','2020-03-25 03:22:35.575837'),(7,'auth','0002_alter_permission_name_max_length','2020-03-25 03:22:35.704642'),(8,'auth','0003_alter_user_email_max_length','2020-03-25 03:22:35.835779'),(9,'auth','0004_alter_user_username_opts','2020-03-25 03:22:35.851127'),(10,'auth','0005_alter_user_last_login_null','2020-03-25 03:22:35.938231'),(11,'auth','0006_require_contenttypes_0002','2020-03-25 03:22:35.943246'),(12,'auth','0007_alter_validators_add_error_messages','2020-03-25 03:22:35.957196'),(13,'auth','0008_alter_user_username_max_length','2020-03-25 03:22:36.125207'),(14,'auth','0009_alter_user_last_name_max_length','2020-03-25 03:22:36.232343'),(15,'auth','0010_alter_group_name_max_length','2020-03-25 03:22:36.359461'),(16,'auth','0011_update_proxy_permissions','2020-03-25 03:22:36.375328'),(17,'sessions','0001_initial','2020-03-25 03:22:36.426025'),(18,'background_task','0001_initial','2020-03-26 08:59:15.624488'),(19,'background_task','0002_auto_20170927_1109','2020-03-26 08:59:16.286962'),(20,'post','0001_initial','2020-03-26 17:11:09.008584'),(21,'post','0002_slides','2020-03-26 17:38:34.891347'),(22,'post','0003_auto_20200403_1443','2020-04-03 07:43:44.084618'),(23,'post','0004_auto_20200412_1334','2020-04-12 06:36:36.659282'),(24,'post','0005_uploaddocuments_name','2020-04-12 07:00:50.187967'),(25,'post','0006_uploadexams','2020-04-12 18:50:12.561306'),(26,'post','0007_auto_20200413_2304','2020-04-13 16:04:59.232061'),(27,'post','0008_uploadslides','2020-04-15 04:29:30.143750');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-17 20:44:52
