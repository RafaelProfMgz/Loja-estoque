-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: trabalhopoo
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `IdCliente` int NOT NULL AUTO_INCREMENT,
  `NomCliente` varchar(100) NOT NULL,
  `Cpf` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Telefone` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Idade` int NOT NULL,
  `Endereco` varchar(100) NOT NULL,
  PRIMARY KEY (`IdCliente`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'maria Joaquina','66 9999 51035','061223845812',25,'Rua Vitorioa, N524'),(2,'João Feijão','6666 6666','78787878787878',25,'rua carla, N245'),(3,'Marcos Evagelo','123 123 123','12356489',84,'Rua Joara, N 15'),(5,'Marica Carla','6699999999','061255948',24,'rua 23, morand');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estoque`
--

DROP TABLE IF EXISTS `estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estoque` (
  `IdProduto` int NOT NULL AUTO_INCREMENT,
  `nomeProduto` varchar(100) NOT NULL,
  `quantidade` int NOT NULL,
  `valorCompra` float NOT NULL,
  `valorVenda` float NOT NULL,
  `ValorCompraIndividual` float NOT NULL,
  `valorVendaIndividual` float NOT NULL,
  PRIMARY KEY (`IdProduto`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estoque`
--

LOCK TABLES `estoque` WRITE;
/*!40000 ALTER TABLE `estoque` DISABLE KEYS */;
INSERT INTO `estoque` VALUES (1,'porca 64',12,840,1000,35,41.6667),(2,'vela de carro',5,250,300,125,150),(3,'teste',2,23,53,11.5,26.5),(4,'Martelo',2,120,320,60,160),(5,'Martelo rosado',4,120,320,30,80),(6,'MAcaco Prego',4,250,325,62.5,81.25),(7,'Roda dentada',4,250,325,62.5,81.25),(8,'Roda dentada 45',4,250,325,62.5,81.25);
/*!40000 ALTER TABLE `estoque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `produtos_vendidos`
--

DROP TABLE IF EXISTS `produtos_vendidos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `produtos_vendidos` (
  `Idprodutos_vendidos` int NOT NULL AUTO_INCREMENT,
  `IdProduto` int NOT NULL,
  `codigoVenda` int NOT NULL,
  `IdCliente` int NOT NULL,
  `nomeProduto` varchar(100) NOT NULL,
  `quantidade` int NOT NULL,
  `valorCompra` float NOT NULL,
  `valorVenda` float NOT NULL,
  `valorCompraIndividual` float NOT NULL,
  `valorVendaIndividual` float NOT NULL,
  PRIMARY KEY (`Idprodutos_vendidos`,`IdProduto`,`codigoVenda`),
  KEY `codigoVenda` (`codigoVenda`),
  KEY `IdCliente` (`IdCliente`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `produtos_vendidos`
--

LOCK TABLES `produtos_vendidos` WRITE;
/*!40000 ALTER TABLE `produtos_vendidos` DISABLE KEYS */;
INSERT INTO `produtos_vendidos` VALUES (1,1,2,1,'porca 64',5,840,208.333,35,41.6667);
/*!40000 ALTER TABLE `produtos_vendidos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `IdUsuario` int NOT NULL AUTO_INCREMENT,
  `NomeUsuario` varchar(20) NOT NULL,
  `Senha` varchar(9) NOT NULL,
  PRIMARY KEY (`IdUsuario`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'admin','1903');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `venda`
--

DROP TABLE IF EXISTS `venda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `venda` (
  `IdVenda` int NOT NULL AUTO_INCREMENT,
  `codigoVenda` int NOT NULL,
  `IdProduto` int NOT NULL,
  `nomeProduto` varchar(45) NOT NULL,
  `IdCliente` int NOT NULL,
  `quantidade` int NOT NULL,
  `valorVenda` float NOT NULL,
  `valorVendaIndividual` float NOT NULL,
  PRIMARY KEY (`IdVenda`,`IdProduto`,`IdCliente`),
  KEY `idCliente_idx` (`IdCliente`),
  KEY `idProduto_idx` (`IdProduto`),
  CONSTRAINT `idCliente` FOREIGN KEY (`IdCliente`) REFERENCES `clientes` (`IdCliente`),
  CONSTRAINT `idProduto` FOREIGN KEY (`IdProduto`) REFERENCES `estoque` (`IdProduto`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `venda`
--

LOCK TABLES `venda` WRITE;
/*!40000 ALTER TABLE `venda` DISABLE KEYS */;
INSERT INTO `venda` VALUES (1,1,1,'porca 64',1,3,125,41.6667),(2,2,1,'porca 64',1,5,208.333,41.6667);
/*!40000 ALTER TABLE `venda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `view_venda_cliente`
--

DROP TABLE IF EXISTS `view_venda_cliente`;
/*!50001 DROP VIEW IF EXISTS `view_venda_cliente`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `view_venda_cliente` AS SELECT 
 1 AS `IdVenda`,
 1 AS `codigoVenda`,
 1 AS `IdProduto`,
 1 AS `nomeProduto`,
 1 AS `quantidade`,
 1 AS `valorVenda`,
 1 AS `valorVendaIndividual`,
 1 AS `IdCliente`,
 1 AS `NomCliente`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `view_venda_cliente`
--

/*!50001 DROP VIEW IF EXISTS `view_venda_cliente`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `view_venda_cliente` AS select `v`.`IdVenda` AS `IdVenda`,`v`.`codigoVenda` AS `codigoVenda`,`v`.`IdProduto` AS `IdProduto`,`v`.`nomeProduto` AS `nomeProduto`,`v`.`quantidade` AS `quantidade`,`v`.`valorVenda` AS `valorVenda`,`v`.`valorVendaIndividual` AS `valorVendaIndividual`,`v`.`IdCliente` AS `IdCliente`,`c`.`NomCliente` AS `NomCliente` from (`venda` `v` join `clientes` `c` on((`v`.`IdCliente` = `c`.`IdCliente`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-01 17:56:35
