-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: registro
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
-- Table structure for table `geocerca`
--

DROP TABLE IF EXISTS `geocerca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `geocerca` (
  `id` int NOT NULL,
  `Veiculo` varchar(45) NOT NULL,
  `Rastra` varchar(45) NOT NULL,
  `Geocerca` varchar(45) NOT NULL,
  `Fecha_Entrada` date NOT NULL,
  `Fecha_Salida` date NOT NULL,
  `Dif_Tiempo` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `geocerca`
--

LOCK TABLES `geocerca` WRITE;
/*!40000 ALTER TABLE `geocerca` DISABLE KEYS */;
/*!40000 ALTER TABLE `geocerca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guardar`
--

DROP TABLE IF EXISTS `guardar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `guardar` (
  `idguardar` int NOT NULL,
  `idveiculo` int NOT NULL,
  `idrastra` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `idgeocerca` int NOT NULL,
  `fecha_entrada` date NOT NULL,
  `fecha_salida` date NOT NULL,
  `dif_tiempo` time NOT NULL,
  PRIMARY KEY (`idguardar`),
  KEY `fk_guardar_veiculo_id_idx` (`idveiculo`),
  KEY `fk_guardar_rastra_id_idx` (`idrastra`),
  KEY `fk_guardar_geocerca_id_idx` (`idgeocerca`),
  CONSTRAINT `fk_guardar_geocerca_id` FOREIGN KEY (`idgeocerca`) REFERENCES `geocerca` (`id`),
  CONSTRAINT `fk_guardar_rastra_id` FOREIGN KEY (`idrastra`) REFERENCES `rastra` (`idrastra`),
  CONSTRAINT `fk_guardar_veiculo_id` FOREIGN KEY (`idveiculo`) REFERENCES `veiculo` (`idveiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guardar`
--

LOCK TABLES `guardar` WRITE;
/*!40000 ALTER TABLE `guardar` DISABLE KEYS */;
/*!40000 ALTER TABLE `guardar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rastra`
--

DROP TABLE IF EXISTS `rastra`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rastra` (
  `idrastra` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idrastra`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rastra`
--

LOCK TABLES `rastra` WRITE;
/*!40000 ALTER TABLE `rastra` DISABLE KEYS */;
/*!40000 ALTER TABLE `rastra` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veiculo`
--

DROP TABLE IF EXISTS `veiculo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veiculo` (
  `idveiculo` int NOT NULL,
  `nombre` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idveiculo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veiculo`
--

LOCK TABLES `veiculo` WRITE;
/*!40000 ALTER TABLE `veiculo` DISABLE KEYS */;
/*!40000 ALTER TABLE `veiculo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-13 14:17:32
