-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 15, 2024 at 10:56 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `services_selling_platforms_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('1ad0aab45c78');

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `message` text NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`id`, `sender_id`, `receiver_id`, `message`, `timestamp`) VALUES
(1, 1, 3, 'zxnvm,xzcnvm,xzcnvm,z.xcnvm,xcnvm,.n xm,nxcvnxcm, nvm,.xcnv', '2024-09-07 12:06:46'),
(2, 1, 3, 'klvzxcklvmxc,.zjvkl;jfgk;sdjfa;sdkm ;lxcvm,xc./ , v./xcz,v./xcz,v/ ', '2024-09-07 12:06:52'),
(3, 1, 3, 'xvcvzxcvxcv', '2024-09-07 12:06:55'),
(4, 4, 2, 'fasdjfhlsdafjlksdj kl;jsdfkjsdkl;jfsdafsd', '2024-09-07 12:31:23'),
(5, 4, 2, 'jg;klfsdjgklsdfjklgjsdfkl dfklgjkdfljgklsdfjg; lkjfdg', '2024-09-07 12:31:49'),
(6, 1, 2, 'fnsdm.anfm,sd.hf. m,nm,sdnfm,sdnafhrwejlhfsda f', '2024-09-07 12:32:54'),
(7, 1, 2, 'f./smg.,asdfm/g.,sdmfklwejrkl jsdkajfklsdaj fklsda fhsdjhfsdjkhfsdhaf jksdhajkfhsdjklahfjsad hfkjsdahfsda', '2024-09-07 12:33:00'),
(8, 1, 2, 'sdfsdaf sdfsdafsdafsdafsdfsdfsdafrewrwerwerwerwe', '2024-09-07 12:33:05'),
(9, 1, 3, 'fgsdfgsdf gdfgsdf gsdf gdfg', '2024-09-10 09:22:14'),
(10, 1, 3, 'gfdsg fdgdfsgsdfgsdfgsdfgsdf', '2024-09-10 09:22:17'),
(11, 1, 3, 'dfg sdfgsdfgsdfgsdfgsdf gdfgdfg', '2024-09-10 09:22:21'),
(14, 1, 1, 'sdfgdfgsdfgsdfgdf', '2024-09-10 09:53:30'),
(15, 1, 1, 'gsdfgsdfgdfsgsdfgertweqaresdfsdf ', '2024-09-10 09:53:35'),
(16, 1, 1, 'dfasdfdsfdsf dfdsfsdfa', '2024-09-10 09:53:38'),
(17, 1, 1, 'dsfsdagfgfdsgdgdfg', '2024-09-10 10:13:19'),
(18, 1, 1, 'dfsgsdfgdfgdfgdgdfg', '2024-09-10 10:21:28'),
(19, 1, 1, 'dfgsdftretewrtwer fdgsdfg', '2024-09-10 10:21:36'),
(20, 1, 1, 'fgdfsgsdfgsdfg', '2024-09-10 10:26:36'),
(21, 4, 2, 'sdfsdafsdaf sdfsda fsda fsdaf', '2024-09-10 10:30:32'),
(22, 4, 2, 'dsfsda ghdfgfdgdf gsdfgdf', '2024-09-10 10:30:36'),
(23, 4, 2, 'rauf khalid', '2024-09-10 10:31:00'),
(24, 1, 2, 'Ad tempor velit aut ', '2024-09-10 10:34:48'),
(25, 1, 3, 'Autem voluptatem Cu', '2024-09-10 10:35:20'),
(26, 4, 3, 'Proident Nam aliqui', '2024-09-10 10:36:51'),
(27, 4, 3, 'Quidem aut cillum ma', '2024-09-10 10:36:53'),
(28, 4, 3, 'Saepe voluptatem do', '2024-09-10 10:36:55'),
(31, 4, 3, 'sdfgdfg', '2024-09-10 10:42:22'),
(33, 1, 1, 'fdgdfsgd fgdfgdf', '2024-09-10 10:42:49'),
(35, 4, 3, 'dsfsdf', '2024-09-10 10:50:25'),
(36, 4, 3, 'dsfdsfsdf', '2024-09-10 10:51:27'),
(37, 1, 3, 'hgfhfghd', '2024-09-10 10:51:38'),
(38, 1, 2, '324', '2024-10-04 06:42:46'),
(39, 1, 3, 'hello', '2024-10-04 06:45:45'),
(40, 1, 2, 'hello', '2024-10-04 06:46:48');

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `message` text NOT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `cust_id` int(11) NOT NULL,
  `cust_user_name` varchar(50) NOT NULL,
  `cust_full_name` varchar(50) NOT NULL,
  `cust_phone` varchar(50) NOT NULL,
  `cust_gender` varchar(20) NOT NULL,
  `cust_rol_name` varchar(20) NOT NULL,
  `cust_password` varchar(256) NOT NULL,
  `cust_photo` varchar(256) DEFAULT NULL,
  `cust_registrationDate` date NOT NULL,
  `isActive` tinyint(1) NOT NULL,
  `cust_drop_address` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` (`cust_id`, `cust_user_name`, `cust_full_name`, `cust_phone`, `cust_gender`, `cust_rol_name`, `cust_password`, `cust_photo`, `cust_registrationDate`, `isActive`, `cust_drop_address`) VALUES
