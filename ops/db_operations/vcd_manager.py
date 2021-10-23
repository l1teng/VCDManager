import prettytable
from prettytable import PrettyTable
from HTMLTable import HTMLTable
from abc import ABC
from .base_operations import BaseManager


class VCDManagerOps(BaseManager, ABC):
    def __init__(self, db_user, db_passwd, db_name, db_ip="127.0.0.1", db_port=3306, db_enc='utf8'):
        super(VCDManagerOps, self).__init__(db_user, db_passwd, db_name, db_ip, db_port, db_enc)

    @property
    def tables(self):
        check_str = self.run_sql_cmd('SHOW TABLES;')
        tabs = [ele[0] for ele in check_str]

        return tabs

    ''' get properties of all elements from the specified table
    @table: specified table
    '''
    def show_elements(self, table: str):
        res = []
        table_head = [ele[0] for ele in self.run_sql_cmd('SHOW COLUMNS FROM {};'.format(table))]
        check_str = self.run_sql_cmd('SELECT * FROM {};'.format(table))
        for ele in check_str:
            ele_dict = {}
            for i in range(len(table_head)):
                ele_dict[table_head[i]] = ele[i]
            res.append(ele_dict)

        return res

    def beauty_show_elements_html(self, table: str):
        tab_caption = "SELECT * FROM {};".format(table)
        tab = HTMLTable(caption=tab_caption)
        tab.caption.set_style({
            'font-size': '15px',
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
        elements = self.show_elements(table)
        for ele in elements:
            table_body.append(list(ele.values()))
        tab.append_data_rows(table_body)
        idx = 0
        for row in tab.iter_data_rows():
            idx += 1
            if idx % 2:
                row.set_style({'background-color': '#ffdddd',})
            else:
                row.set_style({'background-color': '#ffffff',})
        tab_html = tab.to_html()

        return tab_html

    def beauty_show_elements_prettytable(self, table: str):
        elements = self.show_elements(table)
        if not elements:
            return
        ptb = PrettyTable()
        ptb.set_style(prettytable.MSWORD_FRIENDLY)
        ptb_head = list(elements[0].keys())
        ptb.field_names = ptb_head
        for ele in elements:
            ptb.add_row(list(ele.values()))

        # return str(ptb)
        return ptb

    def insert_element(self, table: str, insert_element: dict):
        k_list = list(insert_element.keys())
        k_str = ''
        for ele in k_list:
            k_str += '{}, '.format(ele)
        if k_str != '':
            k_str = k_str[: -2]

        v_list = list(insert_element.values())
        v_str = ''
        for ele in v_list:
            if type(ele) == int or type(ele) == float:
                v_str += '{}, '.format(ele)
            else:
                v_str += '\"{}\", '.format(ele)
        if v_str != '':
            v_str = v_str[: -2]

        cmd = 'INSERT INTO {} ({}) VALUES ({});'.format(table, k_str, v_str)
        self.run_sql_cmd(cmd)

    def select_elements(self, table: str, info: dict):
        pass
