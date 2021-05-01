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
-- Table structure for table `shoppingApp_useraccounts`
--

DROP TABLE IF EXISTS `shoppingApp_useraccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shoppingApp_useraccounts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `user_pw` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `user_address` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `user_email` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `user_phone` int DEFAULT NULL,
  `user_name` varchar(20) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shoppingApp_useraccounts`
--

LOCK TABLES `shoppingApp_useraccounts` WRITE;
/*!40000 ALTER TABLE `shoppingApp_useraccounts` DISABLE KEYS */;
INSERT INTO `shoppingApp_useraccounts` VALUES (1,'test1','1234','aaa','aaa',123,'1'),(2,'daffy','asfdsa','asfdsa','deaf',14321,'1'),(3,'dd','adfaf','dsfafsa','dsfafas',2341,'1'),(4,'dd','adfaf','dsfafsa','dsfafas',2341,'1'),(5,'as','asdfas','asfsad','sadfsa',324,'1'),(6,'hi','hi','dks','dsfa',1324,'1'),(7,'user1','dfafas','dasfsfd','dsafaf',3422,'1'),(8,'test4','afsf','dsafs','asfas',3412,'1'),(9,'fajsl','kafjklfj','aksjdfkajk','adkfaj@adfjalfj',23424,'akfjsdklajf'),(10,'dafjl','dakfjslk','dkasjflksa','dasklfjl@dkasjflkdsf',23194810,'jdakfjslk'),(11,'skdjfak','safsdflk','sdfakjfl','sjkfj@jsdjflasf',23414,'sdfkak'),(12,'dd','sfsaf','sdafsa','dsfasad@jdkljsfkl',241,'asdfasd'),(13,'ddsaf','sdfsf','sdafsa','dsfasad@jdkljsfkl',241,'asdfasd');
/*!40000 ALTER TABLE `shoppingApp_useraccounts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-01 15:14:54
