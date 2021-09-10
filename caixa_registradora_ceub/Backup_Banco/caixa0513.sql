-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema qzaqwxh0wi
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema qzaqwxh0wi
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `qzaqwxh0wi` DEFAULT CHARACTER SET latin1 ;
USE `qzaqwxh0wi` ;

-- -----------------------------------------------------
-- Table `qzaqwxh0wi`.`ta_pedido_produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qzaqwxh0wi`.`ta_pedido_produto` (
  `cod_pedido` INT(11) NOT NULL,
  `cod_produto` INT(11) NOT NULL,
  `qtd_produto` INT(11) NOT NULL,
  PRIMARY KEY (`cod_pedido`, `cod_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `qzaqwxh0wi`.`tb_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qzaqwxh0wi`.`tb_cliente` (
  `idt_cliente` INT(11) NOT NULL AUTO_INCREMENT,
  `nme_cliente` VARCHAR(45) NOT NULL,
  `endereco_cliente` VARCHAR(100) NOT NULL,
  `qtd_token` INT(11) NULL DEFAULT NULL,
  `CPF` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`idt_cliente`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `qzaqwxh0wi`.`tb_funcionario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qzaqwxh0wi`.`tb_funcionario` (
  `idt_funcionario` INT(11) NOT NULL AUTO_INCREMENT,
  `nme_funcionario` VARCHAR(45) NOT NULL,
  `username` VARCHAR(45) NOT NULL,
  `senha` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idt_funcionario`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `qzaqwxh0wi`.`tb_pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qzaqwxh0wi`.`tb_pedido` (
  `idt_pedido` INT(11) NOT NULL AUTO_INCREMENT,
  `cod_funcionario` INT(11) NOT NULL,
  `cod_cliente` INT(11) NOT NULL,
  `DataHora` DATETIME NOT NULL,
  `vlr_total` DECIMAL(8,2) NOT NULL,
  `vlr_total_token` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`idt_pedido`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


-- -----------------------------------------------------
-- Table `qzaqwxh0wi`.`tb_produto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `qzaqwxh0wi`.`tb_produto` (
  `idt_produto` INT(11) NOT NULL AUTO_INCREMENT,
  `nme_produto` VARCHAR(45) NOT NULL,
  `vlr_produto` DECIMAL(8,2) NULL DEFAULT NULL,
  `vlr_produto_token` INT(11) NOT NULL,
  PRIMARY KEY (`idt_produto`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COLLATE = utf8_unicode_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
