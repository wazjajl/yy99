#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from yy99.items import Yy99Item


class Yy99Spider(scrapy.Spider):
    name = 'yy99'

    def start_requests(self):
        #pages = 2550
        pages = 2550
        for id in range(638, pages + 1):
            page_url = 'http://www.yy99.net/zhaoshang/index.asp?page=%s' % id
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        for product_html in response.css('li.company a::attr(href)').extract():
            product_res_url = "http://www.yy99.net" + product_html
            yield scrapy.Request(url=product_res_url, callback=self.parse_question)

    def parse_question(self, response):
        product_url = response.url
	product_name = response.css('table[id=zhaoshanginf] tr:nth-child(1) td:nth-child(2)::text').re('\S+')
	product_tag = "None"
	product_point = response.css('table[id=zhaoshanginf] tr:nth-child(2) td:nth-child(2)::text').re('\S+')
	investment_area =  response.css('table[id=zhaoshanginf] tr:nth-child(3) td:nth-child(2)::text').re('\S+')
	product_category = response.css('table[id=zhaoshanginf] tr:nth-child(4) td a::text').re('\S+')
	approval_number = response.css('table[id=zhaoshanginf] tr:nth-child(5) td:nth-child(2)::text').re('\S+')
	manufacture_factory = response.css('table[id=zhaoshanginf] tr:nth-child(7) td:nth-child(2)::text').re('\S+')
	product_pack = "None"
	product_specifications = response.css('table[id=zhaoshanginf] tr:nth-child(9) td:nth-child(2)::text').re('\S+')
	product_ingredients = response.css('table[id=zhaoshanginf] tr:nth-child(10) td:nth-child(2)::text').re('\S+')
	product_usage = response.css('table[id=zhaoshanginf] tr:nth-child(11) td:nth-child(2)::text').re('\S+')
	product_function = response.css('div[id="cp_xingneng"]::text').re('\S+')
	telphone = response.css('div.zsxx1 tr:nth-child(2) td:nth-child(2)::text').re('\d+')
	mobilephone = response.css('div.zsxx1 tr:nth-child(3) td:nth-child(2)::text').re('\d+')
	fax = response.css('div.zsxx1 tr:nth-child(4) td:nth-child(2)::text').re('\d+')
	contact_name = [response.css('div.zsxx1 tr:nth-child(5) td:nth-child(2)::text').re('\S+')[0]]
	qq = response.css('div.zsxx1 tr:nth-child(6) td:nth-child(2)::text').re('\S+')
	wechat = response.css('div.zsxx1 tr:nth-child(7) td:nth-child(2)::text').re('\S+')
	address = "None"
	mail = response.css('div.zsxx1 tr:nth-child(9) td:nth-child(2) a::text').re('\S+')


        # 生成ItemLoder实例
        item_list = ItemLoader(item=Yy99Item(), response=response)

        #(0)html文件名
        item_list.add_value('product_url', response.url)
        #(1)产品名称
        if product_name:
            item_list.add_value('product_name', product_name)
        else:
            item_list.add_value('product_name', 'None')
        #(2)产品标签
        item_list.add_value('product_tag', product_tag)
        #(3)产品卖点
        if product_point:
            item_list.add_value('product_point', product_point)
        else:
            item_list.add_value('product_point', 'None')
        #(4)招商区域
        if investment_area:
            item_list.add_value('investment_area', investment_area)
        else:
            item_list.add_value('investment_area', 'None')
        #(5)产品类型
        if product_category:
            item_list.add_value('product_category', product_category)
        else:
            item_list.add_value('product_category', 'None')
        #(6)批准文号
        if approval_number:
            item_list.add_value('approval_number', approval_number)
        else:
            item_list.add_value('approval_number', 'None')
        #(7)生产单位
        if manufacture_factory:
            item_list.add_value('manufacture_factory', manufacture_factory)
        else:
            item_list.add_value('manufacture_factory', 'None')
        #(8)包　　装
        item_list.add_value('product_pack', product_pack)
        #(9)规　　格
        if product_specifications:
            item_list.add_value('product_specifications', product_specifications)
        else:
            item_list.add_value('product_specifications', 'None')
        #(10)成　　份
        if product_ingredients:
            item_list.add_value('product_ingredients', product_ingredients)
        else:
            item_list.add_value('product_ingredients', 'None')
        #(11)用法用量
        if product_usage:
            item_list.add_value('product_usage', product_usage)
        else:
            item_list.add_value('product_usage', 'None')
        #(12)产品用途或者功能主治
        if product_function:
            item_list.add_value('product_function', product_function)
        else:
            item_list.add_value('product_function', 'None')
        #(13)电  话
        if telphone:
            item_list.add_value('telphone', telphone)
        else:
            item_list.add_value('telphone', 'None')
        #(14)联系手机
        if mobilephone:
            item_list.add_value('mobilephone', mobilephone)
        else:
            item_list.add_value('mobilephone', 'None')
        #(15)传真
        if fax:
            item_list.add_value('fax', fax)
        else:
            item_list.add_value('fax', 'None')
        #(16)联系人
        if contact_name:
            item_list.add_value('contact_name', contact_name)
        else:
            item_list.add_value('contact_name', 'None')
        #(17)联系QQ
        if qq:
            item_list.add_value('qq', qq)
        else:
            item_list.add_value('qq', 'None')
        #(18)联系微信
        if wechat:
            item_list.add_value('wechat', wechat)
        else:
            item_list.add_value('wechat', 'None')
        #(19)地址
        item_list.add_value('address', address)
        #(20)公司邮箱
        if mail:
            item_list.add_value('mail', mail)
        else:
            item_list.add_value('mail', 'None')

        # 返回数据给itemloder处理
        return item_list.load_item()
        #print item_list.load_item()
