USE VCD_MANAGER;

-- 创建存储过程, 统计某段时间各 VCD 的销售、借还数量

-- 创建存储过程, 统计某段时间各 VCD 的销售数量
Drop PROCEDURE IF EXISTS COUNT_SALE;
CREATE PROCEDURE COUNT_SALE (IN start DATETIME, IN end DATETIME)
BEGIN
    -- SELECT vcd_id, COUNT(vcd_number) as "VCD 编号", "VCD 销售数量" FROM VCD_SALE WHERE date > start and date < end GROUP BY vcd_id;
    SELECT vcd_id as "VCD 编号", COUNT(vcd_number) as "VCD 销售数量" FROM VCD_SALE WHERE date > start and date < end GROUP BY vcd_id;
END;

-- 创建存储过程, 统计某段时间各 VCD 的租借数量
Drop PROCEDURE IF EXISTS COUNT_RENT;
CREATE PROCEDURE COUNT_RENT (IN start DATETIME, IN end DATETIME)
BEGIN
    SELECT vcd_id as "VCD 编号", COUNT(rent_number) as "VCD 租借数量" FROM VCD_RENT WHERE date > start and date < end GROUP BY vcd_id;
end;

-- 创建存储过程, 统计某段时间各 VCD 的归还数量
Drop PROCEDURE IF EXISTS COUNT_RETURN;
CREATE PROCEDURE COUNT_RETURN (IN start DATETIME, IN end DATETIME)
BEGIN
    SELECT VCD_RETURN.vcd_id as "VCD 编号", COUNT(VCD_RENT.rent_number) as "VCD 归还数量" FROM VCD_RETURN, VCD_RENT WHERE VCD_RETURN.date > start and VCD_RETURN.date < end GROUP BY VCD_RETURN.vcd_id;
end;
