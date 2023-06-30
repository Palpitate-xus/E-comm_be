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

 Date: 30/06/2023 17:00:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Inventory
-- ----------------------------
DROP TABLE IF EXISTS `Inventory`;
CREATE TABLE `Inventory` (
  `supplier_id` int NOT NULL,
  `product_id` int NOT NULL,
  `inventory_time` datetime NOT NULL,
  `stock_quantity` int NOT NULL,
  PRIMARY KEY (`supplier_id`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `Supplier` (`supplier_id`),
  CONSTRAINT `inventory_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `Product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Inventory
-- ----------------------------
BEGIN;
INSERT INTO `Inventory` (`supplier_id`, `product_id`, `inventory_time`, `stock_quantity`) VALUES (1, 1, '2023-06-29 14:29:44', 98);
INSERT INTO `Inventory` (`supplier_id`, `product_id`, `inventory_time`, `stock_quantity`) VALUES (1, 2, '2023-06-29 14:30:52', 109);
INSERT INTO `Inventory` (`supplier_id`, `product_id`, `inventory_time`, `stock_quantity`) VALUES (2, 3, '2023-06-29 18:20:12', 112);
COMMIT;

-- ----------------------------
-- Table structure for Order_detail
-- ----------------------------
DROP TABLE IF EXISTS `Order_detail`;
CREATE TABLE `Order_detail` (
  `order_id` varchar(255) NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int DEFAULT NULL,
  `unit_price` float DEFAULT NULL,
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `Orders` (`order_id`),
  CONSTRAINT `order_detail_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `Product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Order_detail
-- ----------------------------
BEGIN;
INSERT INTO `Order_detail` (`order_id`, `product_id`, `quantity`, `unit_price`) VALUES ('951a140c-f081-4d50-a71d-4f671fe46f5a', 1, 2, 10);
INSERT INTO `Order_detail` (`order_id`, `product_id`, `quantity`, `unit_price`) VALUES ('951a140c-f081-4d50-a71d-4f671fe46f5a', 2, 1, 20);
INSERT INTO `Order_detail` (`order_id`, `product_id`, `quantity`, `unit_price`) VALUES ('951a140c-f081-4d50-a71d-4f671fe46f5a', 3, 1, 20);
COMMIT;

-- ----------------------------
-- Table structure for Orders
-- ----------------------------
DROP TABLE IF EXISTS `Orders`;
CREATE TABLE `Orders` (
  `order_id` varchar(255) NOT NULL,
  `user_id` int NOT NULL,
  `order_status` varchar(255) DEFAULT NULL,
  `total_amount` float DEFAULT NULL,
  `order_time` datetime DEFAULT NULL,
  `payment_status` varchar(255) DEFAULT NULL,
  `payment_method` varchar(255) DEFAULT NULL,
  `shipping_address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Orders
-- ----------------------------
BEGIN;
INSERT INTO `Orders` (`order_id`, `user_id`, `order_status`, `total_amount`, `order_time`, `payment_status`, `payment_method`, `shipping_address`) VALUES ('951a140c-f081-4d50-a71d-4f671fe46f5a', 14, 'Pending', 60, '2023-06-30 14:54:30', 'unpaid', NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for Product
-- ----------------------------
DROP TABLE IF EXISTS `Product`;
CREATE TABLE `Product` (
  `product_id` int NOT NULL,
  `product_name` varchar(255) NOT NULL,
  `product_description` varchar(255) NOT NULL,
  `product_price` float NOT NULL,
  `category_id` int NOT NULL,
  `product_image` varchar(255) NOT NULL,
  `product_status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Product
-- ----------------------------
BEGIN;
INSERT INTO `Product` (`product_id`, `product_name`, `product_description`, `product_price`, `category_id`, `product_image`, `product_status`) VALUES (1, 'asd', 'dfdg', 3, 1, 'a', 'active');
INSERT INTO `Product` (`product_id`, `product_name`, `product_description`, `product_price`, `category_id`, `product_image`, `product_status`) VALUES (2, 'dfghm', 'cvn', 3, 2, 'd', 'active');
INSERT INTO `Product` (`product_id`, `product_name`, `product_description`, `product_price`, `category_id`, `product_image`, `product_status`) VALUES (3, 'asder', 'dfg', 3, 4, 'd', 'active');
INSERT INTO `Product` (`product_id`, `product_name`, `product_description`, `product_price`, `category_id`, `product_image`, `product_status`) VALUES (4, 'asd', 'asd', 3, 4, 'a', 'offshelf');
COMMIT;

-- ----------------------------
-- Table structure for Shopping_cart
-- ----------------------------
DROP TABLE IF EXISTS `Shopping_cart`;
CREATE TABLE `Shopping_cart` (
  `user_id` int NOT NULL,
  `product_id` int NOT NULL,
  `quantity` int NOT NULL,
  `add_time` datetime NOT NULL,
  UNIQUE KEY `unique_user_product` (`user_id`,`product_id`),
  KEY `shopping_cart_ibfk_2` (`product_id`),
  CONSTRAINT `shopping_cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
  CONSTRAINT `shopping_cart_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `Product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Shopping_cart
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for Supplier
-- ----------------------------
DROP TABLE IF EXISTS `Supplier`;
CREATE TABLE `Supplier` (
  `supplier_id` int NOT NULL,
  `supplier_name` varchar(255) NOT NULL,
  `supplier_address` varchar(255) NOT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Supplier
-- ----------------------------
BEGIN;
INSERT INTO `Supplier` (`supplier_id`, `supplier_name`, `supplier_address`) VALUES (1, 'apple', 'asd');
INSERT INTO `Supplier` (`supplier_id`, `supplier_name`, `supplier_address`) VALUES (2, 'microsoft', 'asdf');
COMMIT;

-- ----------------------------
-- Table structure for Supplier_product
-- ----------------------------
DROP TABLE IF EXISTS `Supplier_product`;
CREATE TABLE `Supplier_product` (
  `supplier_id` int NOT NULL,
  `product_id` int NOT NULL,
  PRIMARY KEY (`supplier_id`,`product_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `supplier_product_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `Supplier` (`supplier_id`),
  CONSTRAINT `supplier_product_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `Product` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Supplier_product
-- ----------------------------
BEGIN;
INSERT INTO `Supplier_product` (`supplier_id`, `product_id`) VALUES (1, 1);
INSERT INTO `Supplier_product` (`supplier_id`, `product_id`) VALUES (1, 2);
INSERT INTO `Supplier_product` (`supplier_id`, `product_id`) VALUES (2, 3);
COMMIT;

-- ----------------------------
-- Table structure for Supply_order
-- ----------------------------
DROP TABLE IF EXISTS `Supply_order`;
CREATE TABLE `Supply_order` (
  `supplyorder_id` varchar(255) NOT NULL,
  `supplier_id` int DEFAULT NULL,
  `order_status` varchar(255) NOT NULL,
  `order_time` datetime NOT NULL,
  PRIMARY KEY (`supplyorder_id`),
  KEY `supplier_id` (`supplier_id`),
  CONSTRAINT `supply_order_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `Supplier` (`supplier_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Supply_order
-- ----------------------------
BEGIN;
INSERT INTO `Supply_order` (`supplyorder_id`, `supplier_id`, `order_status`, `order_time`) VALUES ('0ac345cf-e1cd-4bec-87e7-32b5c2a37ac3', 1, 'Pending', '2023-06-30 14:54:30');
INSERT INTO `Supply_order` (`supplyorder_id`, `supplier_id`, `order_status`, `order_time`) VALUES ('d29dcf9a-93ad-4dc8-bc91-f57c1a28da77', 2, 'Pending', '2023-06-30 14:54:30');
COMMIT;

-- ----------------------------
-- Table structure for Supply_orderdetail
-- ----------------------------
DROP TABLE IF EXISTS `Supply_orderdetail`;
CREATE TABLE `Supply_orderdetail` (
  `supplyorder_id` varchar(255) DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `order_id` varchar(255) DEFAULT NULL,
  KEY `supplyorder_id` (`supplyorder_id`),
  KEY `product_id` (`product_id`),
  KEY `order_id` (`order_id`),
  CONSTRAINT `supply_orderdetail_ibfk_1` FOREIGN KEY (`supplyorder_id`) REFERENCES `Supply_order` (`supplyorder_id`),
  CONSTRAINT `supply_orderdetail_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `Product` (`product_id`),
  CONSTRAINT `supply_orderdetail_ibfk_3` FOREIGN KEY (`order_id`) REFERENCES `Orders` (`order_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Supply_orderdetail
-- ----------------------------
BEGIN;
INSERT INTO `Supply_orderdetail` (`supplyorder_id`, `product_id`, `quantity`, `order_id`) VALUES ('0ac345cf-e1cd-4bec-87e7-32b5c2a37ac3', 1, 2, '951a140c-f081-4d50-a71d-4f671fe46f5a');
INSERT INTO `Supply_orderdetail` (`supplyorder_id`, `product_id`, `quantity`, `order_id`) VALUES ('0ac345cf-e1cd-4bec-87e7-32b5c2a37ac3', 2, 1, '951a140c-f081-4d50-a71d-4f671fe46f5a');
INSERT INTO `Supply_orderdetail` (`supplyorder_id`, `product_id`, `quantity`, `order_id`) VALUES ('d29dcf9a-93ad-4dc8-bc91-f57c1a28da77', 3, 1, '951a140c-f081-4d50-a71d-4f671fe46f5a');
COMMIT;

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
  PRIMARY KEY (`user_id`) USING BTREE,
  UNIQUE KEY `email` (`email`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of User
-- ----------------------------
BEGIN;
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (14, '20002526', '123456', '3043863274@qq.com', '2023-06-28 11:26:51', '2023-06-30 13:32:59', 'customer', 'active');
INSERT INTO `User` (`user_id`, `username`, `password`, `email`, `registration_date`, `last_login_date`, `user_type`, `user_status`) VALUES (16, '20002526', '123456', '304386324@qq.com', '2023-06-28 20:02:30', NULL, 'customer', 'active');
COMMIT;

-- ----------------------------
-- Table structure for Wishlist
-- ----------------------------
DROP TABLE IF EXISTS `Wishlist`;
CREATE TABLE `Wishlist` (
  `product_id` int NOT NULL,
  `user_id` int NOT NULL,
  `add_time` datetime NOT NULL,
  `wish_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`wish_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Wishlist
-- ----------------------------
BEGIN;
INSERT INTO `Wishlist` (`product_id`, `user_id`, `add_time`, `wish_id`) VALUES (1, 14, '2023-06-30 16:29:08', 1);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
