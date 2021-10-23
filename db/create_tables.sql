-- 创建 VCD 管理系统数据库
CREATE DATABASE VCD_MANAGER;

-- 使用 VCD 管理系统数据库
USE VCD_MANAGER;

-- VCD 表
CREATE TABLE VCD (
    id INT PRIMARY KEY AUTO_INCREMENT, -- VCD 编号
    name VARCHAR(50), -- 名称
    type VARCHAR(50), -- 类型
    actors VARCHAR(50), -- 演员
    price FLOAT -- 价格
);

-- 用户表
CREATE TABLE USER (
    id INT PRIMARY KEY AUTO_INCREMENT, -- 用户编号
    name VARCHAR(20), -- 用户姓名
    phone_no VARCHAR(20) -- 用户手机号
);

-- 供应商表
CREATE TABLE SUPPLIER (
    id INT PRIMARY KEY AUTO_INCREMENT, -- 供应商编号
    -- vcd_id INT, -- VCD 编号
    phone_no VARCHAR(20), -- 供应商电话号码
    address VARCHAR(50) -- 供应商地址
);

-- 库存表
CREATE TABLE STOCK (
    id INT PRIMARY KEY AUTO_INCREMENT, -- 库存编号
    vcd_id INT, -- VCD 编号
    available INT , -- 现货数量
    stocked INT -- 库存量
);

-- 供应单表
CREATE TABLE VCD_SUPPLY(
    id INT PRIMARY KEY AUTO_INCREMENT, -- 供应单编号
    supplier_id INT, -- 供应商编号
    vcd_id INT, -- VCD 编号
    number INT -- 供应数量
);

-- VCD 出售表
CREATE TABLE VCD_SALE(
    id INT PRIMARY KEY AUTO_INCREMENT, -- VCD 出售单编号
    vcd_id INT, -- VCD 编号
    vcd_price FLOAT, -- VCD 价格
    vcd_number INT, -- VCD 数量
    user_id INT, -- 用户编号
    date DATETIME -- 出售时间
);

-- VCD 租借表
CREATE TABLE VCD_RENT(
    id INT PRIMARY KEY AUTO_INCREMENT, -- VCD 租借单编号
    vcd_id INT, -- VCD 编号
    vcd_deposit FLOAT, -- VCD 押金
    rent_price FLOAT, -- 出租单价
    rent_number INT, -- 出租数量
    rent_limit INT, -- 出租期限
    date DATETIME, -- 出租时间
    user_id INT -- 用户编号
);

-- VCD 归还表
CREATE TABLE VCD_RETURN(
    id INT PRIMARY KEY AUTO_INCREMENT, -- VCD 归还单编号
    vcd_id INT, -- VCD 编号
    user_id INT, -- 用户编号
    date DATETIME, -- 归还时间
    expire INT -- 预期天数
);