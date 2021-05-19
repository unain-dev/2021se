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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2021-05-06 12:04:40.962485','4','daeun2',3,'',4,2),(2,'2021-05-06 12:04:40.963865','10','test123',3,'',4,2),(3,'2021-05-06 12:04:40.964763','11','test123412',3,'',4,2),(4,'2021-05-06 12:04:40.965709','9','test5',3,'',4,2),(5,'2021-05-06 12:04:40.966540','3','testuser',3,'',4,2),(6,'2021-05-06 12:04:40.967123','5','testuser2',3,'',4,2),(7,'2021-05-06 12:04:40.967694','6','testuser3',3,'',4,2),(8,'2021-05-06 12:04:40.968245','8','testuser4',3,'',4,2),(9,'2021-05-06 12:04:48.965094','4','UserAccounts object (4)',3,'',7,2),(10,'2021-05-06 12:04:48.966105','3','UserAccounts object (3)',3,'',7,2),(11,'2021-05-06 12:04:48.966789','2','UserAccounts object (2)',3,'',7,2),(12,'2021-05-06 12:04:48.967358','1','UserAccounts object (1)',3,'',7,2),(13,'2021-05-12 15:18:18.851043','1','product object (1)',1,'[{\"added\": {}}]',13,20),(14,'2021-05-12 17:36:27.541457','1','product object (1)',2,'[]',13,20),(15,'2021-05-13 01:27:23.795832','1','Notice object (1)',1,'[{\"added\": {}}]',15,2),(16,'2021-05-13 01:28:07.363430','1','Event object (1)',1,'[{\"added\": {}}]',14,2),(17,'2021-05-13 01:31:31.004163','1','Event object (1)',2,'[{\"changed\": {\"fields\": [\"On off\"]}}]',14,2),(18,'2021-05-13 02:32:41.744267','1','product object (1)',2,'[{\"changed\": {\"fields\": [\"Price range\"]}}]',13,2),(19,'2021-05-13 03:54:23.284284','1','product object (1)',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',13,2),(20,'2021-05-13 05:16:26.631894','1','product object (1)',2,'[{\"changed\": {\"fields\": [\"Category\"]}}]',13,2),(21,'2021-05-14 11:00:20.404471','5','product object (5)',1,'[{\"added\": {}}]',13,2),(22,'2021-05-14 12:03:20.799469','1','product object (1)',2,'[{\"changed\": {\"fields\": [\"PubDate\"]}}]',13,2),(23,'2021-05-14 12:03:31.163596','3','product object (3)',2,'[{\"changed\": {\"fields\": [\"Product id\", \"PubDate\"]}}]',13,2),(24,'2021-05-14 12:03:45.072521','4','product object (4)',2,'[{\"changed\": {\"fields\": [\"Product id\", \"PubDate\"]}}]',13,2),(25,'2021-05-14 12:03:52.603362','5','product object (5)',2,'[{\"changed\": {\"fields\": [\"PubDate\"]}}]',13,2),(26,'2021-05-16 07:11:54.289172','1','Notice_Event object (1)',1,'[{\"added\": {}}]',16,2),(27,'2021-05-16 07:22:12.608506','1','Notice_Event object (1)',2,'[{\"changed\": {\"fields\": [\"Images\"]}}]',16,2),(28,'2021-05-16 08:23:46.997298','2','Notice_Event object (2)',1,'[{\"added\": {}}]',16,2),(29,'2021-05-16 08:33:45.075831','1','Notice_Event object (1)',3,'',16,2),(30,'2021-05-16 09:01:50.663785','3','Notice_Event object (3)',1,'[{\"added\": {}}]',16,2),(31,'2021-05-16 09:24:25.218133','4','Notice_Event object (4)',1,'[{\"added\": {}}]',16,2),(32,'2021-05-17 04:23:03.132711','6','product object (6)',1,'[{\"added\": {}}]',13,20),(33,'2021-05-17 04:58:19.127979','6','product object (6)',3,'',13,20),(34,'2021-05-17 04:58:19.133978','5','product object (5)',3,'',13,20),(35,'2021-05-17 04:58:19.136982','4','product object (4)',3,'',13,20),(36,'2021-05-17 04:58:19.139979','3','product object (3)',3,'',13,20),(37,'2021-05-17 04:58:19.144981','1','product object (1)',3,'',13,20),(38,'2021-05-17 04:58:51.017484','7','product object (7)',1,'[{\"added\": {}}]',13,20),(39,'2021-05-17 05:05:04.831305','8','product object (8)',1,'[{\"added\": {}}]',13,20),(40,'2021-05-17 05:05:46.094711','9','product object (9)',1,'[{\"added\": {}}]',13,20),(41,'2021-05-18 07:22:51.216983','3','product object (3)',3,'',13,20),(42,'2021-05-18 07:22:51.219962','2','product object (2)',3,'',13,20),(43,'2021-05-18 07:22:51.222926','1','product object (1)',3,'',13,20),(44,'2021-05-18 07:23:29.655550','1','product object (1)',1,'[{\"added\": {}}]',13,20),(45,'2021-05-18 07:24:11.975655','2','product object (2)',1,'[{\"added\": {}}]',13,20),(46,'2021-05-18 07:28:14.127390','3','product object (3)',1,'[{\"added\": {}}]',13,20),(47,'2021-05-18 07:33:36.767606','3','product object (3)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',13,20),(48,'2021-05-18 07:33:53.139696','3','product object (3)',3,'',13,20),(49,'2021-05-18 07:34:26.821431','2','product object (2)',2,'[{\"changed\": {\"fields\": [\"Image\"]}}]',13,20),(50,'2021-05-18 15:54:37.547528','3','product object (3)',1,'[{\"added\": {}}]',13,20),(51,'2021-05-18 15:55:24.102172','4','product object (4)',1,'[{\"added\": {}}]',13,20),(52,'2021-05-18 15:57:59.355742','3','product object (3)',2,'[]',13,20),(53,'2021-05-18 15:58:19.901862','4','product object (4)',2,'[]',13,20),(54,'2021-05-19 07:49:54.610349','4','product object (4)',2,'[{\"added\": {\"name\": \"photo\", \"object\": \"Photo object (1)\"}}, {\"added\": {\"name\": \"photo\", \"object\": \"Photo object (2)\"}}, {\"added\": {\"name\": \"photo\", \"object\": \"Photo object (3)\"}}]',13,20),(55,'2021-05-19 07:52:27.888256','4','product object (4)',2,'[]',13,20),(56,'2021-05-19 07:58:50.342892','4','product object (4)',2,'[]',13,20),(57,'2021-05-19 13:09:11.843503','14','UserAccounts object (14)',2,'[{\"added\": {\"name\": \"address\", \"object\": \"address object (1)\"}}, {\"added\": {\"name\": \"address\", \"object\": \"address object (2)\"}}]',7,20),(58,'2021-05-19 13:22:27.778302','14','UserAccounts object (14)',2,'[]',7,20);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-20  1:06:20
