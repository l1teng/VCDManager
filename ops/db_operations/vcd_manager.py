import logging
import prettytable
from prettytable import PrettyTable
from HTMLTable import HTMLTable
from abc import ABC
from .base_operations import BaseManager


class VCDManagerOps(BaseManager, ABC):
    def __init__(self):
        super(VCDManagerOps, self).__init__()
        self.db_name = 'VCD_MANAGER'

    ''' get properties of all elements from the specified table
    @:param table, specified table name, str
    '''
    def get_table_head(self, table: str):
        try:
            table_head = [ele[0] for ele in self.run_sql_cmd('SHOW COLUMNS FROM {};'.format(table))]
            return table_head
        except TypeError:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__, 'get data of table head'))
            return None

    def get_table_elements(self, table: str):
        res = []
        table_head = self.get_table_head(table)
        check_str = self.run_sql_cmd('SELECT * FROM {};'.format(table))
        for ele in check_str:
            ele_dict = {}
            for i in range(len(table_head)):
                ele_dict[table_head[i]] = ele[i]
            res.append(ele_dict)

        return res

    def beauty_show_elements_html(self, table: str):
        tab_caption = "Table {}".format(table)
        tab = HTMLTable(caption=tab_caption)
        tab.caption.set_style({
            'font-size': '15px',
            # 'background-color': '#48a6fb',
            'text-align': 'center',
        })
        tab.set_style({
            'border-collapse': 'collapse',
            'word-break': 'keep-all',
            'white-space': 'nowrap',
            'font-size': '14px',
        })
        tab.set_cell_style({
            'border-color': '#000',
            'border-width': '1px',
            'border-style': 'solid',
            'padding': '5px',
            'text-align': 'center',
        })
        tab.set_header_row_style({
            'color': '#fff',
            'background-color': '#48a6fb',
            'font-size': '18px',
        })
        tab.set_header_cell_style({
            'padding': '15px',
        })
        table_head = [[ele[0] for ele in self.run_sql_cmd('SHOW COLUMNS FROM {};'.format(table))]]
        tab.append_header_rows(table_head)
        table_body = []
        elements = self.get_table_elements(table)
        for ele in elements:
            table_body.append(list(ele.values()))
        tab.append_data_rows(table_body)
        idx = 0
        for row in tab.iter_data_rows():
            idx += 1
            if idx % 2:
                row.set_style({'background-color': '#ffdddd', })
            else:
                row.set_style({'background-color': '#ffffff', })
        tab_html = tab.to_html()

        return tab_html

    def beauty_show_elements_prettytable(self, table: str):
        elements = self.get_table_elements(table)
        if not elements:
            return
        ptb = PrettyTable()
        ptb.set_style(prettytable.MSWORD_FRIENDLY)
        ptb_head = list(elements[0].keys())
        ptb.field_names = ptb_head
        for ele in elements:
            ptb.add_row(list(ele.values()))

        return ptb

    # insert items

    def insert_sale(self, sale_info: dict):
        self.insert_element('VCD_SALE', sale_info)

    def insert_rent(self, rent_info: dict):
        self.insert_element('VCD_RENT', rent_info)

    def insert_return(self, return_info: dict):
        self.insert_element('VCD_RETURN', return_info)

    def insert_supply(self, supply_info: dict):
        self.insert_element('VCD_SUPPLY', supply_info)

    def insert_user(self, user_info: dict):
        self.insert_element('USER', user_info)

    def insert_vcd(self, vcd_info: dict):
        self.insert_element('VCD', vcd_info)

    def insert_supplier(self, supplier_info: dict):
        self.insert_element('SUPPLIER', supplier_info)

    # query items
    def select_element(self, table: str, info: dict):
        pass

    def select_element_use_id(self, table: str, id_name: str, element_id: int):
        res = {}
        cursor_list_head = self.get_table_head(table)
        cmd = 'SELECT * FROM {} WHERE {} = {};'.format(table, id_name, element_id)
        cursor_list = self.run_sql_cmd(cmd)
        if cursor_list is None:
            logging.error('{}, [MODULE]: {}, [ACTION]: {}'.format('Connection login not establish',
                                                                  self.__class__.__name__,
                                                                  'select element via using id term'))
            return None
        elif len(cursor_list) == 0:
            return res
        cursor_list = cursor_list[0]
        for i in range(len(cursor_list_head)):
            res[cursor_list_head[i]] = cursor_list[i]

        return res
