-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: remotemysql.com    Database: qZAqwXH0Wi
-- ------------------------------------------------------
-- Server version	8.0.13-4

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
-- Table structure for table `tb_cliente`
--

DROP TABLE IF EXISTS `tb_cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_cliente` (
  `idt_cliente` int(11) NOT NULL AUTO_INCREMENT,
  `nme_cliente` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `endereco_cliente` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `qtd_token` int(11) DEFAULT NULL,
  `numero_cliente` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `CPF` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`idt_cliente`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_cliente`
--

LOCK TABLES `tb_cliente` WRITE;
/*!40000 ALTER TABLE `tb_cliente` DISABLE KEYS */;
INSERT INTO `tb_cliente` VALUES (1,'André Victor Geronimo Gonçalves','SQN 215 BL B',0,'982830376','3554359181'),(2,'André Victor Geronimo Gonçalves','SQN 215 BL B',0,'982830376','03554359181');
/*!40000 ALTER TABLE `tb_cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_funcionario`
--

DROP TABLE IF EXISTS `tb_funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_funcionario` (
  `idt_funcionario` int(11) NOT NULL AUTO_INCREMENT,
  `nme_funcionario` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `qtd_venda` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`idt_funcionario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_funcionario`
--

LOCK TABLES `tb_funcionario` WRITE;
/*!40000 ALTER TABLE `tb_funcionario` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_funcionario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_pedido`
--

DROP TABLE IF EXISTS `tb_pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_pedido` (
  `idt_pedido` int(11) NOT NULL AUTO_INCREMENT,
  `cod_produto` int(11) NOT NULL,
  `cod_funcionario` int(11) NOT NULL,
  `cod_cliente` int(11) NOT NULL,
  `DataHora` datetime NOT NULL,
  `vlr_total` decimal(8,2) NOT NULL,
  `vlr_total_token` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`idt_pedido`),
  KEY `fk_tb_pedido_tb_produto` (`cod_produto`),
  KEY `fk_tb_pedido_tb_funcionario1` (`cod_funcionario`),
  KEY `fk_tb_pedido_tb_cliente1` (`cod_cliente`),
  CONSTRAINT `fk_tb_pedido_tb_cliente1` FOREIGN KEY (`cod_cliente`) REFERENCES `tb_cliente` (`idt_cliente`),
  CONSTRAINT `fk_tb_pedido_tb_funcionario1` FOREIGN KEY (`cod_funcionario`) REFERENCES `tb_funcionario` (`idt_funcionario`),
  CONSTRAINT `fk_tb_pedido_tb_produto` FOREIGN KEY (`cod_produto`) REFERENCES `tb_produto` (`idt_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_pedido`
--

LOCK TABLES `tb_pedido` WRITE;
/*!40000 ALTER TABLE `tb_pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_produto`
--

DROP TABLE IF EXISTS `tb_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_produto` (
  `idt_produto` int(11) NOT NULL AUTO_INCREMENT,
  `nme_produto` varchar(45) COLLATE utf8_unicode_ci NOT NULL,
  `vlr_produto` decimal(8,2) DEFAULT NULL,
  `vlr_produto_token` int(11) NOT NULL,
  PRIMARY KEY (`idt_produto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_produto`
--

LOCK TABLES `tb_produto` WRITE;
/*!40000 ALTER TABLE `tb_produto` DISABLE KEYS */;
/*!40000 ALTER TABLE `tb_produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 22:58:48
