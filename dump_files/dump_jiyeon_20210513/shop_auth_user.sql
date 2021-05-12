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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$84TYTAX91HbnDOZCuSTbHh$GqOdnioWBg9SCAt45tNirxAow7r/MxJA5W5BL9kav6M=','2021-05-01 15:11:44.035424',1,'beyon','','','91j6j5@naver.com',1,1,'2021-05-01 15:10:18.418459'),(2,'pbkdf2_sha256$260000$Jn8idLCpnPLYxBSMmZZxd7$kQaH5/6Jeei5c6HYH53MYWqoKrH/P0rCMx8oTrxrCLc=','2021-05-11 07:16:39.887381',1,'daeun','','','daeun8436@naver.com',1,1,'2021-05-02 04:57:58.218256'),(12,'pbkdf2_sha256$260000$96Bcd9jWXumbqvQYKVVIxy$qPY0SMffLYHv//jc/SZlzD4gspl/qeZa0Fy6VRSjHks=',NULL,0,'testuser','','','test@test.com',0,1,'2021-05-06 12:05:34.356791'),(13,'pbkdf2_sha256$260000$FslNTUdkzX6vcnbwPn7NGE$srQEaj/nTsl3PC/XE2pcRCqSSUMjJ7LLkBjdxWaz4wU=','2021-05-06 13:11:30.108542',0,'testuser1','','','test@test.com',0,1,'2021-05-06 12:06:20.443024'),(14,'pbkdf2_sha256$260000$cEaB4vUVftxsaoZf98O0Gn$4ZiOgYbAR9Zpsai8WVfrL2ygwou6iSzmFNk3xOzqUW0=',NULL,0,'dsfaf','','','sdafsa@jdlafjls.dofjsal',0,1,'2021-05-06 12:07:25.114113'),(15,'pbkdf2_sha256$260000$GJYOtlYFlq2x6XoBeIcd4N$dDF0k0B7x/y9qM9ZytxYNR/5LcgsY0b0Kfv4+0MsJyM=',NULL,0,'testte','','','jdsalkf@jdlkfjal.cojdl',0,1,'2021-05-06 12:15:30.922531'),(16,'pbkdf2_sha256$260000$QcUENahcgtQ8rNhcIEfqlU$Ibgov5Ec3xLMw3cssEA3sVTQinFFPhNUXo0pdW040x0=',NULL,0,'DSAF','','','',0,1,'2021-05-06 12:21:29.856342'),(17,'pbkdf2_sha256$260000$Jb6rbH34iHbCCkgBOQfVk1$xfq9kWTxzwM6xigDmBnPzApd4m5v+2BhyTl5C5ClUXM=','2021-05-11 07:18:48.158132',0,'testtete','','','dkasfj@jldafjl.cjdlfkajs',0,1,'2021-05-06 12:59:01.134233'),(18,'pbkdf2_sha256$260000$PMWzLqITX783xMWqYElm0n$R0FkxUUohQLF7t8HptwrzZXQ8KtT6VgVZMv49hWFeSk=',NULL,0,'testtetete','','','dsaklf@jfdsklafjsla',0,1,'2021-05-06 12:59:52.895310'),(19,'pbkdf2_sha256$260000$wSsUI48xqkYwNE4PibGUuP$vC3hEG82Q4S8FCZQXEJ09UD+8Vk2d0NK1ra3KdpKyCk=','2021-05-11 07:19:27.007970',0,'testuser2','','','testuser2@testuser2.test',0,1,'2021-05-06 13:22:09.719283'),(20,'pbkdf2_sha256$260000$sLcheuzZwP01k5WHHMQONT$OuM9MNtPt62JzV5Os4lAVzvjascDE96ozn7CoWZ/Zvw=','2021-05-12 17:36:20.135114',1,'jiyeon','','','jiyeon143@naver.com',1,1,'2021-05-12 14:54:33.164054');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13  3:20:18
