-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.24

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
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2021-04-28 10:44:14.984083'),(2,'auth','0001_initial','2021-04-28 10:44:15.627128'),(3,'admin','0001_initial','2021-04-28 10:44:15.779141'),(4,'admin','0002_logentry_remove_auto_add','2021-04-28 10:44:15.791141'),(5,'admin','0003_logentry_add_action_flag_choices','2021-04-28 10:44:15.803142'),(6,'contenttypes','0002_remove_content_type_name','2021-04-28 10:44:15.927155'),(7,'auth','0002_alter_permission_name_max_length','2021-04-28 10:44:15.999159'),(8,'auth','0003_alter_user_email_max_length','2021-04-28 10:44:16.032160'),(9,'auth','0004_alter_user_username_opts','2021-04-28 10:44:16.045162'),(10,'auth','0005_alter_user_last_login_null','2021-04-28 10:44:16.112166'),(11,'auth','0006_require_contenttypes_0002','2021-04-28 10:44:16.116166'),(12,'auth','0007_alter_validators_add_error_messages','2021-04-28 10:44:16.128167'),(13,'auth','0008_alter_user_username_max_length','2021-04-28 10:44:16.202172'),(14,'auth','0009_alter_user_last_name_max_length','2021-04-28 10:44:16.272178'),(15,'auth','0010_alter_group_name_max_length','2021-04-28 10:44:16.300183'),(16,'auth','0011_update_proxy_permissions','2021-04-28 10:44:16.316180'),(17,'auth','0012_alter_user_first_name_max_length','2021-04-28 10:44:16.387188'),(18,'sessions','0001_initial','2021-04-28 10:44:16.443191'),(19,'shoppingApp','0001_initial','2021-04-28 10:44:16.479194'),(20,'shoppingApp','0002_useraccounts_user_name','2021-04-28 10:44:16.509198'),(21,'shoppingApp','0003_event_notice','2021-05-01 14:57:18.144339'),(22,'shoppingApp','0004_auto_20210504_0159','2021-05-04 01:59:13.738514'),(23,'shoppingApp','0005_alter_useraccounts_user_address','2021-05-05 06:43:41.230104'),(24,'products','0001_initial','2021-05-10 15:49:56.503996'),(25,'shoppingApp','0006_iteminfo','2021-05-10 16:24:18.214519'),(26,'shoppingApp','0007_auto_20210512_0348','2021-05-11 18:49:08.097768'),(27,'productApp','0001_initial','2021-05-12 15:11:47.629807'),(28,'shoppingApp','0008_delete_product','2021-05-12 15:11:47.679813');
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

-- Dump completed on 2021-05-13  3:20:10
