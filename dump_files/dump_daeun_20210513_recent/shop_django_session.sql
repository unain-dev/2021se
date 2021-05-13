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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0my4lhpbvg91fzo72nno71pxt2y1rryl','e30:1lgMPT:VOSqZmOe_yKloD8szinBIiSNpMvWVRwSt9LOMPo16LI','2021-05-25 07:02:27.672099'),('32x45468g5bwybin3t40djlglznfrp3m','e30:1lgMYN:qMtjLhd8n_1gfI-gbI9aestTy5wwkyYoIihnzY3qJ4w','2021-05-25 07:11:39.629243'),('6vef2k8jigr92lo8p1afs8k6w9bpdsy9','e30:1lgMP4:KdMgbMr82SmOwwMPgKcPbkNRLKUSQYztph4JfqUko-I','2021-05-25 07:02:02.938266'),('c7grhqz4jo5lpa06ww7h5fet9mg94lkk','.eJxVjDsOwjAQRO_iGln-bgwlPWeI1rtrHECOlE-FuDuJlAKmGs2bmbfqcV1qv84y9QOri3Lq9JtlpKe0HfAD233UNLZlGrLeK_qgs76NLK_r0f07qDjXbZ0sEAqfpViKnlwkKn4zHCFBiUmg67wzJnM2LMGiKQEC2pTB203q8wX3hDfA:1lgzdE:3ijWrrMBTtd8Rzo42XQj3D02cjG0LaXgvynCGxt9KE0','2021-05-27 00:55:16.828300'),('funczzmk9doinkzn7l75yf9w8rexpbo4','e30:1ledjQ:-U7s6DPgWOf7Ftczq4dNJZQ-x6W2WXmMo9jxYXemrqQ','2021-05-20 13:07:56.881879'),('izm2kklwgexguuis81clmrk1n8fg26ei','e30:1ledRL:-rjRTJKAN8YJ2RA1Z6zewUatsWBj4RTanzGxapK-yq0','2021-05-20 12:49:15.663043'),('jovklh0d1wmxtjykneaasnbl4z82q7r8','.eJxVjDsOwjAQRO_iGln-bgwlPWeI1rtrHECOlE-FuDuJlAKmGs2bmbfqcV1qv84y9QOri3Lq9JtlpKe0HfAD233UNLZlGrLeK_qgs76NLK_r0f07qDjXbZ0sEAqfpViKnlwkKn4zHCFBiUmg67wzJnM2LMGiKQEC2pTB203q8wX3hDfA:1lh0jj:fS2NgZcbQx1x130roOnkwZhQDsr5rA9XxaHGkvgd75U','2021-05-27 02:06:03.306598'),('pwyxn145wy9ohl44suv6t761m1al38k5','e30:1lgMLp:Ah6gQ2ys9vmKJFHC8XT9FFubgN5CoOvVDobPE5dEgdg','2021-05-25 06:58:41.821337'),('r8bibkdjz9fnq1y7wvoaj63p7o9em0jm','e30:1ledjx:GA7bCsz71uJ3RxFJjiwd_Gcy3pfJ1g97-1SifG0QmSw','2021-05-20 13:08:29.705677'),('w05661iuqvv1cs6sj77hmccu7lna97yt','.eJxVjMEOwiAQRP-FsyFCgUWP3vsNZGEXqRqalPZk_Hdp0oPeJm_ezFsE3NYStsZLmEhchRKnXxYxPbnuBT2w3meZ5rouU5S7Io-2yXEmft0O9--gYCt97YEdgcqGrE4ZlR6SM-CBgAnRO20vypwH63rKAGitRxUTdsLZGi8-X9YoN1g:1lcrHU:LarOgRDgzFaPqOwwXlDow9OApBwgc9sZo2CVgg9Os_k','2021-05-15 15:11:44.044425');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13 12:14:26