(1, 'asad12345', 'Asad Khan', '03409836430', 'Male', 'Customer', 'scrypt:32768:8:1$8MliOsxXrfGEXYO9$2f0e7077f7e71f156ea9a0e008f87737ae59545b055491087c8da0b72bb88d0aab354382ce8ec296f2d5337b5fe07a422491b9b46696c9728c0f4d719a1992d7', NULL, '2024-03-22', 1, 'plot no#72 street No#9 District Islamabad'),
(4, 'rauf1234', 'Rauf Khalid', '03366645807', 'Male', 'Customer', 'scrypt:32768:8:1$Bfq0MgvZO8SdWfp4$a56cdd05796a780eebf4dba763d3668d6a89853fdaa87355fe0cddd49057e227aa36d973ac3379f571eb494f7c6104bd1c71335012f7279a5cf7e44acfc3e0a8', NULL, '2024-03-22', 1, 'Village Waligai P/O Waligai District Swat\r\n'),
(5, 'wali1234', 'Wali Rehman', '03464589752', 'Male', 'Customer', 'scrypt:32768:8:1$8MliOsxXrfGEXYO9$2f0e7077f7e71f156ea9a0e008f87737ae59545b055491087c8da0b72bb88d0aab354382ce8ec296f2d5337b5fe07a422491b9b46696c9728c0f4d719a1992d7', NULL, '2024-05-07', 1, 'plot no#71 street No#9 District Islamabad\r\n'),
(6, 'abuzar1234', 'Abu Zar', '03245684554', 'Male', 'Customer', 'scrypt:32768:8:1$moFxCmjT505tLHxo$904ec3e68444172898415765e0bda6081c3cdc1648dcaf7f89bfc33f1249aab3159e1564f5f0adde098e0737b34ba1903d825cf395c2efa1e9771153dedeb313', NULL, '2024-05-08', 1, 'Village Waligai P/O Waligai District kashmir'),
(7, 'iqrakhan', 'Iqra Fazeelat', '03418523548', 'Female', 'Customer', 'scrypt:32768:8:1$8hXV6f8pwmPAhjYI$7db5097aee4d6a89b8bd8a981a5e63a15531227fbdc99f14fe9dde847bba1e4f2112d6279015d7e73c8b444cd892f61b5a844cc37560fb9fe091f2ba1de2e292', NULL, '2024-05-20', 1, 'Makaran, Sradi Bhalgran, P/O Thorar, Tahsil Thorar, District Poonch'),
(8, 'adeelahmad', 'Adeel Ahmad', '03418523500', 'Male', 'Customer', 'scrypt:32768:8:1$YLZVXron15Cbuk8n$39194b978d0438c635ac0054a183a6ea3852e628a6a427aecf50d72ddda38d9c9fb9da15aca1f49c2f13030ba15c25cc5bb718dd41e44cd1befac726e4c625fd', NULL, '2024-06-04', 1, 'Poonch Ajk');

-- --------------------------------------------------------

