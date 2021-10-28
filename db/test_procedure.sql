USE VCD_MANAGER;

-- 测试销售统计
CALL COUNT_SALE(timestamp('2021-10-29 00:00:00'), timestamp('2021-10-31 00:00:00'));
-- 测试租借统计
CALL COUNT_RENT(timestamp('2021-10-29 00:00:00'), timestamp('2021-10-31 00:00:00'));
-- 测试归还统计
CALL COUNT_RETURN(timestamp('2021-10-29 00:00:00'), timestamp('2021-10-31 00:00:00'));
