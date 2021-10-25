DROP DATABASE IF EXISTS VCD_MANAGER;
-- 创建 VCD 管理系统数据库
CREATE DATABASE VCD_MANAGER;

-- 使用 VCD 管理系统数据库
USE VCD_MANAGER;

DROP TABLE IF EXISTS VCD;
-- VCD 表
CREATE TABLE VCD (
    id              INT             AUTO_INCREMENT , -- VCD 编号
    name            VARCHAR(50)     NOT NULL , -- 名称
    type            VARCHAR(50), -- 类型
    actors          VARCHAR(50), -- 演员
    price           FLOAT           NOT NULL , -- 价格
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS USER;
-- 用户表
CREATE TABLE USER (
    id              INT             AUTO_INCREMENT , -- 用户编号
    name            VARCHAR(20)     NOT NULL , -- 用户姓名
    phone_no        VARCHAR(20)     NOT NULL , -- 用户手机号
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS SUPPLIER;
-- 供应商表
CREATE TABLE SUPPLIER (
    id              INT             AUTO_INCREMENT , -- 供应商编号
    name            VARCHAR (20)    NOT NULL , -- 供应商名
    phone_no        VARCHAR(20)     NOT NULL , -- 供应商电话号码
    address         VARCHAR(50)     NOT NULL , -- 供应商地址
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS STOCK;
-- 库存表
CREATE TABLE STOCK (
    id              INT             AUTO_INCREMENT , -- 库存编号
    vcd_id          INT             NOT NULL , -- VCD 编号
    available       INT             NOT NULL , -- 现货数量
    stocked         INT             NOT NULL , -- 库存量
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS VCD_SUPPLY;
-- 供应单表
CREATE TABLE VCD_SUPPLY(
    id              INT             AUTO_INCREMENT , -- 供应单编号
    supplier_id     INT             NOT NULL , -- 供应商编号
    vcd_id          INT             NOT NULL , -- VCD 编号
    number          INT             NOT NULL , -- 供应数量
    date            DATETIME        DEFAULT CURRENT_TIMESTAMP , -- 供应时间
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS VCD_SALE;
-- VCD 出售表
CREATE TABLE VCD_SALE(
    id              INT             AUTO_INCREMENT , -- VCD 出售单编号
    vcd_id          INT             NOT NULL , -- VCD 编号
    vcd_price       FLOAT           NOT NULL , -- VCD 价格
    vcd_number      INT             NOT NULL , -- VCD 数量
    user_id         INT             NOT NULL , -- 用户编号
    date            DATETIME        DEFAULT CURRENT_TIMESTAMP , -- 出售时间
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS VCD_RENT;
-- VCD 租借表
CREATE TABLE VCD_RENT(
    id              INT             AUTO_INCREMENT , -- VCD 租借单编号
    vcd_id          INT             NOT NULL , -- VCD 编号
    vcd_deposit     FLOAT           NOT NULL , -- VCD 押金
    rent_price      FLOAT           NOT NULL , -- 出租单价
    rent_number     INT             NOT NULL , -- 出租数量
    rent_limit      INT             NOT NULL , -- 出租期限
    user_id         INT             NOT NULL , -- 用户编号
    date            DATETIME        DEFAULT CURRENT_TIMESTAMP , -- 出租时间
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS VCD_RETURN;
-- VCD 归还表
CREATE TABLE VCD_RETURN(
    id              INT             AUTO_INCREMENT, -- VCD 归还单编号
    vcd_id          INT             NOT NULL , -- VCD 编号
    user_id         INT             NOT NULL , -- 用户编号
    date            DATETIME        DEFAULT CURRENT_TIMESTAMP, -- 归还时间
    expire          INT , -- 逾期天数
    PRIMARY KEY (id)
);