--
-- Table structure for table `make_notification`
--

CREATE TABLE `make_notification` (
  `n_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `notification_info` varchar(50) DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `is_check_by_manager` tinyint(1) DEFAULT NULL,
  `is_check_by_employee` tinyint(1) DEFAULT NULL,
  `is_check_by_parent` tinyint(1) DEFAULT NULL,
  `is_check_by_delivery_boy` tinyint(1) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `make_notification`
--

INSERT INTO `make_notification` (`n_id`, `user_id`, `notification_info`, `end_date`, `is_check_by_manager`, `is_check_by_employee`, `is_check_by_parent`, `is_check_by_delivery_boy`, `status`, `created_at`, `updated_at`) VALUES
(3, 1, 'i want to inform you that sunday was holiday', '2024-05-01', 0, 0, 0, 0, 'Ended', '2024-05-06 04:21:38', '2024-05-19 18:17:15'),
(4, 1, 'dsfdsfadsfsdfadgdsgfdsf', '2024-05-16', 0, 0, 0, 0, 'Ended', '2024-05-06 04:33:37', '2024-05-19 18:17:01'),
(5, 1, 'Today is friday.', '2024-12-11', 0, 0, 0, 0, 'Live', '2024-05-19 18:17:58', '2024-05-19 18:17:58');

-- --------------------------------------------------------

--
-- Table structure for table `make_report`
--

CREATE TABLE `make_report` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `select_reason` varchar(100) DEFAULT NULL,
  `send_report_message` varchar(255) DEFAULT NULL,
  `is_check_by_admin` tinyint(1) DEFAULT NULL,
  `received_report_message` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Table structure for table `order`
--

CREATE TABLE `order` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `price` decimal(20,1) NOT NULL,
  `order_date` datetime NOT NULL,
  `isActive` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `p_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `pc_id` int(11) NOT NULL,
  `p_name` varchar(100) NOT NULL,
  `p_description` text DEFAULT NULL,
  `p_price` decimal(20,1) NOT NULL,
  `p_image` varchar(255) DEFAULT NULL,
  `p_original_image` varchar(255) DEFAULT NULL,
  `p_isActive` tinyint(1) NOT NULL,
  `p_registrationDate` datetime NOT NULL,
  `p_stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`p_id`, `user_id`, `pc_id`, `p_name`, `p_description`, `p_price`, `p_image`, `p_original_image`, `p_isActive`, `p_registrationDate`, `p_stock`) VALUES
(1, 2, 4, 'Art Arabic Calligraphy', 'Hand Paint Calligraphy', 550.0, 'modified_7279885_2.jpeg', '7279885_2.jpeg', 1, '2024-03-19 11:02:53', 5),
(3, 2, 3, 'Acyclic Painting ', 'Calligraphy', 300.0, 'modified_7148154_2.jpeg', '7148154_2.jpeg', 1, '2024-03-19 20:19:10', 4),
(5, 2, 8, 'Quran Ayat', 'Quran Ayat Calligraphy', 250.0, 'modified_5218418_2.jpeg', '5218418_2.jpeg', 1, '2024-03-19 20:22:11', 50),
(7, 2, 3, 'Calligraphy', 'Painting , Calligraphy, waterfall', 700.0, 'modified_9676514_2.jpg', '9676514_2.jpg', 1, '2024-03-19 20:23:59', 1),
(8, 2, 4, 'Arabic Art ', 'Hand Paint Calligraphy', 550.0, 'modified_7635473_2.jpeg', '7635473_2.jpeg', 1, '2024-03-19 20:25:12', 1),
(9, 3, 4, 'Calligraphy', 'Arabic Calligraphy', 480.0, 'modified_2163245_3.jpg', '2163245_3.jpg', 0, '2024-03-19 20:30:05', 0),
(13, 2, 3, 'Islamic Calligraphy', 'Painting , Calligraphy', 600.0, 'modified_8883798_2.jpeg', '8883798_2.jpeg', 1, '2024-03-19 20:32:59', 1),
(15, 2, 4, 'Arabic Quran Verse', 'Calligraphy Painting Quran Verse', 410.0, 'modified_8777331_2.jpeg', '8777331_2.jpeg', 1, '2024-03-19 20:35:01', 1),
(16, 2, 4, 'Arabic CalliPaint', 'Hand Paint Calligraphy Painting', 380.0, 'modified_7768598_2.jpeg', '7768598_2.jpeg', 1, '2024-03-19 20:35:38', 20),
(17, 2, 4, 'Calligraphy Painting', 'Hand Paint Calligraphy Painting', 260.0, 'modified_6519444_2.jpeg', '6519444_2.jpeg', 1, '2024-03-19 20:36:18', 0),
(27, 2, 4, 'Islamic CalliPaint', 'Painting, Calligraphy', 500.0, 'modified_4809463_2.jpeg', '4809463_2.jpeg', 1, '2024-05-09 01:00:40', 1),
(33, 6, 3, 'Home painting', 'Hand paint', 300.0, 'modified_2113991_6.jpg', '2113991_6.jpg', 1, '2024-09-17 07:46:37', 1),
(34, 6, 3, 'flower painting', 'Hand paint', 400.0, 'modified_5237263_6.jpg', '5237263_6.jpg', 1, '2024-09-17 07:47:45', 1),
(35, 6, 3, 'flower', 'painting', 300.0, 'modified_3589635_6.jpg', '3589635_6.jpg', 1, '2024-09-17 07:48:12', 1),
(36, 6, 3, 'painting', 'Tree ', 350.0, 'modified_4043773_6.jpg', '4043773_6.jpg', 1, '2024-09-17 07:48:49', 1),
(37, 7, 4, 'photograph', 'nature photography', 200.0, 'modified_3770994_7.jpg', '3770994_7.jpg', 1, '2024-09-17 07:53:22', 1),
(38, 7, 4, 'flower ', '', 300.0, 'modified_3721670_7.jpg', '3721670_7.jpg', 1, '2024-09-17 07:54:36', 1),
(39, 7, 4, 'Nature', '', 300.0, 'modified_6273275_7.jpg', '6273275_7.jpg', 1, '2024-09-17 07:55:24', 1),
(40, 7, 4, 'photograph', '', 200.0, 'modified_3291956_7.jpg', '3291956_7.jpg', 1, '2024-09-17 07:55:52', 1),
(41, 3, 3, 'painting', '', 300.0, 'modified_2944251_3.jpg', '2944251_3.jpg', 1, '2024-09-17 08:08:32', 1),
(42, 3, 3, 'Home painting', '', 300.0, 'modified_3864606_3.jpg', '3864606_3.jpg', 1, '2024-09-17 08:09:16', 1),
(49, 8, 8, 'calligraphy', 'la ilaha illallah ', 200.0, 'modified_9446232_8.jpg', '9446232_8.jpg', 1, '2024-09-22 12:25:08', 1),
(50, 8, 8, 'Bismillah', 'bismillah ', 200.0, 'modified_5614969_8.jpg', '5614969_8.jpg', 1, '2024-09-22 12:26:03', 3),
(52, 8, 8, 'Arabic Calligraphy', '', 300.0, 'modified_4946586_8.jpg', '4946586_8.jpg', 1, '2024-09-22 12:37:53', 1),
(53, 8, 8, 'Allah', 'Ayat', 350.0, 'modified_4045658_8.jpg', '4045658_8.jpg', 1, '2024-09-22 12:39:15', 1),
(54, 3, 3, 'Wall Art', 'Wall', 250.0, 'modified_5373472_3.jpg', '5373472_3.jpg', 1, '2024-09-22 12:42:28', 1),
(55, 3, 3, 'islamic painting', 'islamic', 300.0, 'modified_8565312_3.jpg', '8565312_3.jpg', 1, '2024-09-22 12:43:19', 1),
(56, 3, 3, 'Arabic ', 'Painting', 350.0, 'modified_7883948_3.jpg', '7883948_3.jpg', 1, '2024-09-22 12:43:48', 1),
(57, 3, 3, 'Quran verse', 'verse', 300.0, 'modified_7536529_3.jpg', '7536529_3.jpg', 1, '2024-09-22 12:44:15', 1),
(58, 5, 4, 'photographer', '', 200.0, 'modified_8615913_5.jpg', '8615913_5.jpg', 1, '2024-09-22 12:53:16', 1),
(59, 5, 4, 'photographer', 'best photograph', 350.0, 'modified_3493440_5.jpg', '3493440_5.jpg', 1, '2024-09-22 12:54:18', 1),
(60, 5, 8, 'Birds photograph', 'photograph', 250.0, 'modified_8674104_5.jpg', '8674104_5.jpg', 1, '2024-09-22 12:54:57', 1);

-- --------------------------------------------------------

--
-- Table structure for table `product_category`
--

CREATE TABLE `product_category` (
  `pc_id` int(11) NOT NULL,
  `pc_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_category`
--

INSERT INTO `product_category` (`pc_id`, `pc_name`) VALUES
(8, 'Calligraphy'),
(3, 'Painter'),
(4, 'Photographer');

-- --------------------------------------------------------

--
-- Table structure for table `product_download_verification`
--

CREATE TABLE `product_download_verification` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `is_verified` tinyint(1) DEFAULT NULL,
  `transaction_no` tinyint(1) DEFAULT NULL,
  `feedback_description` varchar(255) DEFAULT NULL,
  `feedback_stars` int(11) DEFAULT NULL,
  `feedback_submitted` tinyint(1) DEFAULT NULL,
  `delivery_boy_id` int(11) DEFAULT NULL,
  `delivery_status` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `select_payment_method` varchar(100) DEFAULT NULL,
  `receipt_file_path` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_download_verification`
--

INSERT INTO `product_download_verification` (`id`, `customer_id`, `product_id`, `is_verified`, `transaction_no`, `feedback_description`, `feedback_stars`, `feedback_submitted`, `delivery_boy_id`, `delivery_status`, `created_at`, `select_payment_method`, `receipt_file_path`) VALUES
(25, 1, 3, 1, 1, 'good', 4, 1, NULL, 'Deliver', '2024-09-07 05:45:13', 'EasyPaisa', '1771910_25.jpg'),
(26, 1, 7, 1, 1, 'some thing good', 3, 1, NULL, 'OnTheWay', '2024-09-10 05:37:39', 'Jazz Cash', '2282173_26.jpg'),
(27, 1, 9, 1, 1, 'very good', 5, 1, NULL, 'OnTheWay', '2024-09-10 09:09:58', 'EasyPaisa', '8456039_27.png'),
(28, 1, 5, 0, 0, NULL, NULL, 0, NULL, NULL, '2024-09-16 05:32:21', NULL, NULL),
(29, 1, 13, 0, 0, NULL, NULL, 0, NULL, NULL, '2024-09-21 11:00:37', NULL, NULL),
(30, 5, 35, 0, 0, NULL, NULL, 0, NULL, NULL, '2024-09-21 11:08:49', NULL, NULL),
(31, 1, 50, 0, 0, NULL, NULL, 0, NULL, NULL, '2024-09-26 04:46:43', NULL, NULL),
(32, 1, 52, 0, 0, NULL, NULL, 0, NULL, NULL, '2024-09-26 04:47:45', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `user_name` varchar(50) DEFAULT NULL,
  `full_name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `cnic` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `rol_name` varchar(20) DEFAULT NULL,
  `password` varchar(256) DEFAULT NULL,
  `photo` varchar(256) DEFAULT NULL,
  `isActive` tinyint(1) NOT NULL,
  `registrationDate` date NOT NULL,
  `delivery_status` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `user_name`, `full_name`, `email`, `phone`, `cnic`, `gender`, `rol_name`, `password`, `photo`, `isActive`, `registrationDate`, `delivery_status`) VALUES
(1, 'Admin', 'Rauf Khalid', 'raufkhalis27@gmail.com', '03366645807', '1111111111111', 'Male', 'Administrator', 'scrypt:32768:8:1$r1uj7qL4KvRsXHkr$65d484f336c167e6026e2e1d51a104b356f9cfbf5bd98c73ba08d7f74cc5c38b0177a612f36b4c8859516cc662212d53ef4b05a2f76b9b372a2ffa8c50934c4b', '1532608_7.jpg', 1, '2024-02-17', NULL),
(2, 'Calligrapher', 'Asad Khan', 'asadkhan@gmail.com', '03366645808', '2222222222222', 'Male', 'Artist', 'scrypt:32768:8:1$r1uj7qL4KvRsXHkr$65d484f336c167e6026e2e1d51a104b356f9cfbf5bd98c73ba08d7f74cc5c38b0177a612f36b4c8859516cc662212d53ef4b05a2f76b9b372a2ffa8c50934c4b', '7857447_2.jpg', 1, '2024-03-18', NULL),
(3, 'Painter', 'Kaleem Khan', 'kaleem23@gmail.com', '03409836431', '3333333333333', 'Male', 'Artist', 'scrypt:32768:8:1$r1uj7qL4KvRsXHkr$65d484f336c167e6026e2e1d51a104b356f9cfbf5bd98c73ba08d7f74cc5c38b0177a612f36b4c8859516cc662212d53ef4b05a2f76b9b372a2ffa8c50934c4b', '6740264_3.jpg', 1, '2024-03-18', NULL),
(5, 'Photographer', 'Irsa Sadiq', 'irsasadiq20@gmail.com', '03441567345', '1234567890', 'Male', 'Artist', 'scrypt:32768:8:1$NfEW3l5p093yEKap$78d5982432bd0387e1aa5c3282ca84378c6f540fa174cdc429b06977a898011338970a4b970a58e4ce1222d8e2ae214adeee8b0b86b39ddd55d51eb030d54cc0', '8057643_5.jpg', 1, '2024-05-20', 'Available'),
(6, 'Painter', 'Noor Khan', 'noorkhan00@gmail.com', '03409985774', '8230356809842', 'Female', 'Artist', 'scrypt:32768:8:1$HzQpHUbd39MMPhA8$4e39ec3d91d62e40be7cc0b27c40e2c5dba618974e2e7486ec7492e73561ba7fc4ab01744c957dec94f38358cc24698d2625acafd9bcfb5912b58b57c984fc71', '4208049_6.jpeg', 1, '2024-05-20', 'Available'),
(7, 'Photographer', 'Khan', 'asherkhan@gmail.com', '03418523549', '01234567890', 'Male', 'Artist', 'scrypt:32768:8:1$68WEfj6Ys4HPTlm8$81ea188a19604bf695a40c2d5723b383b0adf68d29a0e1c37951e5f3ccc9d4409a15ead05e248d0bb89ba341ddcea8fcc4bd3effe62e9f7dc92712a2a3f3f7d9', '4820324_7.jpg', 1, '2024-06-04', 'Available'),
(8, 'Calligrapher', 'Mudasir', 'rerr@gfcg.com', '56467547656', '0000000000000', 'Male', 'Artist', 'scrypt:32768:8:1$R6pSJzFb7mPZUevW$f07159d6c193239ad422edd348256fc945ae47307715d7dc651801b05ea2c412add34bd24407f68af2cab4baec16eaea9985e6e4942cd3cc1f1c0c1c6601c1bd', '6041770_8.jpg', 1, '2024-06-10', 'Available'),
(9, 'MuhmmadAli', 'Alikhan', 'Ali899@gmail.com', '03457689432', '821017896554', 'Male', 'Artist', 'scrypt:32768:8:1$yNO2oW2DQdhJJ4UI$69ddcfb99672b318a2e1fb6dc18256c115effd741452950b5c6ffdbf3f9c5a461f108f66ca8951428c9c1c3da877bb8ab2fc416cb7a315b684c151126dc55042', NULL, 1, '2024-09-16', 'Available'),
(10, '3333333333333', 'amir', 'amir786@gmail.con', '0345678902', '45678901234', 'Male', 'Artist', 'scrypt:32768:8:1$14CP0kZZuv8CzIP8$1f4693250594d1fef72f9edd443294e9439efd27e1a037de66db198ae7c48722d25aa3b0573e467dda876d2b741972adde438d0d443082c3d78eca88cf5f2d33', NULL, 1, '2024-09-17', 'Available'),
(11, '1111111111111', 'waqaskhan', 'khan123@gmail.com', '03469867543', '4444444444444', 'Male', 'Artist', 'scrypt:32768:8:1$VZyUH5ZJkYlxNaEZ$548d00dd2e9d44eee7633126771b3b20145db55ae0cd2d1bf2e990803b9e4e0059258e1f55791f04e4682f64dfbc3c6605832145f6aaa56ed95b50c78b839129', NULL, 1, '2024-09-17', 'Available'),
(12, 'zaheer', 'zaheerahmed', 'zaheer12345@gmail.com', '03467854321', '1234567891', 'Male', 'Artist', 'scrypt:32768:8:1$4I7Q2jaHwKBr5QIq$d0d7d58d366d391e15b3c7c88d42f94ffe0765343388d774fef0f2b22130ada063b8f4cc70a7e1fbab0e71fa391305ad9d30a961d2fafd4e40ebe43d938bfbb4', NULL, 0, '2024-09-18', 'Available'),
(13, 'imrankhan', 'khankhan', 'khan12345@gmail.com', '03234567893', '0999999999999', 'Male', 'Artist', 'scrypt:32768:8:1$Bog0VrVHU9GqZdQP$3a6edbf1360a0b5323cfbb5602b72351c0f115cb90283786ccea71e530a868f26fc435778b29d33c48d5d368abb4ef5003f5470cad025e4001837fa68030a38d', NULL, 0, '2024-09-18', 'Available');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`),
  ADD KEY `receiver_id` (`receiver_id`),
  ADD KEY `sender_id` (`sender_id`);

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`cust_id`),
  ADD UNIQUE KEY `cust_phone` (`cust_phone`),
  ADD UNIQUE KEY `cust_user_name` (`cust_user_name`);

