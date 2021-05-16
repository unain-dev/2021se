-- MySQL dump 10.13  Distrib 8.0.22, for macos10.15 (x86_64)
--
-- Host: 127.0.0.1    Database: shop
-- ------------------------------------------------------
-- Server version	8.0.23

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
-- Table structure for table `noticeApp_notice_event`
--

DROP TABLE IF EXISTS `noticeApp_notice_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `noticeApp_notice_event` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `noti_event_id` int NOT NULL,
  `title` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `pubdate` datetime(6) NOT NULL,
  `contents` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `on_off` tinyint(1) NOT NULL,
  `activation` varchar(10) COLLATE utf8mb4_general_ci NOT NULL,
  `dueDate` datetime(6) NOT NULL,
  `images` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticeApp_notice_event`
--

LOCK TABLES `noticeApp_notice_event` WRITE;
/*!40000 ALTER TABLE `noticeApp_notice_event` DISABLE KEYS */;
INSERT INTO `noticeApp_notice_event` VALUES (2,2,'second','2021-05-16 08:23:46.995073','second',1,'yes','2021-05-31 08:23:45.000000','notice/banner1.jpg'),(3,3,'third','2021-05-16 09:01:50.662264','third',1,'yes','2021-05-29 09:01:49.000000','notice/banner2.jpg'),(4,4,'third','2021-05-16 09:24:25.216712','third',1,'yes','2021-05-31 09:24:24.000000','notice/banner3.jpg');
/*!40000 ALTER TABLE `noticeApp_notice_event` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-16 18:29:20
