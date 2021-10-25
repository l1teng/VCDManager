USE VCD_MANAGER;

-- add USERs
INSERT INTO USER (id, name, phone_no) VALUES (1, "A", "+86-13800000001");
INSERT INTO USER (id, name, phone_no) VALUES (2, "B", "+86-13800000002");
INSERT INTO USER (id, name, phone_no) VALUES (3, "C", "+86-13800000003");
INSERT INTO USER (id, name, phone_no) VALUES (4, "D", "+86-13800000004");
INSERT INTO USER (id, name, phone_no) VALUES (5, "D", "+86-13800000005");

-- add VCDs
INSERT INTO VCD (id, name, type, actors, price) VALUES (1, "VCD1", "action", "Terry", 12.01);
INSERT INTO VCD (id, name, type, actors, price) VALUES (2, "VCD2", "love", "Bluce", 12.02);
INSERT INTO VCD (id, name, type, actors, price) VALUES (3, "VCD3", "comedy", "Bin", 12.03);
INSERT INTO VCD (id, name, type, actors, price) VALUES (4, "VCD4", "love", "Rice", 12.04);
INSERT INTO VCD (id, name, type, actors, price) VALUES (5, "VCD5", "love", "Joe", 12.05);

-- add SUPPLIERs
INSERT INTO SUPPLIER (id, name, phone_no, address) VALUES (1, "SUPPLIER1", "+86-0751-242001", "CA");
INSERT INTO SUPPLIER (id, name, phone_no, address) VALUES (2, "SUPPLIER2", "+86-0751-242002", "LA");
INSERT INTO SUPPLIER (id, name, phone_no, address) VALUES (3, "SUPPLIER3", "+86-0751-242003", "NY");
INSERT INTO SUPPLIER (id, name, phone_no, address) VALUES (4, "SUPPLIER4", "+86-0751-242004", "WT");
INSERT INTO SUPPLIER (id, name, phone_no, address) VALUES (5, "SUPPLIER5", "+86-0751-242005", "NT");

-- add STOCKs
INSERT INTO STOCK (id, vcd_id, available, stocked) VALUES (1, 1, 12, 15);
INSERT INTO STOCK (id, vcd_id, available, stocked) VALUES (2, 2, 13, 16);
INSERT INTO STOCK (id, vcd_id, available, stocked) VALUES (3, 3, 14, 17);
INSERT INTO STOCK (id, vcd_id, available, stocked) VALUES (4, 4, 15, 18);
INSERT INTO STOCK (id, vcd_id, available, stocked) VALUES (5, 5, 16, 19);

-- test trigger :: UPDATE_AVAILABLE_IN_STOCK_WHEN_RENT
INSERT INTO VCD_RENT (id, vcd_id, vcd_deposit, rent_price, rent_number, rent_limit, user_id) VALUES (1, 1, 12.01, 1.01, 2, 7, 1);
INSERT INTO VCD_RENT (id, vcd_id, vcd_deposit, rent_price, rent_number, rent_limit, user_id) VALUES (2, 1, 12.01, 1.01, 2, 7, 1);
INSERT INTO VCD_RETURN (id, vcd_id, user_id, expire) VALUES (1, 1, 1, 0);
INSERT INTO VCD_SALE (id, vcd_id, vcd_price, vcd_number, user_id) VALUES (1, 1, 12.01, 2, 1);
INSERT INTO VCD_SUPPLY (id, supplier_id, vcd_id, number) VALUES (1, 1, 1, 2);