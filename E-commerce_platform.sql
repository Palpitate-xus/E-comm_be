/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : localhost:3306
 Source Schema         : E-commerce_platform

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 27/06/2023 14:59:59
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for User
-- ----------------------------
DROP TABLE IF EXISTS `User`;
CREATE TABLE `User` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `registration_date` datetime DEFAULT NULL,
  `last_login_date` datetime DEFAULT NULL,
  `user_type` varchar(255) DEFAULT NULL,
  `user_status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT '1',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of User
-- ----------------------------
BEGIN;
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (1, 'john_doe', 'password123', 'john.doe@example.com', NULL, NULL, 'regular', '1');
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (2, '20002526', '123456', '3043863274@qq.com', NULL, NULL, 'customer', '1');
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (3, '20002526', '123456', '3043863274@qq.com', NULL, NULL, 'customer', '1');
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (4, '20002526', '123456', '3043863274@qq.com', '2023-06-27 14:39:25', '2023-06-27 14:39:25', 'customer', '1');
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (5, '20002526', '123456', '3043863274@qq.com', '2023-06-27 14:48:48', NULL, 'customer', '1');
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (6, '20002526', '123456', '3043863274@qq.com', '2023-06-27 14:53:26', NULL, 'customer', 'active');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
