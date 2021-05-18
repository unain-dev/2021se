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
-- Table structure for table `productapp_product`
--

DROP TABLE IF EXISTS `productapp_product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productapp_product` (
  `product_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `price` int NOT NULL,
  `description` longtext NOT NULL,
  `stock` int NOT NULL,
  `salesamount` int NOT NULL,
  `status` int NOT NULL,
  `category` varchar(20) NOT NULL,
  `pubDate` datetime(6) NOT NULL,
  `published` tinyint(1) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE KEY `productApp_product_product_id_706d108d_uniq` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productapp_product`
--

LOCK TABLES `productapp_product` WRITE;
/*!40000 ALTER TABLE `productapp_product` DISABLE KEYS */;
INSERT INTO `productapp_product` VALUES (1,'레이어드링1',10000,'레이어드링',1,1,1,'rings','2021-05-18 07:22:53.000000',1,'image/r1.jpg'),(2,'레이어드링2',20000,'레이어드링2',2,2,2,'rings','2021-05-18 07:23:32.000000',1,'image/r2_Kp4Sf3a.jpg');
/*!40000 ALTER TABLE `productapp_product` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-18 16:43:13