--
-- Indexes for table `make_notification`
--
ALTER TABLE `make_notification`
  ADD PRIMARY KEY (`n_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `make_report`
--
ALTER TABLE `make_report`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `order`
--
ALTER TABLE `order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `product_id` (`product_id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`p_id`),
  ADD KEY `pc_id` (`pc_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `product_category`
--
ALTER TABLE `product_category`
  ADD PRIMARY KEY (`pc_id`),
  ADD UNIQUE KEY `pc_name` (`pc_name`);

--
-- Indexes for table `product_download_verification`
--
ALTER TABLE `product_download_verification`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `product_id` (`product_id`),
  ADD KEY `delivery_boy_id` (`delivery_boy_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `cnic` (`cnic`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `customers`
--
ALTER TABLE `customers`
  MODIFY `cust_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `make_notification`
--
ALTER TABLE `make_notification`
  MODIFY `n_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `make_report`
--
ALTER TABLE `make_report`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `order`
--
ALTER TABLE `order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `product_category`
--
ALTER TABLE `product_category`
  MODIFY `pc_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `product_download_verification`
--
ALTER TABLE `product_download_verification`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `chat`
--
ALTER TABLE `chat`
  ADD CONSTRAINT `chat_ibfk_1` FOREIGN KEY (`receiver_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `chat_ibfk_2` FOREIGN KEY (`sender_id`) REFERENCES `customers` (`cust_id`);

--
-- Constraints for table `make_notification`
--
ALTER TABLE `make_notification`
  ADD CONSTRAINT `make_notification_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `make_report`
--
ALTER TABLE `make_report`
  ADD CONSTRAINT `make_report_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `order`
--
ALTER TABLE `order`
  ADD CONSTRAINT `order_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`cust_id`),
  ADD CONSTRAINT `order_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`p_id`);

--
-- Constraints for table `products`
--
ALTER TABLE `products`
  ADD CONSTRAINT `products_ibfk_1` FOREIGN KEY (`pc_id`) REFERENCES `product_category` (`pc_id`),
  ADD CONSTRAINT `products_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `product_download_verification`
--
ALTER TABLE `product_download_verification`
  ADD CONSTRAINT `product_download_verification_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`cust_id`),
  ADD CONSTRAINT `product_download_verification_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`p_id`),
  ADD CONSTRAINT `product_download_verification_ibfk_3` FOREIGN KEY (`delivery_boy_id`) REFERENCES `users` (`user_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
