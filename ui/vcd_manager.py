import sys
import logging
from PyQt5 import QtWidgets
from ops import VCDManagerOps
from .ui_vcd_manager import Ui_VCDManager


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
        sale_info['vcd_name'] = self.tab_sale_le_vcd_name.text()
        sale_info['user_id'] = self.tab_sale_sb_user_id.value()
        sale_info['user_name'] = self.tab_sale_le_user_name.text()
        sale_info['sale_num'] = self.tab_sale_sb_sale_num.value()
        sale_info['sale_price'] = self.tab_sale_dsb_sale_price.value()
        # data valid check
        if sale_info['sale_num'] == 0:
            return
        # TODO: not finished

    # TAB: rent VCD

    def rent_vcd(self):
        rent_info = {}
        rent_info['vcd_id'] = self.tab_rent_sb_vcd_id.value()
        rent_info['vcd_name'] = self.tab_rent_le_vcd_name.text()
        rent_info['user_id'] = self.tab_rent_sb_user_id.value()
        rent_info['user_name'] = self.tab_rent_le_user_name.text()
        rent_info['rent_num'] = self.tab_rent_sb_rent_num.value()
        rent_info['per_price'] = self.tab_rent_dsb_per_price.value()
        rent_info['rent_price'] = self.tab_rent_dsb_rent_price.value()
        rent_info['rent_limit'] = self.tab_rent_sb_rent_limit.value()
        # data valid check
        pass
        # TODO: not finished

    # TAB: return VCD

    def return_vcd(self):
        return_info = {}
        return_info['vcd_id'] = self.tab_return_sb_vcd_id.value()
        return_info['vcd_name'] = self.tab_return_le_vcd_name.text()
        return_info['user_id'] = self.tab_return_sb_user_id.value()
        return_info['user_name'] = self.tab_return_le_user_name.text()
        pass
        # TODO: not finished
