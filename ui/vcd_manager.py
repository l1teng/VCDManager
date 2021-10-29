import logging
from PyQt5 import QtWidgets
from ops import VCDManagerOps
from ui.ui_vcd_manager import Ui_VCDManager


# VCD MANAGER
class VCDManager(QtWidgets.QTabWidget, Ui_VCDManager):
    def __init__(self, parent=None):
        super(VCDManager, self).__init__(parent=parent)
        # db ops
        # self.__db_opts = VCDManagerOpt().parse()
        self.login_info = {}
        self.db_ops = VCDManagerOps()
        self.setupUi(self)

    # TAB: login
    def db_login(self):
        # fetch login info from input interface
        self.login_info['db_user'] = self.tb1_le_user.text()
        self.login_info['db_passwd'] = self.tb1_le_pswd.text()
        self.login_info['db_ip'] = self.tb1_le_ip.text()
        self.login_info['db_port'] = self.tb1_sb_port.value()
        self.db_ops.connection_establish(self.login_info['db_user'], self.login_info['db_passwd'],
                                         self.login_info['db_ip'], self.login_info['db_port'], re_login=True)
        self.db_refresh()
        logging.info('[MODULE]: {}, [ACTION]: login, [STATUS]: {}, [USER]: {}, [IP]: {}, [PORT]: {}'.format(
            self.__class__.__name__, self.db_ops.connection_status, self.login_info['db_user'],
            self.login_info['db_ip'], self.login_info['db_port']))
        # try:
        #     self.db_ops = VCDManagerOps(self.__db_opts.db_user, self.__db_opts.db_passwd, self.__db_opts.db)
        # except pymysql.err.OperationalError:
        #     # login info error
        #     self.__db_opts.__db_login = False
        #     logging.error('[ACTION]: login, [STATUS]: {}, [USER]: {}, [IP]: {}, [PORT]: {}'.format(
        #         self.__db_opts.__db_login, self.__db_opts.db_user, self.__db_opts.db_ip, self.__db_opts.db_port))
        # else:
        #     self.__db_opts.__db_login = True
        #     logging.info('[ACTION]: login, [STATUS]: {}, [USER]: {}, [IP]: {}, [PORT]: {}'.format(
        #         self.__db_opts.__db_login, self.__db_opts.db_user, self.__db_opts.db_ip, self.__db_opts.db_port))
        # self.db_refresh()

    def db_logout(self):
        self.db_ops.connection_close()
        self.db_refresh()
        logging.info('[MODULE]: {}, [ACTION]: {}, [STATUS]: {}'.format(self.__class__.__name__, 'logout',
                                                                       self.db_ops.connection_status))

    def db_refresh(self):
        self.tb1_le_status.setText('STATUS: {}'.format(self.db_ops.connection_status))
        logging.info('[MODULE]: {}, [ACTION]: {}, [STATUS]: {}'.format(self.__class__.__name__, 'login status refresh',
                                                                       self.db_ops.connection_status))

    # TAB: check data from tables
    def tb_data_show(self):
        # process table head
        table_name = self.tab2_cb_tab_select.currentText()
        table_head = self.db_ops.get_table_head(table_name)
        try:
            self.tab2_tw_data.setColumnCount(len(table_head))
        except TypeError:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__, 'show table data'))
            return
        self.tab2_tw_data.setHorizontalHeaderLabels(table_head)
        # process data for table body
        table_elements = self.db_ops.get_table_elements(table_name)
        self.tab2_tw_data.setRowCount(len(table_elements))
        for i in range(len(table_elements)):
            v_i = list(table_elements[i].values())
            for j in range(len(v_i)):
                self.tab2_tw_data.setItem(i, j, QtWidgets.QTableWidgetItem(str(v_i[j])))
        logging.info('[MODULE]: {}, [ACTION]: {}'.format(self.__class__.__name__,
                                                         'show all data of the specified table'))

    def tb_data_clear(self):
        self.tab2_tw_data.clear()
        logging.info('[MODULE]: {}, [ACTION]: {}'.format(self.__class__.__name__,
                                                         'clear illustration of the specified table'))

    # TAB: sale VCD

    def sale_vcd(self):
        sale_info = {}
        sale_info['vcd_id'] = self.tab_sale_sb_vcd_id.value()
        # sale_info['vcd_name'] = self.tab_sale_le_vcd_name.text()
        sale_info['user_id'] = self.tab_sale_sb_user_id.value()
        # sale_info['user_name'] = self.tab_sale_le_user_name.text()
        sale_info['vcd_number'] = self.tab_sale_sb_sale_num.value()
        sale_info['vcd_price'] = self.tab_sale_dsb_sale_price.value()
        self.db_ops.insert_sale(sale_info)
        self.sale_vcd_clear()

    def sale_update_vcd_name(self):
        vcd_id = self.tab_sale_sb_vcd_id.value()
        vcd_ele = self.db_ops.select_element_use_id('VCD', 'id', vcd_id)
        if vcd_ele is None:
            self.tab_sale_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[SALE] update vcd name when vcd id is changed'))
        elif len(vcd_ele) == 0:
            self.tab_sale_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[SALE] update vcd name when vcd id is changed'))
        else:
            self.tab_sale_le_vcd_name.setText(vcd_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[SALE] update vcd name when vcd id is changed'))

    def sale_update_user_name(self):
        user_id = self.tab_sale_sb_user_id.value()
        user_ele = self.db_ops.select_element_use_id('USER', 'id', user_id)
        if user_ele is None:
            self.tab_sale_le_user_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[SALE] update user name when user id is changed'))
        elif len(user_ele) == 0:
            self.tab_sale_le_user_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[SALE] update user name when user id is changed'))
        else:
            self.tab_sale_le_user_name.setText(user_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[SALE] update user name when user id is changed'))

    def sale_vcd_clear(self):
        self.tab_sale_sb_vcd_id.setValue(0)
        self.tab_sale_le_vcd_name.setText('')
        self.tab_sale_sb_user_id.setValue(0)
        self.tab_sale_le_user_name.setText('')
        self.tab_sale_sb_sale_num.setValue(0)
        self.tab_sale_dsb_sale_price.setValue(0)

    # TAB: rent VCD

    def rent_vcd(self):
        rent_info = {}
        rent_info['vcd_id'] = self.tab_rent_sb_vcd_id.value()
        # rent_info['vcd_name'] = self.tab_rent_le_vcd_name.text()
        rent_info['user_id'] = self.tab_rent_sb_user_id.value()
        # rent_info['user_name'] = self.tab_rent_le_user_name.text()
        rent_info['rent_number'] = self.tab_rent_sb_rent_num.value()
        rent_info['rent_price'] = self.tab_rent_dsb_per_price.value()
        rent_info['vcd_deposit'] = self.tab_rent_dsb_rent_price.value()
        rent_info['rent_limit'] = self.tab_rent_sb_rent_limit.value()
        self.db_ops.insert_rent(rent_info)
        self.rent_vcd_clear()

    def rent_update_vcd_name(self):
        vcd_id = self.tab_rent_sb_vcd_id.value()
        vcd_ele = self.db_ops.select_element_use_id('VCD', 'id', vcd_id)
        if vcd_ele is None:
            self.tab_rent_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[RENT] update vcd name when vcd id is changed'))
        elif len(vcd_ele) == 0:
            self.tab_rent_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[RENT] update vcd name when vcd id is changed'))
        else:
            self.tab_rent_le_vcd_name.setText(vcd_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[RENT] update vcd name when vcd id is changed'))

    def rent_update_user_name(self):
        user_id = self.tab_rent_sb_user_id.value()
        user_ele = self.db_ops.select_element_use_id('USER', 'id', user_id)
        if user_ele is None:
            self.tab_rent_le_user_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[RENT] update user name when user id is changed'))
        elif len(user_ele) == 0:
            self.tab_rent_le_user_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[RENT] update user name when user id is changed'))
        else:
            self.tab_rent_le_user_name.setText(user_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[RENT] update user name when user id is changed'))

    def rent_vcd_clear(self):
        self.tab_rent_sb_vcd_id.setValue(0)
        self.tab_rent_le_vcd_name.setText('')
        self.tab_rent_sb_user_id.setValue(0)
        self.tab_rent_le_user_name.setText('')
        self.tab_rent_sb_rent_num.setValue(0)
        self.tab_rent_dsb_per_price.setValue(0)
        self.tab_rent_dsb_rent_price.setValue(0)
        self.tab_rent_sb_rent_limit.setValue(0)

    # TAB: return VCD

    def return_vcd(self):
        return_info = {}
        return_info['vcd_id'] = self.tab_return_sb_vcd_id.value()
        # return_info['vcd_name'] = self.tab_return_le_vcd_name.text()
        return_info['user_id'] = self.tab_return_sb_user_id.value()
        # return_info['user_name'] = self.tab_return_le_user_name.text()
        # return_info['expire'] =
        self.db_ops.insert_return(return_info)
        self.return_vcd_clear()

    def return_update_vcd_name(self):
        vcd_id = self.tab_return_sb_vcd_id.value()
        vcd_ele = self.db_ops.select_element_use_id('VCD', 'id', vcd_id)
        if vcd_ele is None:
            self.tab_return_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[RETURN] update vcd name when vcd id is changed'))
        elif len(vcd_ele) == 0:
            self.tab_return_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[RETURN] update vcd name when vcd id is changed'))
        else:
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[RETURN] update vcd name when vcd id is changed'))
            self.tab_return_le_vcd_name.setText(vcd_ele['name'])

    def return_update_user_name(self):
        user_id = self.tab_return_sb_user_id.value()
        user_ele = self.db_ops.select_element_use_id('USER', 'id', user_id)
        if user_ele is None:
            self.tab_return_le_user_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[RETURN] update user name when user id is changed'))
        elif len(user_ele) == 0:
            self.tab_return_le_user_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[RETURN] update user name when user id is changed'))
        else:
            self.tab_return_le_user_name.setText(user_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[RETURN] update user name when user id is changed'))

    def return_vcd_clear(self):
        self.tab_return_sb_vcd_id.setValue(0)
        self.tab_return_le_vcd_name.setText('')
        self.tab_return_sb_user_id.setValue(0)
        self.tab_return_le_user_name.setText('')

    # TAB: supply VCD

    def supply_vcd(self):
        supply_info = {}
        supply_info['supplier_id'] = self.tab_stock_sb_supplier_id.value()
        supply_info['vcd_id'] = self.tab_stock_sb_vcd_id.value()
        supply_info['supply_num'] = self.tab_stock_sb_supply_num.value()
        self.db_ops.insert_supply(supply_info)
        self.supply_vcd_clear()

    def supply_update_supplier_name(self):
        supplier_id = self.tab_stock_sb_supplier_id.value()
        supplier_ele = self.db_ops.select_element_use_id('SUPPLIER', 'id', supplier_id)
        if supplier_ele is None:
            self.tab_stock_le_supplier_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[SUPPLY] update supplier name when supplier id is '
                                                                  'changed'))
        elif len(supplier_ele) == 0:
            self.tab_stock_le_supplier_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[SUPPLY] update supplier name when supplier id is '
                                                                  'changed'))
        else:
            self.tab_stock_le_supplier_name.setText(supplier_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[SUPPLY] update supplier name when supplier id is '
                                                                 'changed'))

    def supply_update_vcd_name(self):
        vcd_id = self.tab_stock_sb_vcd_id.value()
        vcd_ele = self.db_ops.select_element_use_id('VCD', 'id', vcd_id)
        if vcd_ele is None:
            self.tab_stock_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[SUPPLY] update vcd name when vcd id is changed'))
        elif len(vcd_ele) == 0:
            self.tab_stock_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[SUPPLY] update vcd name when vcd id is changed'))
        else:
            self.tab_stock_le_vcd_name.setText(vcd_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[SUPPLY] update vcd name when vcd id is changed'))

    def supply_vcd_clear(self):
        self.tab_stock_sb_vcd_id.setValue(0)
        self.tab_stock_le_vcd_name.setText('')
        self.tab_stock_sb_supplier_id.setValue(0)
        self.tab_stock_le_supplier_name.setText('')
        self.tab_stock_sb_supply_num.setValue(0)

    # TAB: user/ VCD query

    def user_stat_update_user_name(self):
        user_id = self.tab_slct_br_sb_user_id.value()
        user_ele = self.db_ops.select_element_use_id('USER', 'id', user_id)
        if user_ele is None:
            self.tab_slct_br_le_user_name .setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[USER STAT] update vcd name when vcd id is changed'))
        elif len(user_ele) == 0:
            self.tab_slct_br_le_user_name .setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[USER STAT] update vcd name when vcd id is changed'))
        else:
            self.tab_slct_br_le_user_name .setText(user_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[USER STAT] update vcd name when vcd id is changed'))
    
    def __user_stat_query_confirm_rent(self, tb_head, tb_body):
        try:
            self.tab_slct_br_tw_user_rent.setColumnCount(len(tb_head))
        except TypeError:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__, 'show user rent stat'))
            return
        self.tab_slct_br_tw_user_rent.setHorizontalHeaderLabels(tb_head)
        self.tab_slct_br_tw_user_rent.setRowCount(len(tb_body))
        for i in range(len(tb_body)):
            v_i = list(tb_body[i])
            for j in range(len(v_i)):
                self.tab_slct_br_tw_user_rent.setItem(i, j, QtWidgets.QTableWidgetItem(str(v_i[j])))
            logging.info('[MODULE]: {}, [ACTION]: {}'.format(self.__class__.__name__, 'show user rent stat'))

    def __user_stat_query_confirm_return(self, tb_head, tb_body):
        try:
            self.tab_slct_br_tw_user_return.setColumnCount(len(tb_head))
        except TypeError:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__, 'show user return stat'))
            return
        self.tab_slct_br_tw_user_return.setHorizontalHeaderLabels(tb_head)
        self.tab_slct_br_tw_user_return.setRowCount(len(tb_body))
        for i in range(len(tb_body)):
            v_i = list(tb_body[i])
            for j in range(len(v_i)):
                self.tab_slct_br_tw_user_return.setItem(i, j, QtWidgets.QTableWidgetItem(str(v_i[j])))
            logging.info('[MODULE]: {}, [ACTION]: {}'.format(self.__class__.__name__, 'show user return stat'))

    def user_stat_query_confirm(self):
        user_id = self.tab_slct_br_sb_user_id.value()
        # rent process
        rent_head = self.db_ops.get_table_head('VCD_RENT')
        rent_cmd_body = 'SELECT {} FROM {} WHERE {};'.format('*', 'VCD_RENT', 'VCD_RENT.user_id = {}'.format(user_id))
        rent_body = self.db_ops.run_sql_cmd(rent_cmd_body)
        self.__user_stat_query_confirm_rent(rent_head, rent_body)
        
        # return process
        return_head = self.db_ops.get_table_head('VCD_RENT')
        return_cmd_body = 'SELECT {} FROM {} WHERE {};'.format('*', 'VCD_RETURN',
                                                               'VCD_RETURN.user_id = {}'.format(user_id))
        return_body = self.db_ops.run_sql_cmd(return_cmd_body)
        self.__user_stat_query_confirm_return(return_head, return_body)

    def user_stat_query_clear(self):
        self.tab_slct_br_sb_user_id.setValue(0)
        self.tab_slct_br_le_user_name.setText('')
        self.tab_slct_br_tw_user_rent.clear()
        self.tab_slct_br_tw_user_return.clear()

    def vcd_stat_update_vcd_name(self):
        vcd_id = self.tab_slct_br_sb_vcd_id.value()
        vcd_ele = self.db_ops.select_element_use_id('VCD', 'id', vcd_id)
        if vcd_ele is None:
            self.tab_slct_br_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  '[VCD STAT] update user name when user id is changed'))
        elif len(vcd_ele) == 0:
            self.tab_slct_br_le_vcd_name.setText('INVALID')
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('No id-specified element, invalid id',
                                                                  self.__class__.__name__,
                                                                  '[VCD STAT] update user name when user id is changed'))
        else:
            self.tab_slct_br_le_vcd_name.setText(vcd_ele['name'])
            logging.info('{}, [MODULE]: {}, [ACTION]: {}'.format('Update success',
                                                                 self.__class__.__name__,
                                                                 '[VCD STAT] update user name when user id is changed'))

    def vcd_stat_query_confirm(self):
        vcd_id = self.tab_slct_br_sb_vcd_id.value()

        # TODO: not finished
        pass

    def vcd_stat_query_clear(self):
        self.tab_slct_br_sb_vcd_id.setValue(0)
        self.tab_slct_br_lb_vcd_name.setText('')
        self.tab_slct_br_tw_vcd_stat.clear()

    # TAB: sign up

    def signup_user(self):
        user_info = {}
        user_info['name'] = self.tab_signup_le_user_name.text()
        user_info['phone_no'] = self.tab_signup_le_user_tel_pre.text() + '-' + self.tab_signup_le_user_tel_ext.text()
        self.db_ops.insert_user(user_info)
        self.signup_user_clear()

    def signup_user_clear(self):
        self.tab_signup_le_user_name.clear()
        self.tab_signup_le_user_tel_pre.setText('+86')
        self.tab_signup_le_user_tel_ext.setText('')

    def signup_vcd(self):
        vcd_info = {}
        vcd_info['name'] = self.tab_signup_le_vcd_name.text()
        vcd_info['type'] = self.tab_signup_cb_vcd_type.currentText()
        vcd_info['actors'] = self.tab_signup_le_vcd_actors.text()
        vcd_info['price'] = self.tab_signup_dsb_vcd_price.value()
        self.db_ops.insert_vcd(vcd_info)
        self.signup_vcd_clear()

    def signup_vcd_clear(self):
        self.tab_signup_le_vcd_name.setText('')
        self.tab_signup_cb_vcd_type.setCurrentIndex(0)
        self.tab_signup_le_vcd_actors.setText('')
        self.tab_signup_dsb_vcd_price.setValue(0)

    def signup_supplier(self):
        supplier_info = {}
        supplier_info['name'] = self.tab_signup_le_supplier_name.text()
        supplier_info['phone_no'] = self.tab_signup_le_supplier_tel_pre.text() + '-' + \
                                    self.tab_signup_le_supplier_tel_ext.text()
        supplier_info['address'] = self.tab_signup_le_supplier_addr.text()
        self.db_ops.insert_supplier(supplier_info)
        self.signup_supplier_clear()

    def signup_supplier_clear(self):
        self.tab_signup_le_supplier_name.setText('')
        self.tab_signup_le_supplier_addr.setText('')
        self.tab_signup_le_supplier_tel_pre.setText('+86')
        self.tab_signup_le_supplier_tel_ext.setText('')
