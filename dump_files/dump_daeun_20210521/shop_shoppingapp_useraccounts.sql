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
-- Table structure for table `shoppingapp_useraccounts`
--

DROP TABLE IF EXISTS `shoppingapp_useraccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoppingapp_useraccounts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_pw` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `user_phone` int DEFAULT NULL,
  `user_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingapp_useraccounts`
--

LOCK TABLES `shoppingapp_useraccounts` WRITE;
/*!40000 ALTER TABLE `shoppingapp_useraccounts` DISABLE KEYS */;
INSERT INTO `shoppingapp_useraccounts` VALUES (5,'testuser','testuser123*','test','test@test.com',1012341234,'testuser'),(6,'testuser1','1234','test','test@test.com',1012341234,'testuser'),(7,'dsfaf','safsdaf','safsa','sdafsa@jdlafjls.dofjsal',2414241,'dsadsf'),(8,'testte','dkalfj','dkslafjlk','jdsalkf@jdlkfjal.cojdl',11,'kldsjafklj'),(9,'DSAF','ASDFA','DSFA','',23424,''),(10,'testtete','testtete*','dfjaksflj','dkasfj@jldafjl.cjdlfkajs',234142314,'testtete'),(11,'testtetete','tetete1234*','kjdakflj','dsaklf@jfdsklafjsla',24153241,'jdkafj'),(12,'testuser2','test2222*','testuser2','testuser2@testuser2.test',1234,'testuser2'),(13,'jiyeon1','!ska35785','동일로 22길 마들대림아파트5-1504','jiyeon143@naver.com',29381317,'남지연'),(14,'hyein','!asdf35785!','동일로 22길 마들대림아파트5-1504','asdfaasdfsdf@naver.com',29381317,'김혜인'),(15,'ddddaaaa','ddddaaaa*','ddddaaaa','ddd@ddd.ddd',231414234,'ddddaaaa');
/*!40000 ALTER TABLE `shoppingapp_useraccounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-21  1:56:24
