USE VCD_MANAGER;

-- 视图: 库存查询
DROP VIEW IF EXISTS CHECK_STOCK;
CREATE VIEW CHECK_STOCK
AS
    SELECT VCD.id as "VCD 编号", VCD.name as "VCD 名称", STOCK.available as "现货数量", STOCK.stocked as "库存量"  FROM VCD, STOCK
WHERE VCD.id = STOCK.vcd_id;
