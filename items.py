# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
itemlist = ['report_date','report_name','avg_roe', 'np_per_share', 'operate_cash_flow_ps', 'basic_eps', 'capital_reserve', 'undistri_profit_ps', 'net_interest_of_total_assets', 'net_selling_rate', 'gross_selling_rate', 'total_revenue', 'operating_income_yoy', 'net_profit_atsopc', 'net_profit_atsopc_yoy', 'net_profit_after_nrgal_atsolc', 'np_atsopc_nrgal_yoy', 'ore_dlt', 'rop', 'asset_liab_ratio', 'current_ratio', 'quick_ratio', 'equity_multiplier', 'equity_ratio', 'holder_equity', 'ncf_from_oa_to_total_liab', 'inventory_turnover_days', 'receivable_turnover_days', 'accounts_payable_turnover_days', 'cash_cycle', 'operating_cycle', 'total_capital_turnover', 'inventory_turnover', 'account_receivable_turnover', 'accounts_payable_turnover', 'current_asset_turnover_rate', 'fixed_asset_turnover_ratio']

class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    #collection = 'jd'
    id = scrapy.Field()
    price = scrapy.Field()
    keyword = scrapy.Field()
    title = scrapy.Field()
    promo_words = scrapy.Field()
    sale_num = scrapy.Field()
    href = scrapy.Field()
    shop = scrapy.Field()
    img = scrapy.Field()
    img_small = scrapy.Field()
    pass

class TmailItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    price = scrapy.Field()
    keyword = scrapy.Field()
    title = scrapy.Field()
    promo_words = scrapy.Field()
    sale_num = scrapy.Field()
    href = scrapy.Field()
    shop = scrapy.Field()
    img = scrapy.Field()
    img_small = scrapy.Field()
    pass
"""
class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    collection = 'jd'
    id = scrapy.Field()
    price = scrapy.Field()
    keyword = scrapy.Field()
    title = scrapy.Field()
    promo_words = scrapy.Field()
    comment_num = scrapy.Field()
    href = scrapy.Field()
    shop = scrapy.Field()
    img = scrapy.Field()
    pass
"""
class GSJJItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    org_name_cn = scrapy.Field()
    pre_name_cn = scrapy.Field()
    provincial_name = scrapy.Field()
    actual_controller = scrapy.Field()
    classi_name = scrapy.Field()
    main_operation_business = scrapy.Field()
    org_cn_introduction = scrapy.Field()
    chairman = scrapy.Field()
    
    general_manager = scrapy.Field()
    secretary = scrapy.Field()
    established_date = scrapy.Field()
    reg_asset = scrapy.Field()
    staff_num = scrapy.Field()
    executives_nums = scrapy.Field()
    listed_date = scrapy.Field()
    actual_issue_vol = scrapy.Field()
    issue_price = scrapy.Field()
    actual_rc_net_amt = scrapy.Field()
    pe_after_issuing = scrapy.Field()
    online_success_rate_of_issue = scrapy.Field()
    telephone = scrapy.Field()
    postcode = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
    org_website = scrapy.Field()
    reg_address_cn = scrapy.Field()
    office_address_cn = scrapy.Field()
    pass

class ZYZBItem(scrapy.Item):
    id = scrapy.Field()
    quote_name = scrapy.Field()
    report_date = scrapy.Field()
    report_name = scrapy.Field()
    avg_roe = scrapy.Field()
    np_per_share = scrapy.Field()
    operate_cash_flow_ps = scrapy.Field()
    basic_eps = scrapy.Field()
    capital_reserve = scrapy.Field()
    undistri_profit_ps = scrapy.Field()
    net_interest_of_total_assets = scrapy.Field()
    net_selling_rate = scrapy.Field()
    gross_selling_rate = scrapy.Field()
    total_revenue = scrapy.Field()
    operating_income_yoy = scrapy.Field()
    net_profit_atsopc = scrapy.Field()
    net_profit_atsopc_yoy = scrapy.Field()
    net_profit_after_nrgal_atsolc = scrapy.Field()
    np_atsopc_nrgal_yoy = scrapy.Field()
    ore_dlt = scrapy.Field()
    rop = scrapy.Field()
    asset_liab_ratio = scrapy.Field()
    current_ratio = scrapy.Field()
    quick_ratio = scrapy.Field()
    equity_multiplier = scrapy.Field()
    equity_ratio = scrapy.Field()
    holder_equity = scrapy.Field()
    ncf_from_oa_to_total_liab = scrapy.Field()
    inventory_turnover_days = scrapy.Field()
    receivable_turnover_days = scrapy.Field()
    accounts_payable_turnover_days = scrapy.Field()
    cash_cycle = scrapy.Field()
    operating_cycle = scrapy.Field()
    total_capital_turnover = scrapy.Field()
    inventory_turnover = scrapy.Field()
    account_receivable_turnover = scrapy.Field()
    accounts_payable_turnover = scrapy.Field()
    current_asset_turnover_rate = scrapy.Field()
    fixed_asset_turnover_ratio = scrapy.Field()
