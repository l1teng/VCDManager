USE VCD_MANAGER;

-- 触发器：借出 VCD 更新库存现货项
CREATE TRIGGER UPDATE_AVAILABLE_IN_STOCK_WHEN_RENT AFTER INSERT ON VCD_MANAGER.VCD_RENT FOR EACH ROW
    BEGIN
        UPDATE VCD_MANAGER.STOCK SET available = available - NEW.rent_number WHERE id = NEW.vcd_id;
    END;

-- 触发器：归还 VCD 更新库存现货项
CREATE TRIGGER UPDATE_AVAILABLE_IN_STOCK_WHEN_RETURN AFTER INSERT ON VCD_MANAGER.VCD_RETURN FOR EACH ROW
    BEGIN
        UPDATE VCD_MANAGER.STOCK SET available = available + (
            -- 通过归还项中用户编号和 VCD 编号查找借出表，获取借出 VCD 数量
            SELECT rent_number FROM VCD_MANAGER.VCD_RENT Where VCD_RENT.user_id = NEW.user_id AND VCD_RENT.vcd_id = NEW.user_id
            ) WHERE vcd_id = NEW.vcd_id;
    END;

-- 触发器：售出修改库存现货项/库存项
CREATE TRIGGER UPDATE_AVAILABLE_STOCKED_IN_STOCK_WHEN_SALE AFTER INSERT ON VCD_MANAGER.VCD_SALE FOR EACH ROW
    BEGIN
        UPDATE VCD_MANAGER.STOCK SET available = available - NEW.vcd_number, stocked = stocked - NEW.vcd_number WHERE vcd_id = NEW.vcd_id;
    END;

-- 触发器：入库修改库存现货项/库存项
CREATE TRIGGER UPDATE_AVAILABLE_STOCKED_IN_STOCK_WHEN_SUPPLY AFTER INSERT ON VCD_MANAGER.VCD_SUPPLY FOR EACH ROW
    BEGIN
        UPDATE VCD_MANAGER.STOCK SET available = available + NEW.number, stocked = stocked + NEW.number WHERE vcd_id = NEW.vcd_id;
    END;
